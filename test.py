import os
import urllib
from pprint import pprint
import urllib.parse

import requests
from dotenv import load_dotenv

API_HOST = 'https://cloud-api.yandex.net/'
API_VERSION = 'v1'
DISK_INFO_URL = f'{API_HOST}{API_VERSION}/disk/'
REQUEST_UPLOAD_URL = f'{API_HOST}{API_VERSION}/disk/resources/upload'
DOWNLOAD_LINK_URL = f'{API_HOST}{API_VERSION}/disk/resources/download'


load_dotenv()
DISK_TOKEN = os.environ.get('DISK_TOKEN')


AUTH_HEADERS = {
    'Authorization': f'OAuth {DISK_TOKEN}'
}

# payload = {
#     'path': 'app:/filename.txt',
#     'overwrite': 'True'
# }


# # response = requests.get(url=DISK_INFO_URL, headers=AUTH_HEADERS)

# response_upload = requests.get(
#     headers=AUTH_HEADERS,
#     params=payload,
#     url=REQUEST_UPLOAD_URL
# )
# upload_url = response_upload.json()['href']


# with open('filename.txt', 'rb') as file:
#     response = requests.put(
#         data=file,
#         url=upload_url
#     )
# location = response.headers['Location']
# location = urllib.parse.unquote(location)

# location = location.replace('/disk', '')
# print(location)


response = requests.get(
    headers=AUTH_HEADERS,
    url=DOWNLOAD_LINK_URL, 
    params={'path': '/Приложения/Uploader/filename.txt'}
)

link = response.json()['href']
print(link)
