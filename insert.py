import requests
import json
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def inserir(caminho_csv):
    # Carregar a API key do arquivo .env
    api_key = os.getenv('API_KEY')
    region = "br-se1"  # região da VM

    # Endpoint da API para instâncias
    url = f"https://api.magalu.cloud/{region}/compute/v1/instances"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }

    # Mapear tipos de máquina para IDs correspondentes
    machine_types = {
        'BV8-32-100': '388cddd2-e8c8-4f2f-9247-6f441320df34',
        'BV4-8-100': 'dfc14d19-93dc-4b2a-9d78-a9a235507d14',
        'BV1-1-10': '0122fb85-0fd0-47d1-bf25-f24ca6f11493',
        'BV2-2-40': '3af39578-fce4-491d-88a6-f41c3eaf83fc'
    }

    # ID de imagem padrão e chave SSH padrão
    id_imagem = "99a6e7e4-86b6-4106-bd38-e6a1c6270ef7"  # Ubuntu 22.04 LTS
    ssh_key_name = "uniao-bsi-23-24-25"  # Nome da chave SSH
    ip_publico_bool = True  # Associar IP público

    # Carregar o CSV e selecionar a última linha
    df = pd.read_csv(caminho_csv)
    last_row = df.iloc[-1]  # Obtém apenas a última linha do CSV

    # Obter dados da última linha
    nome_instancia = last_row['Instancia']
    tipo_maquina = last_row['Computador']
    zona_vm = last_row['IP']  # Ajuste conforme necessário, caso o campo 'IP' represente a zona
    
    # Obter o ID do tipo de máquina
    id_tipo_machine = machine_types.get(tipo_maquina)

    # Montar o payload com os dados da VM
    dados = {
        "availability_zone": zona_vm,
        "image": {
            "id": id_imagem
        },
        "machine_type": {
            "id": id_tipo_machine
        },
        "name": nome_instancia,
        "network": {
            "associate_public_ip": ip_publico_bool,
        },
        "ssh_key_name": ssh_key_name
    }

    # Enviar requisição para criar a VM
    response = requests.post(url, headers=headers, data=json.dumps(dados))

    # Verificar a resposta
    response.json[]
