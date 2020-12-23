#!python3

from flask import Flask, render_template, request
from cryptography.fernet import Fernet
en_text = ''
app = Flask(__name__)

class DataStore():
    en_text = ''
    

data = DataStore()

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST' and 'link' in request.form:
        link = str(request.form.get('link'))
        
        data.en_text = encrypt(link)
        import pyperclip
        pyperclip.copy(data.en_text)
        
    return render_template("encrypt.html",
	                        en_text=data.en_text)





def encrypt(message):
    key = 'PG1JIvKftPEQC7EcqBSrRoRYMoLCbWpcTTcFGrZNDXY='.encode()
    encryption_type = Fernet(key)
    encrypted_message = encryption_type.encrypt(message.encode())

    return encrypted_message.decode()

if __name__ == '__main__':
    app.run()