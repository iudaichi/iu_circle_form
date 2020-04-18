import os
import requests
import json
from typing import Dict
from service.firebase_session import firebase_app
from service.firestore_session import db
from firebase_admin import auth


class FireBase:
    def __init__(self,):
        with open('./config/config.json') as f:
            self.config_date = json.load(f)
        self.api_key = os.environ['API_KEY']

    def get_id_token(self, custom_token: str) -> Dict[str, str]:
        try:
            response = requests.post(f"{self.config_date['verifyCustomTokenUrl']}{self.api_key}",
                                     {"token": custom_token, "returnSecureToken": "true"})
            return_date = response.json()
            return return_date
        except Exception as e:
            return e

    def sign_in_with_email_and_password(self,
                                        email: str,
                                        password: str) -> Dict[str, str]:
        uri = f"{self.config_date['verifyPasswordUrl']}{self.api_key}"
        headers = {"Content-type": "application/json"}
        data = json.dumps({"email": email, "password": password,
                           "returnSecureToken": True})
        result = requests.post(url=uri, headers=headers, data=data,)
        return result.json

    def verify_session_cookie(self, session_cookie: str) -> Dict[str, str]:
        try:
            result = auth.verify_session_cookie(
                session_cookie, check_revoked=True, app=firebase_app)
            return result
        except Exception as error:
            return error

    def add_data_to_db(self, collection_name: str, document_name: str, contents: dict):
        doc_ref = db.collection(collection_name).document(document_name)
        doc_ref.set(contents)
