# data_store.py

authors_data = [
    {"Name": "Karim Keshavjee", "Skillset": "Machine Learning, Data Science", "Projects": "Ping-pong paddle, Nomogram", "Notes": ""},
    {"Name": "Aziz Guergachi", "Skillset": "Environmental Health, Data Science", "Projects": "Ping-pong paddle", "Notes": ""},
    {"Name": "Alessia Paglialonga", "Skillset": "Bioinformatics, Genomics", "Projects": "", "Notes": ""},
    {"Name": "Yacine Marouf", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Alireza Khatami", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Marta Lenatti", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Swetha Chakravarthy", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Dora Mugambi", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Pooyeh Graili", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},
    {"Name": "Mohammad Noaeen", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""},

]

papers_data = [
    {"ID": 1, "Selected": False, "Project Name": "CNN Pooling Layers", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 2, "Selected": False, "Project Name": "Quadratic function", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 3, "Selected": False, "Project Name": "Prescriptive analytics (CanPath)", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 4, "Selected": False, "Project Name": "Diabetes complications", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 5, "Selected": False, "Project Name": "Diabetes complications --Swetha", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 6, "Selected": False, "Project Name": "Time to Diabetes", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 7, "Selected": False, "Project Name": "Nutrition", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 8, "Selected": False, "Project Name": "Education", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 9, "Selected": False, "Project Name": "Ping-pong paddle", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 10, "Selected": False, "Project Name": "Nomogram", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 11, "Selected": False, "Project Name": "Apps 4 All", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 12, "Selected": False, "Project Name": "Simulation modeling for health system transformation", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 13, "Selected": False, "Project Name": "App Development", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 14, "Selected": False, "Project Name": "Architecture for AI driven behavior change", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 15, "Selected": False, "Project Name": "Mathematical model for AI driven behaviour change", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 16, "Selected": False, "Project Name": "Marking prescriptions using LLM and graphical DBs vs text parsing", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    {"ID": 17, "Selected": False, "Project Name": "Next Generation EMR", "Title": "Title A", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
    {"ID": 18, "Selected": False, "Project Name": "Basic building blocks of health system transformation", "Title": "Title B", "Author1": "Karim Keshavjee", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"},
    
]


# authors_data = [
#     {"Name": "John Doe", "Skillset": "Machine Learning, Data Science", "Projects": "Project A, Project B", "Notes": ""},
#     {"Name": "Jane Smith", "Skillset": "Environmental Health, Data Science", "Projects": "Project B", "Notes": ""},
#     {"Name": "Alice Johnson", "Skillset": "Bioinformatics, Genomics", "Projects": "", "Notes": ""},
#     {"Name": "Bob Brown", "Skillset": "Healthcare, AI", "Projects": "", "Notes": ""}
# ]

# papers_data = [
#     {"ID": 1, "Selected": False, "Project Name": "Project A", "Title": "Title A", "Author1": "John Doe", "Author2": "", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-01-01", "End Date": "2024-12-31", "Required Skillsets": "Machine Learning", "Deadline": "2024-12-31", "Priority": 1, "Status": "In Progress", "Next Steps": "Complete data analysis", "Current Issues": "Data inconsistency", "Notes": "Initial draft", "Submission Venue": "PLOS Journal", "Submission Status": "Not Submitted"},
#     {"ID": 2, "Selected": False, "Project Name": "Project B", "Title": "Title B", "Author1": "John Doe", "Author2": "Jane Smith", "Author3": "", "Author4": "", "Author5": "", "Author6": "", "Author7": "", "Author8": "", "Author9": "", "Author10": "", "Start Date": "2024-02-01", "End Date": "2024-11-30", "Required Skillsets": "Data Science", "Deadline": "2024-11-30", "Priority": 2, "Status": "Submitted", "Next Steps": "Review comments", "Current Issues": "None", "Notes": "Review pending", "Submission Venue": "IEEE", "Submission Status": "Submitted"}
# ]




















