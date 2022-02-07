from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

profile_obj = {}
tank_list = []

tank_count = 0

# GET /profile
@app.route("/profile")
def get_profile():
    return profile_obj

# POST /profile
@app.route("/profile", methods=["POST"])
def post_profile():
    profile_obj["username"] = request.json["username"]
    profile_obj["role"] = request.json["role"]
    profile_obj["color"] = request.json["color"]
    profile_obj["last_updated"] = datetime.now()

    return{
      "success": True,
      "data": profile_obj
    }

# PATCH /profile
@app.route("/profile", methods=["PATCH"])
def update_profile():
  if "username" in request.json:
    profile_obj["username"] = request.json["username"]
  
  if "role" in request.json:
    profile_obj["role"] = request.json["role"]

  if "color" in request.json:
    profile_obj["color"] = request.json["color"]
  
  profile_obj["last_updated"] = datetime.now()
  
  return {
    "success": True,
    "data": profile_obj
  }

# GET /data
@app.route("/data")
def get_tanks():
  return jsonify(tank_list)

@app.route("/data", methods=["POST"])
def add_tank():
  global tank_count
  tank_count+=1
  tank_list.append({
    "id": tank_count,
    "location": request.json["location"],
    "lat": request.json["lat"],
    "long": request.json["long"],
    "percentage_full": request.json["percentage_full"]
  })
  return {
    "id": tank_count,
    "location": request.json["location"],
    "lat": request.json["lat"],
    "long": request.json["long"],
    "percentage_full": request.json["percentage_full"]
  }

# PATCH /data/:id
@app.route("/data/<int:id>", methods=["PATCH"])
def update_tank(id):
  for tank in tank_list:
    if id == tank["id"]:
      if "location" in request.json:
        tank["location"] = request.json["location"]
      
      if "lat" in request.json:
        tank["lat"] = request.json["lat"]

      if "long" in request.json:
        tank["long"] = request.json["long"]

      if "percentage_full" in request.json:
        tank["percentage_full"] = request.json["percentage_full"]

  return tank_list[int(id)-1]

# DELETE /data/:id
@app.route("/data/<int:id>", methods=["DELETE"])
def del_tank(id):
  for tank in tank_list:
    if tank["id"] == id:
      tank_list.remove(tank)

  return {
    "success": True
  }



if __name__ == "__main__":
    app.run(debug=True)

