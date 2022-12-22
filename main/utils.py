import requests
from dataclasses import dataclass
import os
import json
from os.path import join
from dotenv import load_dotenv
from TranslateBackens.settings import BASE_DIR
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)



@dataclass
class Translate:
    url: str
    sourceLanguageCode: str
    targetLanguageCode: str
    texts: str or None
    headers: dict
    folderID: str

def RefreshToken(refresh_url: str, access_token: str)-> dict:
    data = {

    "yandexPassportOauthToken": "{}".format(access_token)

            }
    try:
        response = requests.post(refresh_url, json=data)

        if response.status_code == 200:
            return response.text
        else:
            return {'error': 'Not data'}

    except Exception as e:
        return e

def post(translated_data: Translate) -> str:

    datas = {
        'sourceLanguageCode': translated_data.sourceLanguageCode,
        'targetLanguageCode': translated_data.targetLanguageCode,
        'texts': translated_data.texts,
        'folderId': translated_data.folderID
    }


    try:
        response = requests.post(translated_data.url, json=datas, headers=translated_data.headers)
        if response.status_code == 401:
            data = RefreshToken(os.environ.get('TOKEN_REFRESH_URL'), os.environ.get('ACCESS_TOKEN'))
            json_convert = json.loads(data)
            headers = {'Authorization': 'Bearer {}'.format(json_convert['iamToken'])}
            response = requests.post(translated_data.url, json=datas, headers=headers)
    except Exception as e:
        return e
    data = json.loads(response.text)
    try:
        data['translations'][0]['text']
    except:
        return False

    return data['translations'][0]['text']

















