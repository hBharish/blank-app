import streamlit as st
import hashlib
import requests

# API credentials (replace with your actual credentials or use environment variables)
api_key = '9bjokluovk546xbx' 
api_secret = "38iqdsm18i7oklyppfdagmkg2jqnqg5f"

# Streamlit UI
st.title("🎈 My Kite Connect App")
st.write(
    "Login here @ [Kite Connect](https://kite.zerodha.com/connect/login?v=3&api_key=9bjokluovk546xbx)." 
)

# Extract the request_token from the URL query parameters
params = st.experimental_get_query_params()
request_token = params.get('request_token', [None])[0]

if request_token:
    # Display the request token
    st.write(f"Request Token: {request_token}")
    
    # Generate checksum (SHA-256 of api_key + request_token + api_secret)
    checksum = hashlib.sha256()
    checksum.update(f"{api_key}{request_token}{api_secret}".encode('utf-8'))
    checksum = checksum.hexdigest()
    
    st.write(f"Checksum: {checksum}")
else:
    st.write("Request Token is not provided in the URL. Please login first.")

# Define the URL for getting the access token
url = "https://api.kite.trade/session/token"

# If request_token is valid, send the request to get the access token
if request_token:
    data = {
        "api_key": api_key,
        "request_token": request_token,
        "checksum": checksum
    }

    # Set the headers for the request
    headers = {
        "X-Kite-Version": "3"
    }

    try:
        # Send the POST request to get the access token
        response = requests.post(url, data=data, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            json_data = response.json()
            if 'data' in json_data and 'access_token' in json_data['data']:
                access_token = json_data['data']['access_token']
                st.success("Access token received successfully!")
                st.write("Access Token:", access_token)
            else:
                st.error("Failed to retrieve access token. Please check your request token.")
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        # Handle network or request errors
        st.error(f"Request failed: {e}")
