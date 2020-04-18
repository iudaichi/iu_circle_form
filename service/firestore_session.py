from service.firebase_session import firebase_app
from firebase_admin import firestore

app = firebase_app
db = firestore.client()
