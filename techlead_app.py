import streamlit as st
import pandas as pd

# Load data (ensure the files are in the same directory or provide correct paths)
teams_df = pd.read_csv("C:/Users/thati/OneDrive/Desktop/TL_GROUPING/developer_interns_with_ids.csv")

techleads_df = pd.read_csv("techleads_with_ids.csv")

# Shuffle interns and group them into groups of 5
teams_df = teams_df.sample(frac=1).reset_index(drop=True)
groups = [teams_df.iloc[i:i + 5] for i in range(0, len(teams_df), 5)]

# Shuffle tech leads
techleads_df = techleads_df.sample(frac=1).reset_index(drop=True)

# Assign 5 groups to each tech lead
techlead_assignments = {}
techlead_index = 0

total_groups = len(groups)
total_techleads = len(techleads_df)

for i, group in enumerate(groups):
    techlead_id = techleads_df.iloc[techlead_index % total_techleads]['tech_lead_id']
    techlead_name = techleads_df.iloc[techlead_index % total_techleads]['techlead_name']
    
    if techlead_name not in techlead_assignments:
        techlead_assignments[techlead_name] = []
    techlead_assignments[techlead_name].append(group)

    if len(techlead_assignments[techlead_name]) == 5:
        techlead_index += 1

# Streamlit App
st.title("Tech Lead Group Allocation")

input_name = st.text_input("Enter Tech Lead Name (e.g., some-name_college001):")

if input_name:
    if input_name in techlead_assignments:
        st.success(f"Groups assigned to {input_name}:")
        for idx, group in enumerate(techlead_assignments[input_name], 1):
            st.subheader(f"Group {idx}")
            st.table(group[['intern_id', 'developer_intern_name', 'college']])
    else:
        st.error("Tech Lead not found or no groups assigned.")
