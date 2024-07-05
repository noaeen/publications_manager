import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import data_store  # Import the data script
import json

# User credentials
users = {
    'mohammad': {'name': 'mohammad', 'password': 'mn'},
    'karim': {'name': 'karim', 'password': 'k'}
}

# Authentication function
def authenticate(username, password):
    if username in users:
        if users[username]['password'] == password:
            return True, users[username]['name'], username
        else:
            st.error("Incorrect password")
    else:
        st.error("Username not found")
    return False, None, None

# Load data from the data store script
authors_df = pd.DataFrame(data_store.authors_data)
papers_df = pd.DataFrame(data_store.papers_data)

# Function to save DataFrame back to data_store.py
def save_data(authors_df, papers_df):
    authors_list = authors_df.to_dict(orient='records')
    papers_list = papers_df.to_dict(orient='records')
    with open('data_store.py', 'w') as f:
        f.write(f"authors_data = {json.dumps(authors_list, indent=4)}\n\n")
        f.write(f"papers_data = {json.dumps(papers_list, indent=4)}\n")

# Function to update paper IDs
def update_paper_ids():
    papers_df["ID"] = range(1, len(papers_df) + 1)

update_paper_ids()

# Function to update author projects
def update_author_projects():
    for idx, row in authors_df.iterrows():
        projects = []
        for i in range(1, 11):
            projects += papers_df[papers_df[f"Author{i}"] == row["Name"]]["Project Name"].tolist()
        authors_df.at[idx, "Projects"] = ", ".join(projects)

update_author_projects()

# Initialize session state for authentication and user role
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
    st.session_state['user_role'] = None
    st.session_state['name'] = ''
    st.session_state['username'] = ''

# Prompt viewer/editor selection
role_selection = st.sidebar.radio("Select Role", ["Viewer", "Editor"])

if role_selection == "Editor":
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.button("Login"):
        authentication_status, name, username = authenticate(username, password)
        if authentication_status:
            st.session_state['authenticated'] = True
            st.session_state['user_role'] = role_selection
            st.session_state['name'] = name
            st.session_state['username'] = username
            st.sidebar.success(f"Welcome {name}")
        else:
            st.sidebar.error("Username/password is incorrect")
elif role_selection == "Viewer":
    st.session_state['authenticated'] = True
    st.session_state['user_role'] = role_selection
    st.session_state['name'] = "Viewer"
    st.session_state['username'] = "viewer"

if st.session_state['authenticated']:
    st.sidebar.title(f"Welcome {st.session_state['name']}")
    if st.sidebar.button("Logout"):
        st.session_state['authenticated'] = False
        st.session_state['user_role'] = None
        st.session_state['name'] = ''
        st.session_state['username'] = ''
        st.experimental_rerun()

    # Sidebar navigation
    menu = st.sidebar.radio("Go to", ["Papers", "Authors", "Authors by Selection"])

    if menu == "Papers":
        st.title("Papers")

        # Define grid options
        gb = GridOptionsBuilder.from_dataframe(papers_df)
        gb.configure_default_column(editable=st.session_state['user_role'] == 'Editor')
        gb.configure_column("Status", editable=st.session_state['user_role'] == 'Editor', cellEditor='agSelectCellEditor', cellEditorParams={'values': ["Not Started", "In Progress", "Completed", "Submitted"]})
        gb.configure_column("Submission Status", editable=st.session_state['user_role'] == 'Editor', cellEditor='agSelectCellEditor', cellEditorParams={'values': ["Not Submitted", "Submitted"]})
        for i in range(1, 11):
            gb.configure_column(f"Author{i}", editable=st.session_state['user_role'] == 'Editor', cellEditor='agSelectCellEditor', cellEditorParams={'values': authors_df["Name"].tolist()})
        gb.configure_column("Selected", editable=st.session_state['user_role'] == 'Editor', cellEditor='agCheckboxCellEditor')
        grid_options = gb.build()

        # Auto-size all columns
        grid_options['defaultColDef']['resizable'] = True
        grid_options['defaultColDef']['autoHeight'] = True

        # Display the table
        response = AgGrid(
            papers_df.reset_index(drop=True),  # Remove the default index
            gridOptions=grid_options,
            update_mode='MODEL_CHANGED',
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
            allow_unsafe_jscode=True,
            enable_enterprise_modules=True,
        )

        # Save changes
        updated_df = response['data'].copy()  # Create a copy to avoid modifying the original DataFrame
        updated_df.reset_index(drop=True, inplace=True)  # Remove the default index
        if st.session_state['user_role'] == 'Editor' and st.button("Save Changes"):
            papers_df = pd.DataFrame(updated_df)
            update_paper_ids()
            save_data(authors_df, papers_df)
            st.success("Changes saved successfully!")

        # Show only selected papers
        selected_papers = papers_df[papers_df["Selected"]].reset_index(drop=True)
        if not selected_papers.empty:
            st.subheader("Selected Papers")
            st.table(selected_papers.drop(columns=["Selected"]))

        # Button to add new paper
        if st.session_state['user_role'] == 'Editor' and st.button("Add Paper"):
            st.session_state.show_add_paper_form = True

        if st.session_state.get('show_add_paper_form', False):
            with st.form("Add Paper"):
                project_name = st.text_input("Project Name")
                title = st.text_input("Title")
                authors = st.multiselect("Authors", authors_df["Name"].tolist())
                start_date = st.date_input("Start Date")
                end_date = st.date_input("End Date")
                required_skillsets = st.multiselect("Required Skillsets", ["Machine Learning", "Data Science", "Environmental Health"])
                deadline = st.date_input("Deadline")
                priority = st.number_input("Priority", min_value=1, max_value=5)
                status = st.selectbox("Status", ["Not Started", "In Progress", "Completed", "Submitted"])
                next_steps = st.text_area("Next Steps")
                current_issues = st.text_area("Current Issues")
                notes = st.text_area("Notes")
                submission_venue = st.text_input("Submission Venue")
                submission_status = st.selectbox("Submission Status", ["Not Submitted", "Submitted"])
                submit_paper = st.form_submit_button("Add Paper")

                if submit_paper:
                    new_paper = {
                        "ID": len(papers_df) + 1,
                        "Selected": False,
                        "Project Name": project_name,
                        "Title": title,
                        "Author1": authors[0] if len(authors) > 0 else "",
                        "Author2": authors[1] if len(authors) > 1 else "",
                        "Author3": authors[2] if len(authors) > 2 else "",
                        "Author4": authors[3] if len(authors) > 3 else "",
                        "Author5": authors[4] if len(authors) > 4 else "",
                        "Author6": authors[5] if len(authors) > 5 else "",
                        "Author7": authors[6] if len(authors) > 6 else "",
                        "Author8": authors[7] if len(authors) > 7 else "",
                        "Author9": authors[8] if len(authors) > 8 else "",
                        "Author10": authors[9] if len(authors) > 9 else "",
                        "Start Date": start_date.strftime("%Y-%m-%d"),
                        "End Date": end_date.strftime("%Y-%m-%d"),
                        "Required Skillsets": ", ".join(required_skillsets),
                        "Deadline": deadline.strftime("%Y-%m-%d"),
                        "Priority": priority,
                        "Status": status,
                        "Next Steps": next_steps,
                        "Current Issues": current_issues,
                        "Notes": notes,
                        "Submission Venue": submission_venue,
                        "Submission Status": submission_status
                    }
                    papers_df = papers_df.append(new_paper, ignore_index=True)
                    update_paper_ids()
                    save_data(authors_df, papers_df)
                    st.session_state.show_add_paper_form = False
                    st.success(f"Paper '{title}' added successfully!")
                    update_author_projects()

    if menu == "Authors":
        st.title("Authors")

        # Define grid options
        gb = GridOptionsBuilder.from_dataframe(authors_df)
        gb.configure_default_column(editable=st.session_state['user_role'] == 'Editor')
        gb.configure_column("Projects", editable=st.session_state['user_role'] == 'Editor', cellEditor='agSelectCellEditor', cellEditorParams={'values': papers_df["Project Name"].unique().tolist(), 'multiple': True})
        grid_options = gb.build()

        # Display the table
        response = AgGrid(
            authors_df.reset_index(drop=True),  # Remove the default index
            gridOptions=grid_options,
            update_mode='MODEL_CHANGED',
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
            allow_unsafe_jscode=True,
            enable_enterprise_modules=True,
        )

        # Save changes
        updated_df = response['data'].copy()  # Create a copy to avoid modifying the original DataFrame
        updated_df.reset_index(drop=True, inplace=True)  # Remove the default index
        if st.session_state['user_role'] == 'Editor' and st.button("Save Changes"):
            authors_df = pd.DataFrame(updated_df)
            save_data(authors_df, papers_df)
            st.success("Changes saved successfully!")

        # Button to add new author
        if st.session_state['user_role'] == 'Editor' and st.button("Add Author"):
            st.session_state.show_add_author_form = True

        if st.session_state.get('show_add_author_form', False):
            with st.form("Add Author"):
                name = st.text_input("Name")
                skillset = st.multiselect("Skillset", ["Machine Learning", "Data Science", "Environmental Health"])
                projects = st.multiselect("Projects", papers_df["Project Name"].unique().tolist())
                notes = st.text_area("Notes")
                submit_author = st.form_submit_button("Add Author")

                if submit_author:
                    new_author = {"Name": name, "Skillset": ", ".join(skillset), "Projects": ", ".join(projects), "Notes": notes}
                    authors_df = authors_df.append(new_author, ignore_index=True)
                    save_data(authors_df, papers_df)
                    st.session_state.show_add_author_form = False
                    st.success(f"Author {name} added successfully!")

    if menu == "Authors by Selection":
        st.title("Papers by Author")
        selected_authors = st.multiselect("Select Author(s) to View Papers", authors_df["Name"].tolist(), key="view_papers")
        if selected_authors:
            for author_name in selected_authors:
                st.write(f"Papers for {author_name}:")
                author_papers = papers_df[papers_df[[f"Author{i}" for i in range(1, 11)]].apply(lambda row: author_name in row.values, axis=1)].reset_index(drop=True)
                st.table(author_papers.drop(columns=["Selected"]))


# import streamlit as st
# import pandas as pd
# from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode

# # Sample data
# authors_data = {
#     "Name": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"],
#     "Skillset": ["Machine Learning, Data Science", "Environmental Health, Data Science", "Bioinformatics, Genomics", "Healthcare, AI"],
#     "Projects": ["Project A, Project B", "Project B", "", ""],
#     "Notes": ["", "", "", ""]
# }

# papers_data = {
#     "ID": [1, 2],
#     "Selected": [False, False],
#     "Project Name": ["Project A", "Project B"],
#     "Title": ["Title A", "Title B"],
#     "Author1": ["John Doe", "John Doe"],
#     "Author2": ["", "Jane Smith"],
#     "Author3": ["", ""],
#     "Author4": ["", ""],
#     "Author5": ["", ""],
#     "Author6": ["", ""],
#     "Author7": ["", ""],
#     "Author8": ["", ""],
#     "Author9": ["", ""],
#     "Author10": ["", ""],
#     "Start Date": ["2024-01-01", "2024-02-01"],
#     "End Date": ["2024-12-31", "2024-11-30"],
#     "Required Skillsets": ["Machine Learning", "Data Science"],
#     "Deadline": ["2024-12-31", "2024-11-30"],
#     "Priority": [1, 2],
#     "Status": ["In Progress", "Submitted"],
#     "Next Steps": ["Complete data analysis", "Review comments"],
#     "Current Issues": ["Data inconsistency", "None"],
#     "Notes": ["Initial draft", "Review pending"],
#     "Submission Venue": ["PLOS Journal", "IEEE"],
#     "Submission Status": ["Not Submitted", "Submitted"]
# }

# authors_df = pd.DataFrame(authors_data)
# papers_df = pd.DataFrame(papers_data)

# # Function to update paper IDs
# def update_paper_ids():
#     papers_df["ID"] = range(1, len(papers_df) + 1)

# update_paper_ids()

# # Function to update author projects
# def update_author_projects():
#     for idx, row in authors_df.iterrows():
#         projects = []
#         for i in range(1, 11):
#             projects += papers_df[papers_df[f"Author{i}"] == row["Name"]]["Project Name"].tolist()
#         authors_df.at[idx, "Projects"] = ", ".join(projects)

# update_author_projects()

# # Streamlit app
# st.sidebar.title("Research Management")

# # Sidebar navigation
# menu = st.sidebar.radio("Go to", ["Papers", "Authors", "Authors by Selection"])

# # Helper function to save updated DataFrame to session state
# def save_df_to_session_state(df, key):
#     st.session_state[key] = df

# # Load dataframes from session state if available
# if "authors_df" in st.session_state:
#     authors_df = st.session_state["authors_df"]

# if "papers_df" in st.session_state:
#     papers_df = st.session_state["papers_df"]

# # Helper function to get author profile
# def get_author_profile(name):
#     author_data = authors_df[authors_df["Name"] == name].iloc[0]
#     return f"Name: {author_data['Name']}\nSkillset: {author_data['Skillset']}\nProjects: {author_data['Projects']}\nNotes: {author_data['Notes']}"

# if menu == "Papers":
#     st.title("Papers")
    
#     # Define grid options
#     gb = GridOptionsBuilder.from_dataframe(papers_df)
#     gb.configure_default_column(editable=True)
#     gb.configure_column("Status", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={'values': ["Not Started", "In Progress", "Completed", "Submitted"]})
#     gb.configure_column("Submission Status", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={'values': ["Not Submitted", "Submitted"]})
#     for i in range(1, 11):
#         gb.configure_column(f"Author{i}", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={'values': authors_df["Name"].tolist()})
#     gb.configure_column("Selected", editable=True, cellEditor='agCheckboxCellEditor')
#     grid_options = gb.build()

#     # Auto-size all columns
#     grid_options['defaultColDef']['resizable'] = True
#     grid_options['defaultColDef']['autoHeight'] = True

#     # Display the table
#     response = AgGrid(
#         papers_df.reset_index(drop=True),  # Remove the default index
#         gridOptions=grid_options,
#         update_mode='MODEL_CHANGED',
#         columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
#         allow_unsafe_jscode=True,
#         enable_enterprise_modules=True,
#     )

#     # Save changes
#     updated_df = response['data'].copy()  # Create a copy to avoid modifying the original DataFrame
#     updated_df.reset_index(drop=True, inplace=True)  # Remove the default index
#     if st.button("Save Changes"):
#         papers_df = pd.DataFrame(updated_df)
#         update_paper_ids()
#         save_df_to_session_state(papers_df, "papers_df")
#         st.success("Changes saved successfully!")

#     # Show only selected papers
#     selected_papers = papers_df[papers_df["Selected"]].reset_index(drop=True)
#     if not selected_papers.empty:
#         st.subheader("Selected Papers")
#         st.table(selected_papers.drop(columns=["Selected"]))

#     # Button to add new paper
#     if st.button("Add Paper"):
#         st.session_state.show_add_paper_form = True

#     if st.session_state.get('show_add_paper_form', False):
#         with st.form("Add Paper"):
#             project_name = st.text_input("Project Name")
#             title = st.text_input("Title")
#             authors = st.multiselect("Authors", authors_df["Name"].tolist())
#             start_date = st.date_input("Start Date")
#             end_date = st.date_input("End Date")
#             required_skillsets = st.multiselect("Required Skillsets", ["Machine Learning", "Data Science", "Environmental Health"])
#             deadline = st.date_input("Deadline")
#             priority = st.number_input("Priority", min_value=1, max_value=5)
#             status = st.selectbox("Status", ["Not Started", "In Progress", "Completed", "Submitted"])
#             next_steps = st.text_area("Next Steps")
#             current_issues = st.text_area("Current Issues")
#             notes = st.text_area("Notes")
#             submission_venue = st.text_input("Submission Venue")
#             submission_status = st.selectbox("Submission Status", ["Not Submitted", "Submitted"])
#             submit_paper = st.form_submit_button("Add Paper")

#             if submit_paper:
#                 new_paper = {
#                     "ID": len(papers_df) + 1,
#                     "Selected": False,
#                     "Project Name": project_name,
#                     "Title": title,
#                     "Author1": authors[0] if len(authors) > 0 else "",
#                     "Author2": authors[1] if len(authors) > 1 else "",
#                     "Author3": authors[2] if len(authors) > 2 else "",
#                     "Author4": authors[3] if len(authors) > 3 else "",
#                     "Author5": authors[4] if len(authors) > 4 else "",
#                     "Author6": authors[5] if len(authors) > 5 else "",
#                     "Author7": authors[6] if len(authors) > 6 else "",
#                     "Author8": authors[7] if len(authors) > 7 else "",
#                     "Author9": authors[8] if len(authors) > 8 else "",
#                     "Author10": authors[9] if len(authors) > 9 else "",
#                     "Start Date": start_date.strftime("%Y-%m-%d"),
#                     "End Date": end_date.strftime("%Y-%m-%d"),
#                     "Required Skillsets": ", ".join(required_skillsets),
#                     "Deadline": deadline.strftime("%Y-%m-%d"),
#                     "Priority": priority,
#                     "Status": status,
#                     "Next Steps": next_steps,
#                     "Current Issues": current_issues,
#                     "Notes": notes,
#                     "Submission Venue": submission_venue,
#                     "Submission Status": submission_status
#                 }
#                 papers_df = papers_df.append(new_paper, ignore_index=True)
#                 update_paper_ids()
#                 save_df_to_session_state(papers_df, "papers_df")
#                 st.session_state.show_add_paper_form = False
#                 st.success(f"Paper '{title}' added successfully!")
#                 update_author_projects()
#                 save_df_to_session_state(authors_df, "authors_df")

# if menu == "Authors":
#     st.title("Authors")
    
#     # Define grid options
#     gb = GridOptionsBuilder.from_dataframe(authors_df)
#     gb.configure_default_column(editable=True)
#     gb.configure_column("Projects", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={'values': papers_df["Project Name"].unique().tolist(), 'multiple': True})
#     grid_options = gb.build()

#     # Display the table
#     response = AgGrid(
#         authors_df.reset_index(drop=True),  # Remove the default index
#         gridOptions=grid_options,
#         update_mode='MODEL_CHANGED',
#         columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
#         allow_unsafe_jscode=True,
#         enable_enterprise_modules=True,
#     )

#     # Save changes
#     updated_df = response['data'].copy()  # Create a copy to avoid modifying the original DataFrame
#     updated_df.reset_index(drop=True, inplace=True)  # Remove the default index
#     if st.button("Save Changes"):
#         authors_df = pd.DataFrame(updated_df)
#         save_df_to_session_state(authors_df, "authors_df")
#         st.success("Changes saved successfully!")

#     # Button to add new author
#     if st.button("Add Author"):
#         st.session_state.show_add_author_form = True

#     if st.session_state.get('show_add_author_form', False):
#         with st.form("Add Author"):
#             name = st.text_input("Name")
#             skillset = st.multiselect("Skillset", ["Machine Learning", "Data Science", "Environmental Health"])
#             projects = st.multiselect("Projects", papers_df["Project Name"].unique().tolist())
#             notes = st.text_area("Notes")
#             submit_author = st.form_submit_button("Add Author")

#             if submit_author:
#                 new_author = {"Name": name, "Skillset": ", ".join(skillset), "Projects": ", ".join(projects), "Notes": notes}
#                 authors_df = authors_df.append(new_author, ignore_index=True)
#                 save_df_to_session_state(authors_df, "authors_df")
#                 st.session_state.show_add_author_form = False
#                 st.success(f"Author {name} added successfully!")

# if menu == "Authors by Selection":
#     st.title("Papers by Author")
#     selected_authors = st.multiselect("Select Author(s) to View Papers", authors_df["Name"].tolist(), key="view_papers")
#     if selected_authors:
#         for author_name in selected_authors:
#             st.write(f"Papers for {author_name}:")
#             author_papers = papers_df[papers_df[[f"Author{i}" for i in range(1, 11)]].apply(lambda row: author_name in row.values, axis=1)].reset_index(drop=True)
#             st.table(author_papers.drop(columns=["Selected"]))
