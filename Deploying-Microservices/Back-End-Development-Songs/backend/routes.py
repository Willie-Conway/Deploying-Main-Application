from . import app
import os
import json
import pymongo
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401
from pymongo import MongoClient
from bson import json_util
from pymongo.errors import OperationFailure
from pymongo.results import InsertOneResult
from bson.objectid import ObjectId
import sys

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "songs.json")
songs_list: list = json.load(open(json_url))

# client = MongoClient(
#     f"mongodb://{app.config['MONGO_USERNAME']}:{app.config['MONGO_PASSWORD']}@localhost")
mongodb_service = os.environ.get('MONGODB_SERVICE')
mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')
mongodb_port = os.environ.get('MONGODB_PORT')

print(f'The value of MONGODB_SERVICE is: {mongodb_service}')

if mongodb_service == None:
    app.logger.error('Missing MongoDB server in the MONGODB_SERVICE variable')
    # abort(500, 'Missing MongoDB server in the MONGODB_SERVICE variable')
    sys.exit(1)

if mongodb_username and mongodb_password:
    url = f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_service}"
else:
    url = f"mongodb://{mongodb_service}"


print(f"connecting to url: {url}")

try:
    client = MongoClient(url)
except OperationFailure as e:
    app.logger.error(f"Authentication error: {str(e)}")

db = client.songs
db.songs.drop()
db.songs.insert_many(songs_list)

def parse_json(data):
    return json.loads(json_util.dumps(data))

######################################################################
# INSERT CODE HERE
######################################################################

######################################################################
# Implement the /health endpoint
######################################################################

@app.route("/health", methods=["GET"])
def healthz():
    """Health check endpoint"""
    return jsonify({"status": "OK"}), 200

######################################################################
# Implement the /count endpoint
######################################################################

@app.route("/count", methods=["GET"])
def count():
    """Return the number of songs in the database"""
    count = db.songs.count_documents({})
    return jsonify({"count": count}), 200

######################################################################
# Implement the GET /song endpoint
######################################################################

@app.route("/song", methods=["GET"])
def songs():
    """Get all songs from the database"""
    results = list(db.songs.find({}))  # Retrieve all songs from the database
    return jsonify({"songs": parse_json(results)}), 200

######################################################################
# Implement the GET /song/<id> endpoint
######################################################################

@app.route("/song/<int:id>", methods=["GET"])
def get_song_by_id(id):
    """Get a specific song by its ID."""
    song = db.songs.find_one({"id": id})

    if song is None:
        return jsonify({"message": f"song with id {id} not found"}), 404

    return jsonify(parse_json(song)), 200

######################################################################
# Implement the POST /song endpoint
######################################################################

@app.route("/song", methods=["POST"])
def create_song():
    """Create a new song"""
    # Extract the song data from the request body
    song_data = request.get_json()

    # Check if a song with the same ID already exists in the database
    existing_song = db.songs.find_one({"id": song_data["id"]})
    
    if existing_song:
        return jsonify({"Message": f"song with id {song_data['id']} already present"}), 302

    # Insert the new song into the database
    result = db.songs.insert_one(song_data)

    # Return the inserted song ID as part of the response
    return jsonify({"inserted id": str(result.inserted_id)}), 201

######################################################################
# Implement the PUT /song endpoint
######################################################################

@app.route("/song/<int:id>", methods=["PUT"])
def update_song(id):
    """Update an existing song by its ID"""
    # Extract the song data from the request body
    song_data = request.get_json()

    # Validate that the required fields are present
    if not song_data or "title" not in song_data or "lyrics" not in song_data:
        return jsonify({"message": "Missing required fields: title and lyrics are required."}), 400

    # Find the song by its ID
    song = db.songs.find_one({"id": id})

    if not song:
        return jsonify({"message": f"song with id {id} not found"}), 404

    # Check if the song data has changed, to avoid unnecessary updates
    if song["title"] == song_data["title"] and song["lyrics"] == song_data["lyrics"]:
        return jsonify({"message": "song found, but nothing updated"}), 200

    # Update the song in the database
    result = db.songs.update_one(
        {"id": id},  # Find the song by its ID
        {"$set": song_data}  # Update the song fields
    )

    # If the update was successful, return the updated song
    if result.matched_count > 0:
        updated_song = db.songs.find_one({"id": id})
        return jsonify(parse_json(updated_song)), 200

    # If no song was updated, return a relevant message
    return jsonify({"message": "song found, but nothing updated"}), 200

######################################################################
# Implement the DELETE /song/<id> endpoint
######################################################################

@app.route("/song/<int:id>", methods=["DELETE"])
def delete_song(id):
    """Delete a song by its ID"""
    # Attempt to delete the song by its ID
    result = db.songs.delete_one({"id": id})

    # If no song was deleted (deleted_count is 0), return 404 with a message
    if result.deleted_count == 0:
        return jsonify({"message": f"song with id {id} not found"}), 404

    # If the song was successfully deleted, return 204 No Content
    return '', 204
