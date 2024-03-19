import requests
from datetime import datetime

USERNAME="guramritpandher"
TOKEN="der4rjf4nuh434r"
GRAPH_ID="graph1"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"h",
    "type":"int",
    "color":"ajisai",
}

headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime(year=2024,month=3,day=2)
pixel_data={
    "date":today.strftime('%Y%m%d'),
    "quantity":"4"
}
# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"2"
}
response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)