import streamlit as st
import hashlib
api_key = '9bjokluovk546xbx'
api_secret = "38iqdsm18i7oklyppfdagmkg2jqnqg5f"

st.title("🎈 My new app")
st.write(
    "LOGIN HERE @ [KITE CONNECT](https://kite.zerodha.com/connect/login?v=3&api_key=9bjokluovk546xbx)."
)

params = st.experimental_get_query_params()

user_id = params.get('request_token', [None])[0]

if user_id:
    st.write(f"Request Token: {user_id}")
    checksum = hashlib.sha256() 
    checksum.update((api_key+api_secret+user_id).encode('utf-8'))
    st.write(checksum.hexdigest())
else:
    st.write("User ID is not provided in the URL.")
