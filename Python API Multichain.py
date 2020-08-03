
import requests
import json
import urllib.request
import getpass
import os
import ast
from flask import Flask, jsonify, request 
import subprocess


app = Flask(__name__)
app.config["DEBUG"] = True
chainname = ""
port=4447
host="127.0.0.1"

peeraddress1=""

from keyboard import press
import pickle
import time


@app.route('/createblockchain', methods=['POST'])
def createblockchain():
    n = request.args.get('chain')    
    item = subprocess.Popen([r"C:\Users\Fahad Sultan\Desktop\test.bat", str(n)] )
    press('enter')
    return "SUCCESS"
    




@app.route('/getpeeraddress',methods=['POST'])
def getpeeraddress():
    moizip="192.168.0.107"
    localchain = request.args.get('local')
    os.system("start cmd /k "+"cd /d E:\Multichain")
    os.chdir(r"E:\Multichain")
    addressOutput = os.popen("multichaind "+localchain+"@"+moizip+":6465").read()
    y = addressOutput.splitlines()
    print(y[4])
    return y[4];
    
@app.route('/grantPermission',methods=['POST'])
def grantPermission():
    commandId = request.args.get('ID')
    os.chdir(r"E:\Multichain")
    os.chdir(commandId)


@app.route('/CreateStream',methods=['POST'])
def CreateStream():
    chainname = request.args.get('chain')
    id = request.args.get('id')
    data  = request.args.get('data')
    data = str(data); 
    s = data.encode("utf-8").hex()
    os.chdir(r"E:\Multichain")
    os.system("multichain-cli "+chainname+" create stream medicine true")
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    os.system("multichain-cli "+chainname+" publish medicine "+id+" "+data)
    jsonString = os.popen("multichain-cli "+chainname+" liststreamkeyitems medicine "+id+" true 1").read()
    return jsonString

@app.route('/getSecondStream1',methods=['POST'])
def getSecondStream1():
    chainname = request.args.get('chain')
    id = request.args.get('id')
    cid = request.args.get('cid')    
    os.chdir(r"E:\Multichain")
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    jsonString = os.popen("multichain-cli "+chainname+" liststreamkeyitems medicine "+id+" true 1").read()
    print(jsonString);
    addressOutput = os.popen("multichain-cli "+chainname+" listpermissions medicine.*").read()
    print(addressOutput);
    parsed = json.loads(jsonString)
    data = str(parsed[0]["data"])
    hex_string = "0x"+data
    hex_string = hex_string[2:]
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    r =  eval(ascii_string)
    print(r)
    r["wid"] = cid
    print("SECOND ",r)
    x = str(r); 
    hexPushData = x.encode("utf-8").hex()
    print(hexPushData);
    
    time.sleep(3)
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    os.system("multichain-cli "+chainname+" publish medicine "+id+" "+hexPushData)
    return r

@app.route('/getSecondStream2',methods=['POST'])
def getSecondStream2():
    chainname = request.args.get('chain')
    id = request.args.get('id')
    cid = request.args.get('cid')
    os.chdir(r"E:\Multichain")
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    jsonString = os.popen("multichain-cli "+chainname+" liststreamkeyitems medicine "+id+" true 1").read()
    print(jsonString);
    addressOutput = os.popen("multichain-cli "+chainname+" listpermissions medicine.*").read()
    parsed = json.loads(jsonString)
    data = str(parsed[0]["data"])
    hex_string = "0x"+data
    hex_string = hex_string[2:]
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    r =  eval(ascii_string)
    print(r)
    r["rid"] = cid
    x = str(r); 
    hexPushData = x.encode("utf-8").hex()
    print(hexPushData);
    time.sleep(2)
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    os.system("multichain-cli "+chainname+" publish medicine "+id+" "+hexPushData)
    return r

@app.route('/getSecondStream3',methods=['POST'])
def getSecondStream3():
    chainname = request.args.get('chain')
    id = request.args.get('id')
    cid = request.args.get('cid')
    os.chdir(r"E:\Multichain")
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    jsonString = os.popen("multichain-cli "+chainname+" liststreamkeyitems medicine "+id+" true 1").read()
    print(jsonString);
    # addressOutput = os.popen("multichain-cli "+chainname+" listpermissions medicine.*").read()
    # print(addressOutput);
    parsed = json.loads(jsonString)
    data = str(parsed[0]["data"])
    hex_string = "0x"+data
    hex_string = hex_string[2:]
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    r =  eval(ascii_string)
    print(r)
    r["cid"] = cid
    x = str(r); 
    hexPushData = x.encode("utf-8").hex()
    print(hexPushData);
    time.sleep(3)
    os.system("multichain-cli "+chainname+" subscribe medicine true")
    os.system("multichain-cli "+chainname+" publish medicine "+id+" "+hexPushData)
    
    return r
   

@app.route('/PushSecondStream',methods=['POST'])
def PushSecondStream():
    chainname = request.args.get('chain')
    id = request.args.get('id')
    
    data  = request.args.get('data')
    
    data = str(data)
    hex_string = "0x"+data
    hex_string = hex_string[2:]

    bytes_object = bytes.fromhex(hex_string)


    ascii_string = bytes_object.decode("ASCII")

    print(ascii_string);
    r =  eval(ascii_string)

    print(r);
    r["wid"] = "test";

    print(r["wid"])
    return r
    

@app.route('/InitializeBlockchain', methods=['POST'])
def InitializeBlockchain():
    x = request.args.get('chain')
    item = subprocess.Popen([r"C:\Users\Fahad Sultan\Desktop\test.bat", str(x)] )
    press('enter')
    return "SUCCESS"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port= 5000)