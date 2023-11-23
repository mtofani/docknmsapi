from app import app
from apis.nedyquerys import api as namespace_api

"""def test_endpoint():
    response = app.test_client().get('/masivos/getStatusCodes/')   
    assert response.status_code == 200
"""""

def test_index_route():
    response = app.test_client().get('/')   
    assert response.status_code == 200 

