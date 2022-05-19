import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def get_href(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = { 'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json()) # получили ссылку на загрузку
        return response.json()
    def upload(self, file_path):
        href = self.get_href(file_path=file_path).get('href', '')
        response = requests.put(href, open('hello yandex.txt', 'rb'))

if __name__ == '__main__':
    path_to_file = 'hello yandex.txt' # адрес указал не явно
    token = '' # переменную для токена нужно оставить пустой
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
