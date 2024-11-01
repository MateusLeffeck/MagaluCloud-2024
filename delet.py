import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

def deletar_instancia(id_instancia, dias_espera):
    api_key = os.getenv('API_KEY')
    url = f'https://api.magalu.cloud/br-se1/compute/v1/instances/{id_instancia}'
    
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }

    # Converte o número de dias em segundos e espera o tempo especificado
    segundos_espera = dias_espera * 24 * 60 * 60
    print(f"Aguardando {dias_espera} dias ({segundos_espera} segundos) para deletar a instância...")
    time.sleep(segundos_espera)

    # Executa a requisição DELETE após o tempo de espera
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print("Instância deletada com sucesso!")
    else:
        print("Erro ao deletar a instância:", response.status_code)

# Exemplo de uso
deletar_instancia("ff75e6cc-abbd-43d7-9ad6-2b2e013980a7", 1)  # Aguarda 1 dia antes de deletar
