import streamlit as st
from send_email import send_email

st.title("Contact Me")

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if st.session_state.form_submitted:
    st.session_state.form_submitted = False


with st.form(key='email_forms', clear_on_submit=True):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message") #for multi line text
    raw_message = f"Subject: Email from portfolio\n\nFrom: {email}\n{message}"
    submit_button = st.form_submit_button("Submit") #special button that acts as boolean.
    if submit_button:
        send_email(raw_message)
        st.info("Your message has been sent")
        st.session_state.form_submitted = True
