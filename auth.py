import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

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
            return [True, db.collection('Users').document(user['localId']).get().to_dict()['name'],user['localId']]

        except Exception as e:
            print(e)
            return [False]

    def pushInfo(task_name,description,tf,uid):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        db.collection('Users').document(uid).collection('Tasks').add({'task_name':task_name,'description': description,'time':current_time,'productive':tf})
        li =[]
        result = db.collection('Users').document(uid).collection('Tasks').get()
        for doc in result:
            li.append(doc.to_dict())
        print (li)
        return li
    def pullInfo(uid):
        li =[]
        result = db.collection('Users').document(uid).collection('Tasks').get()
        for doc in result:
            li.append(doc.to_dict())
        return li