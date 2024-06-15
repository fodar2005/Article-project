import streamlit as st

# Set the title of the app
st.title("User Information Form")

# Input fields for user information
age = st.number_input("Age", min_value=0, max_value=120, step=1)
education_level = st.selectbox(
    "Level of Education",
    ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Ph.D.", "Other"]
)
job = st.text_input("Job")
interests = st.text_area("Interests (comma-separated)")

# Select level of professionalism for the rewritten article
professionalism_level = st.select_slider(
    "Level of Professionalism Wanted in Rewritten Article",
    options=["Casual", "Semi-formal", "Formal"]
)

# Button to submit the form
if st.button("Submit"):
    # Display the input information
    st.write("### Submitted Information")
    st.write(f"**Age:** {age}")
    st.write(f"**Level of Education:** {education_level}")
    st.write(f"**Job:** {job}")
    st.write(f"**Interests:** {interests}")
    st.write(f"**Level of Professionalism:** {professionalism_level}")

# Run the app
if __name__ == "__main__":
    st._is_running_with_streamlit = True
    from streamlit.cli import main
    main()
