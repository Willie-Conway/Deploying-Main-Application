from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################

@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################

@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200
    return {"message": "Internal server error"}, 500

######################################################################
# GET ALL PICTURES
######################################################################

@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200

######################################################################
# GET A PICTURE BY ID
######################################################################

@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    for picture in data:
        if picture["id"] == id:
            return jsonify(picture), 200
    return jsonify({"message": "picture not found"}), 404

######################################################################
# CREATE A PICTURE
######################################################################

@app.route("/picture", methods=["POST"])
def create_picture():
    picture_in = request.json  # Get the picture data from the request body
    
    # Check if a picture with the same id already exists
    for picture in data:
        if picture_in["id"] == picture["id"]:
            return jsonify({
                "Message": f"picture with id {picture_in['id']} already present"
            }), 302  # Return HTTP 302 if the picture already exists
    
    # Append the new picture to the data list
    data.append(picture_in)
    
    # Return the newly created picture with HTTP 201 status
    return jsonify(picture_in), 201

######################################################################
# UPDATE A PICTURE
######################################################################

@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    # Extract the updated picture data from the request body
    picture_in = request.json
    
    # Search for the picture with the given id in the data list
    for index, picture in enumerate(data):
        if picture["id"] == id:
            # If picture is found, update it with the incoming data
            data[index] = picture_in
            return jsonify(picture_in), 201  # Return the updated picture with HTTP 201 status
    
    # If picture is not found, return 404 Not Found with an error message
    return jsonify({"message": "picture not found"}), 404

######################################################################
# DELETE A PICTURE
######################################################################

@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    # Traverse the data list to find the picture by id
    for picture in data:
        if picture["id"] == id:
            data.remove(picture)  # Remove the picture from the list
            return "", 204  # Return an empty response with 204 No Content status
    
    # If picture is not found, return 404 Not Found with a message
    return jsonify({"message": "picture not found"}), 404
