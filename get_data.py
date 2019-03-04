import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

def connect_to_db():
  # Use a service account
  cred = credentials.Certificate('fbio-config.json')
  if not len(firebase_admin._apps):
    firebase_admin.initialize_app(cred)
  db = firestore.client()
  return db

def get_data(table, fields=[]):
  db = connect_to_db()
  docs = db.collection(table).get()
  result = []
  for doc in docs:
    result.append(doc.to_dict())
  return result
  
def get_data_mapped(table, fields=[], key='id'):
  data = get_data(table, fields)
  result = {}
  for d in data:
    result[d[key]] = d
  return result