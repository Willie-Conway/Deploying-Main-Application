# Create Get Pictures Service with Flask 🐚📸
 ![Passing All Tests](https://github.com/Willie-Conway/Back-End-Development-Pictures/blob/30102b68a6dda277c02c4ca6f3e250c7c6082cc3/Screenshots/Passing%20All%20Tests.gif)

## Objectives 🎯

- **Create a Flask server**: Set up a Flask application to serve the API endpoints.
- **Write RESTful APIs on picture URL resource**: Implement RESTful CRUD operations (Create, Read, Update, Delete) for managing picture resources.
- **Check the APIs should pass the given pytest tests**: Ensure all endpoints are correctly implemented by running and passing the provided test cases using pytest.

## Overview 📋
This is a RESTful API designed to handle pictures data. It supports the basic operations of **Create**, **Read**, **Update**, and **Delete** (CRUD) for picture resources. The API exposes several endpoints for interacting with a list of pictures.

## Endpoints 🚀

### 1. **Health Check** 🩺
- **Method**: `GET`
- **URL**: `/health`
- **Response**:
  - **Code**: `200 OK`
  - **Body**: `"message": "API is healthy"`

### 2. **Get List of Pictures** 🖼️
- **Method**: `GET`
- **URL**: `/picture`
- **Response**:
  - **Code**: `200 OK`
  - **Body**: 
    ```json
    [
      { "id": 1, "pic_url": "http://example.com/image1.jpg", ... },
      { "id": 2, "pic_url": "http://example.com/image2.jpg", ... }
    ]
    ```

### 3. **Get Picture by ID** 🔍
- **Method**: `GET`
- **URL**: `/picture/{id}`
- **Response**:
  - **Code**: `200 OK`
  - **Body**:
    ```json
    {
      "id": 1,
      "pic_url": "http://example.com/image1.jpg",
      "event_country": "United States",
      "event_state": "California",
      "event_city": "Fremont",
      "event_date": "11/2/2030"
    }
    ```
  - **Error Response** (if picture not found):
    ```json
    {
      "message": "picture not found"
    }
    ```

### 4. **Create Picture** ➕
- **Method**: `POST`
- **URL**: `/picture`
- **Request Body**:
  ```json
  {
    "id": 200,
    "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
    "event_country": "United States",
    "event_state": "California",
    "event_city": "Fremont",
    "event_date": "11/2/2030"
  }
  ```
- **Response**:
  - **Code**: `201 CREATED`
  - **Body**:
    ```json
    {
      "id": 200,
      "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
      "event_country": "United States",
      "event_state": "California",
      "event_city": "Fremont",
      "event_date": "11/2/2030"
    }
    ```
  - **Error Response** (if picture already exists):
    ```json
    {
      "Message": "picture with id 200 already present"
    }
    ```

### 5. **Update Picture by ID** ✏️
- **Method**: `PUT`
- **URL**: `/picture/{id}`
- **Request Body**:
  ```json
  {
    "id": 2,
    "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
    "event_country": "United States",
    "event_state": "California",
    "event_city": "Fremont",
    "event_date": "11/2/2030"
  }
  ```
- **Response**:
  - **Code**: `200 OK`
  - **Body**:
    ```json
    {
      "id": 2,
      "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
      "event_country": "United States",
      "event_state": "California",
      "event_city": "Fremont",
      "event_date": "11/2/2030"
    }
    ```
  - **Error Response** (if picture not found):
    ```json
    {
      "message": "picture not found"
    }
    ```

### 6. **Delete Picture by ID** 🗑️
- **Method**: `DELETE`
- **URL**: `/picture/{id}`
- **Response**:
  - **Code**: `204 NO CONTENT`
  - **Body**: `""` (Empty Body)
  - **Error Response** (if picture not found):
    ```json
    {
      "message": "picture not found"
    }
    ```

## REST API Guidelines 📜

| Action  | Method  | Return Code | Body | URL Endpoint  |
|---------|---------|-------------|------|---------------|
| **List**    | `GET`    | `200 OK`   | Array of pictures  | `/picture` |
| **Create**  | `POST`   | `201 CREATED` | Picture resource  | `/picture` |
| **Read**    | `GET`    | `200 OK`   | Picture resource  | `/picture/{id}` |
| **Update**  | `PUT`    | `200 OK`   | Updated picture   | `/picture/{id}` |
| **Delete**  | `DELETE` | `204 NO CONTENT` | `""` (Empty Body) | `/picture/{id}` |

## Reference: RESTful Service 🧑‍💻

Here are some hints on the RESTful behavior of each of the endpoints.

### List
- **GET /picture**
  - Returns a list of pictures.
  - HTTP status code `200 OK`.

### Read
- **GET /picture/{id}**
  - Accepts a picture ID.
  - If found, returns the picture with HTTP status code `200 OK`.
  - If not found, returns `404 Not Found` with a message `{"message": "picture not found"}`.

### Create
- **POST /picture**
  - Accepts a picture resource in the request body.
  - If the picture exists (i.e., `id` already in data), it returns `302 Found` with a message indicating the picture already exists.
  - If the picture is new, it adds to the list and returns `201 Created`.

### Update
- **PUT /picture/{id}**
  - Accepts a picture ID and updates its data.
  - Returns `200 OK` with the updated picture if successful.
  - Returns `404 Not Found` with a message if the picture isn't found.

### Delete
- **DELETE /picture/{id}**
  - Deletes the picture identified by `id`.
  - Returns `204 No Content` on success.
  - Returns `404 Not Found` if the picture isn't found.

---

### 🎉 Conclusion
This REST API provides a full range of operations for handling pictures in your application. Whether you're listing pictures, creating new ones, updating existing pictures, or deleting them, the API provides the necessary functionality to interact with the data.

