import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

firebaseConfig = {
  'apiKey': "AIzaSyA_CcN61WKNw7VKSangr7HKVBOst18exTE",
  'authDomain': "habittracker-e93e9.firebaseapp.com",
  'projectId': "habittracker-e93e9",
  'storageBucket': "habittracker-e93e9.appspot.com",
  'messagingSenderId': "241841178874",
  'appId': "1:241841178874:web:3f99011101a938267de143",
  'databaseURL': ""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class Auth:
    def __init__(self):
        super(Auth, self).__init__()
    def createAcc(email,pwd,cpwd,name):
        if pwd==cpwd:
            try:
                user = auth.create_user_with_email_and_password(email,pwd)
                db.collection('Users').document(user['localId']).set({'name': name})
                print("Account Created" , user)
                return True
            except Exception as e:
                print(e)
                return False
        else: 
            return False

    
    def login(email,pwd):

        try:
            user = auth.sign_in_with_email_and_password(email,pwd)
            print(user)
            print("Login Successful")
            return [True, db.collection('Users').document(user['localId']).get().to_dict()['name']]

        except Exception as e:
            print(e)
            return [False]
