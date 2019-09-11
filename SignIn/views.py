from django.shortcuts import render
import pyrebase
from django.contrib import auth
from django.contrib import auth
config = {
    'apiKey': "AIzaSyBele0wVjlZvLPj2eYz1TnUITSP6iKnpOk",
    'authDomain': "chatbot-9a662.firebaseapp.com",
    'databaseURL': "https://chatbot-9a662.firebaseio.com",
    'projectId': "chatbot-9a662",
    'storageBucket': "chatbot-9a662.appspot.com",
    'messagingSenderId': "657579802000",
    'appId': "1:657579802000:web:c3b53e0b79ef5b5eae8715"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    import time
    from datetime import datetime, timezone
    import pytz
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    
    Name = request.POST.get('Name')
    Name1 = request.POST.get('Name1')
    Number = int(request.POST.get('Number'))
    Mail = request.POST.get('mail')
    city = request.POST.get('city')

    Name = Name.lower()
    Name1 = Name1.lower()   
    data = {
        "City" : city,
        "First Name" : Name,
        "Last Name":Name1,
        "Number":Number,
        "Mail":Mail
    }
    Name = str(Name)
    Name1 = str(Name1)
    Name2 = Name + " " + Name1
    database.child(Name2).set(data)
    #name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request,'home3.html')

def download(request):
    username = "sonijay1910@gmail.com"
    password = "Jay19101207"
    user = auth.sign_in_with_email_and_password(username, password)
    user = auth.refresh(user['refreshToken'])
    db = firebase.database()
    values = db.get()
    import pandas as pd
    data = pd.DataFrame(values.val())
    data.to_excel('sm1.xlsx')
    return render(request,'home3.html')
