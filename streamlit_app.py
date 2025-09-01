import streamlit as st
import hashlib
import requests
api_key = '9bjokluovk546xbx'
api_secret = "38iqdsm18i7oklyppfdagmkg2jqnqg5f"

st.title("🎈 My new app")
st.write(
    "LOGIN HERE @ [KITE CONNECT](https://kite.zerodha.com/connect/login?v=3&api_key=9bjokluovk546xbx)."
)

params = st.experimental_get_query_params()

request_token = params.get('request_token', [None])[0]

if request_token:
    st.write(f"Request Token: {request_token}")
    checksum = hashlib.sha256() 
    checksum.update((api_key+api_secret+request_token).encode('utf-8'))
    st.write(checksum.hexdigest())
else:
    st.write("User ID is not provided in the URL.")



url = "https://api.kite.trade/session/token"


data = {
    "api_key": api_key,
    "request_token": request_token,
    "checksum": checksum.hexdigest()
}

# Set the headers
headers = {
    "X-Kite-Version": "3"
}

# Send the POST request
response = requests.post(url, data=data, headers=headers)

# Print the response (the access token)
if response.status_code == 200:
    json_data = response.json()
    access_token = json_data['data']['access_token']
    st.write(access_token)
else:
    print("Error:", response.text)