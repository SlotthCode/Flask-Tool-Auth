from flask import Flask, jsonify, request
import time, requests, json
from dataclasses import dataclass

@dataclass
class User:
  username: str
  password: str
  hwid: str




app = Flask(__name__)
start = time.time()

@app.route("/uptime")
def uptime():
      end = time.time()
      uptime = {"uptime": end - start}
      return jsonify(uptime)
  
@app.route("/api/auth", methods=['POST'])
def auth():
    datas = request.get_json()
    rip = {
      "status":"success", 
      "username": target_user.username, 
      "password": target_user.password, 
      "hwid": target_user.hwid
    }
    target_user = User(**datas)
    f = open ('auth.json', "r")
    data = json.loads(f.read())

    users = [User(**data) for user in data["users"]]
  
    for user in users:
      equ = {
        "username": user.username == target_user.username,
        "password": user.password == target_user.password, 
        "hwid": user.hwid == target_user.hwid    
      }
      if equ["username"] and equ["password"] and equ["hwid"]:
        print(f'{target_user.username} has Login!')
        lol = jsonify({"status": "success", "message": "Login Success"})
            
        f= open ('config.json', "r")
        data = json.loads(f.read()) 
        jsons = {
           "content": f"{rip}"
        }
         
        r = requests.post(data["discordwebhook"], json=jsons)
        return jsonify(lol)
            
    lol = jsonify({"status": "fail", "message": "Login Fail"})
    print(datas)
    f = open ('config.json', "r")
    data = json.loads(f.read())
    rip["status"] = "failed"
    jsons = {
      "content": f"{rip}"
    }
    r = requests.post(data["discordwebhook"], json=jsons)
    return lol
    

          
@app.errorhandler(404)
def page_not_found(e):
    lol = {"error": "Something Happened: " + str(e)}
    return jsonify(lol), 404

app.run("0.0.0.0")
