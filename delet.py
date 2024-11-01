import requests

from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')

# RECEBER CSV
id = 'ff75e6cc-abbd-43d7-9ad6-2b2e013980a7'
url = f'https://api.magalu.cloud/br-se1/compute/v1/instances/{id}'

headers = {
    "x-api-key": api_key,
    "Accept": "application/json"
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print("Instância deletada com sucesso!")
    print("Detalhes da instância:", response.json())
else:
    print("Erro ao deletar a instância:", response.status_code)
    print("Resposta:", response.json())



