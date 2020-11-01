from  flask import Flask, render_template, request
import os

app = Flask(__name__)
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'relay1':
            os.system('./relay1.sh')
        if deviceName == 'relay2':
            os.system('./relay2.sh')
        if deviceName == 'relay3':
            os.system('./relay3.sh')
        if deviceName == 'relay4':
            os.system('./relay4.sh')
        if deviceName == 'relay5':
            os.system('./relay5.sh')
        if deviceName == 'relay6':
            os.system('./relay6.sh')
        if deviceName == 'relay7':
            os.system('./relay7.sh')
        if deviceName == 'relay8':
            os.system('./relay8.sh')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
