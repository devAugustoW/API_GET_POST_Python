# Imports
from flask import Flask, jsonify, request
import os

# Criar a API
app = Flask(__name__)

# Lista de Itens para API
items = [
   {"id": 1, "nome": "Calca Jeans", "preco": 89.99},
   {"id": 2, "nome": "Camisa", "preco": 55.50},
   {"id": 3, "nome": "Chaveiro", "preco": 9.90,}
]

# Endpoint para listar todos os itens
@app.route('/api/items', methods=['GET'])
def get_items():
   return jsonify(items), 200


# Enpoint para enviar itens
@app.route('/api/items', methods=['POST'])
def create_item():
   data = request.json
   items.append(data)
   return jsonify({"message": "Item adicionado", "item": data}), 201


# Enpoint para buscar um item específico
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
   for item in items:
      if item["id"] == item_id:
         return jsonify(item), 200
   return jsonify({"message": "Item não encontrado"}), 404


# Função que vai executar a aplicação
if __name__ == '__main__':
   app.run(debug=True, port=5000)