import json
import requests


######################################################################
# GET /health tests
######################################################################

def test_health(client):
    """Test the /health endpoint"""
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json == {"status": "OK"}

######################################################################
# GET /song tests
######################################################################

def test_get_songs(client):
    """Test the /song endpoint to get all songs"""
    # Make a GET request to the /song endpoint
    res = client.get("/song")
    
    # Assert that the response status code is 200 OK
    assert res.status_code == 200
    
    # Assert that the response contains a key "songs" and it's a list
    assert "songs" in res.json
    assert isinstance(res.json["songs"], list)
    
    # Optionally, check if the number of songs returned is as expected
    expected_song_count = 20  # Replace with the actual number of songs in your collection
    assert len(res.json["songs"]) == expected_song_count


def test_get_song_by_id(client):
    """Test the /song/<id> endpoint to get a song by id"""
    song_id = 1  # Replace with an actual song id in your database
    
    # Make a GET request to the /song/<id> endpoint
    res = client.get(f"/song/{song_id}")
    
    # Assert that the response status code is 200 OK
    assert res.status_code == 200
    
    # Assert that the response contains the song data and not an error message
    assert "id" in res.json
    assert res.json["id"] == song_id

def test_song_not_found(client):
    """Test that requesting a non-existent song returns 404"""
    non_existent_id = 999  # Replace with an ID that doesn't exist in your database
    
    # Make a GET request to the /song/<non_existent_id> endpoint
    res = client.get(f"/song/{non_existent_id}")
    
    # Assert that the response status code is 404 NOT FOUND
    assert res.status_code == 404
    
    # Assert that the response contains the correct error message
    assert res.json == {"message": f"song with id {non_existent_id} not found"}


######################################################################
# POST /song tests
######################################################################

def test_create_song(client):
    """Test the POST /song endpoint to create a new song"""
    # New song data to be posted
    new_song = {
        "id": 323,
        "lyrics": "Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.\n\nPraesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
        "title": "in faucibus orci luctus et ultrices"
    }

    res = client.post("/song", json=new_song)
    
    # Assert that the response status code is 201 CREATED
    assert res.status_code == 201
    
    # Assert that the response contains the inserted song id
    assert "inserted id" in res.json
    assert isinstance(res.json["inserted id"], str)

def test_create_song_with_duplicate_id(client):
    """Test the POST /song endpoint with an existing song id"""
    # Create a song with an existing ID
    duplicate_song = {
        "id": 323,  # This ID should already exist in the database
        "lyrics": "Duplicate song data.",
        "title": "Duplicate Song"
    }

    res = client.post("/song", json=duplicate_song)
    
    # Assert that the response status code is 302 FOUND
    assert res.status_code == 302
    
    # Assert that the response contains the correct message
    assert res.json == {"Message": "song with id 323 already present"}

######################################################################
# PUT /song tests (Update Song)
######################################################################

def test_update_song(client):
    """Test the PUT /song/<id> endpoint to update a song"""
    song_id = 1  # Replace with an actual song id in your database

    # New data to update the song
    updated_song = {
        "title": "Updated Song Title",
        "lyrics": "Updated song lyrics here"
    }

    res = client.put(f"/song/{song_id}", json=updated_song)
    
    # Assert that the response status code is 200 OK
    assert res.status_code == 200
    
    # Assert that the response contains the updated song data
    assert res.json["id"] == song_id
    assert res.json["title"] == updated_song["title"]
    assert res.json["lyrics"] == updated_song["lyrics"]

def test_update_song_not_found(client):
    """Test that trying to update a non-existent song returns 404"""
    non_existent_id = 999  # Replace with an ID that doesn't exist in your database

    # New data to update the song
    updated_song = {
        "title": "New Song Title",
        "lyrics": "New song lyrics"
    }

    res = client.put(f"/song/{non_existent_id}", json=updated_song)
    
    # Assert that the response status code is 404 NOT FOUND
    assert res.status_code == 404
    
    # Assert that the response contains the correct error message
    assert res.json == {"message": f"song with id {non_existent_id} not found"}

def test_update_song_missing_fields(client):
    """Test that updating a song with missing required fields returns 400"""
    song_id = 1  # Replace with an actual song id in your database

    # Missing the 'lyrics' field
    updated_song = {
        "title": "Song without lyrics"
    }

    res = client.put(f"/song/{song_id}", json=updated_song)
    
    # Assert that the response status code is 400 BAD REQUEST
    assert res.status_code == 400
    
    # Assert that the response contains the correct error message
    assert res.json == {"message": "Missing required fields: title and lyrics are required."}

def test_update_song_no_changes(client):
    """Test that trying to update a song with identical data returns 'nothing updated'"""
    song_id = 1  # Replace with an actual song id in your database
    
    # Same data as the current song
    unchanged_song = {
        "title": "Original Title",
        "lyrics": "Original lyrics"
    }

    res = client.put(f"/song/{song_id}", json=unchanged_song)
    
    # Assert that the response status code is 200 OK
    assert res.status_code == 200
    
    # Assert that the response message indicates nothing was updated
    assert res.json == {"message": "song found, but nothing updated"}

def test_invalid_json(client):
    """Test that sending invalid JSON returns a 400 BAD REQUEST"""
    res = client.put("/song/1", data='{"title": "New title", "lyrics": "New lyrics"')  # Missing closing bracket
    assert res.status_code == 400
    assert res.json == {"message": "Invalid JSON format"}

def test_create_song_missing_data(client):
    """Test the POST /song endpoint with missing title or lyrics"""
    # New song data with missing lyrics
    new_song = {
        "id": 324,
        "title": "Song without lyrics"
    }

    res = client.post("/song", json=new_song)
    
    # Assert that the response status code is 400 BAD REQUEST
    assert res.status_code == 400
    
    # Assert that the response contains the correct error message
    assert res.json == {"message": "Missing required fields: title and lyrics are required."}

######################################################################
# DELETE /song tests
######################################################################

def test_delete_song(client):
    """Test the DELETE /song/<id> endpoint to delete a song"""
    song_id = 1  # Replace with an actual song id that exists in your database
    
    # Make a DELETE request to the /song/<id> endpoint
    res = client.delete(f"/song/{song_id}")
    
    # Assert that the response status code is 204 NO CONTENT
    assert res.status_code == 204

def test_delete_song_not_found(client):
    """Test that trying to delete a non-existent song returns 404"""
    non_existent_id = 999  # Replace with an ID that doesn't exist in your database
    
    # Make a DELETE request to the /song/<non_existent_id> endpoint
    res = client.delete(f"/song/{non_existent_id}")
    
    # Assert that the response status code is 404 NOT FOUND
    assert res.status_code == 404
    
    # Assert that the response contains the correct error message
    assert res.json == {"message": f"song with id {non_existent_id} not found"}
