import requests

# Your Sketchfab API token
token = ''

# Filepath to the model you want to upload
model_filepath = 'MPU6050Gyro-sensor.gltf'

# URL for the Sketchfab model upload API
upload_url = 'https://api.sketchfab.com/v3/models'

# Request headers
headers = {
    'Authorization': f'Token {token}',
}

# Request body
data = {
    'modelFile': open(model_filepath, 'rb'),
}

# Make the POST request to upload the model
response = requests.post(upload_url, headers=headers, files=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the UID of the uploaded model from the response JSON
    model_data = response.json()
    uid = model_data['uid']
    print(f"Model uploaded successfully. UID: {uid}")
else:
    print(f"Failed to upload model. Status code: {response.status_code}")
    print(response.text)
