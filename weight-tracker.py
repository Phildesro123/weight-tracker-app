import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Initialize session state for tracking
if "tracker" not in st.session_state:
    start_date = datetime.today()
    weeks = [start_date + timedelta(weeks=i) for i in range(26)]
    st.session_state["tracker"] = pd.DataFrame({
        "Week Ending": [date.strftime("%Y-%m-%d") for date in weeks],
        "Weight (lbs)": ["" for _ in weeks],
        "Workout Completed (Yes/No)": ["" for _ in weeks],
        "Notes": ["" for _ in weeks],
    })

# Title
st.title("6-Month Weight Loss Progress Tracker")

# Show and Edit Tracker
st.write("### Update your progress:")
edited_tracker = st.data_editor(st.session_state["tracker"], num_rows="dynamic")

# Save Progress Button
if st.button("Save Progress"):
    st.session_state["tracker"] = edited_tracker
    st.success("Progress saved successfully!")

# Display Tracker
st.write("### Current Progress:")
st.dataframe(st.session_state["tracker"])

# Option to Download Tracker
csv = st.session_state["tracker"].to_csv(index=False)
st.download_button(label="Download CSV", data=csv, file_name="weight_tracker.csv", mime="text/csv")