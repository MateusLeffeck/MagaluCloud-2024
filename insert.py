import requests
import json

# REGIÃO SEM O TRACINHO !!!!!!

from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')
region = "br-se1"  # região da vm 

# endpoint da api na parte de instancias
url = f"https://api.magalu.cloud/{region}/compute/v1/instances"
# header da requisicao
headers = {
    "x-api-key": api_key,
    "Accept": "application/json"
}
machine_types = {


    'BV8-32-100': '388cddd2-e8c8-4f2f-9247-6f441320df34',
    'BV4-8-100': 'dfc14d19-93dc-4b2a-9d78-a9a235507d14',
    'BV1-1-10': '0122fb85-0fd0-47d1-bf25-f24ca6f11493',
    'BV2-2-40': '3af39578-fce4-491d-88a6-f41c3eaf83fc'

}
zona_vm = ''
id_imagem = "99a6e7e4-86b6-4106-bd38-e6a1c6270ef7"  # ubuntuzada 22.04 lts bro yes nugget
nome_instancia = "site-uniao-bsi" 
id_tipo_machine = machine_types["BV1-1-10"] # id do tipo de maquina  
ssh_key_name = "uniao-bsi-23-24-25"  
ip_publico_bool = True

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
    "ssh_key_name": ssh_key_name,
    # "user_data": "some_base64_script" # script para executar assim que a instancia for criada 
}



# request para criar a vm (PERIGO !!!!!)
response = requests.post(url, headers=headers, data=json.dumps(dados))


if response.status_code == 201:
    print("Instância criada com sucesso!")
    print("Detalhes da instância:", response.json())
else:
    print("Erro ao criar a instância:", response.status_code)
    print("Resposta:", response.json())
