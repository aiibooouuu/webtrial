from website import create_app
# import pyrebase
# firebaseConfig = {
#   'apiKey': "AIzaSyBf9wPzmnhFV_MLIbr74zFxTsGEcfhruoM",
#   'authDomain': "webtrial-987ed.firebaseapp.com",
#   'projectId': "webtrial-987ed",
#   'storageBucket': "webtrial-987ed.appspot.com",
#   'messagingSenderId': "187446131873",
#   'appId': "1:187446131873:web:02b05376568630629f04e0",
#   'measurementId': "G-RTF7B1ZR33",
#   "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

# Hello