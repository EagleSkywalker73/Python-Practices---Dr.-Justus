import streamlit as st
#create my Resume
from PIL import Image
col1, col2 = st.columns((4, 5))

with col1:
    st.title("Josh Delgado")
    st.header("Student in Computer Science")

with col2:
    image = Image.open("PAP4TACO.jpg")
    st.image(image, width=200)

st.balloons()
st.snow()

st.markdown("About Me")
st.text("I am learning Computer Science and IA at JBU")
st.divider()

st.markdown("Qualifications")
st.text("Public speaking and communication skills")
st.text("Leadership and teamwork skills")
st.text("I have a strong foundation in python and Neuroscience")
st.text("I have experience in web development and software engineering")
st.divider()

st.markdown("Work Experience")
st.text("I have worked as a data analyst in Caja de Ahorros Bank in Panama")
st.text("I have worked as an official Public Speaker for the Presidency of Panama.")
st.divider()


st.markdown("Awards and Achievements")
st.text("Top 60 best Public Speakers 2024-2025 - National Oratory Competition")
st.text("International articles writer for Almanaque Digital - Politics, Tech and Neuroscience")
st.divider()

st.markdown("Projects")
st.divider()

st.markdown("**Contact me:**")
username = st.text_input("Your Name:")
usermailID = st.text_input("Your Email:")
userMessage = st.text_area("Your Message:")
st.divider()





