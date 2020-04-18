import firebase_admin
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./config/service-account-file.json"
firebase_app = firebase_admin.initialize_app()
