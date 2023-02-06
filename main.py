from flask import Flask, jsonify, request
import time, requests, json



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
    f = open ('auth.json', "r")
    data = json.loads(f.read())
  
    for i in data["users"]:
      if datas["username"] == i["username"]:
        if datas["password"] == i["password"]:
          if datas["hwid"]== i["hwid"]:
            print(f'{datas["username"]} has Login!')
            lol = jsonify({"status": "success", "message": "Login Success"})
            
            f= open ('config.json', "r")
            data = json.loads(f.read())
            rip = {"status":"success", "username": datas["username"], "password":datas["password"], "hwid":datas["hwid"]}
            jsons = {
              "content": f"{rip}"
            }
            
            r = requests.post(data["discordwebhook"], json=jsons)
            return lol
          else:
            pass
            
    lol = jsonify({"status": "fail", "message": "Login Fail"})
    print(datas)
    f = open ('config.json', "r")
    data = json.loads(f.read())
    rip = {"status":"failed", "username": datas["username"], "password":datas["password"], "hwid":datas["hwid"]}
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
