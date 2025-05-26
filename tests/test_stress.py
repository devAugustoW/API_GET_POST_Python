from locust import HttpUser, task, between

class APIUser(HttpUser):
   wait_time = between(1, 5) # Tempo de espera entre requisições
   
   @task(3) # executa 3 vezes
   def get_items(self):
      self.client.get('/api/items')
      
   @task(1) # Executa 1 vez
   def get_item_by_id(self):
      self.client.get('/api/items/1')
      
   @task(1)
   def create_item(self):
      self.client.post('/api/items', json={
         "id": 20,
         "nome": "locust",
         "preco": 10.00
      })