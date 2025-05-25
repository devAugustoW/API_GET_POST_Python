# imports
import json
import pytest
import sys
import os

# Adiciona o app que esta em main.py 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from main import app

# Teste para endpoint de listar todos os itens
def test_get_items():
   client = app.test_client()
   response = client.get('/api/items')
   assert response.status_code == 200
   
   data =json.loads(response.data)
   assert len(data) == 3
   assert data[0]["nome"] == "Calca Jeans"


# Teste para endpoint de enviar um item
def test_create_item():
   client = app.test_client()
   new_item = {"id": 4, "nome": "Pytest", "preco": 10.00}
   
   response = client.post('/api/items', 
                          data=json.dumps(new_item), 
                          content_type='application/json')

   assert response.status_code == 201
   
   data = json.loads(response.data)
   assert data["message"] == "Item adicionado"
 
# Teste para endpoint de buscar um item específico
def test_get_item_by_id():
   client = app.test_client()
   response = client.get('/api/items/2')
   assert response.status_code == 200

