import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

params = st.experimental_get_query_params()

user_id = params.get('request_token', [None])[0]

if user_id:
    st.write(f"Request Token: {user_id}")
else:
    st.write("User ID is not provided in the URL.")
