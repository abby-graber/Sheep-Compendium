# Import TestClient to simulate API requests
from fastapi.testclient import TestClient
from models.models import Sheep

# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format
    new_sheep_data = {
        "id": 7,
        "name": "Pika",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    #  Arguments should be your endpoint and new sheep data
    response = client.post("/sheep", json=new_sheep_data)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep_data

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    #  include and assert statement to see if the new sheep data can be retrieved
    get_response = client.get("/sheep/7")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep_data
