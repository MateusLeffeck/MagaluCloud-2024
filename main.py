from delet import deletar_instancia
from insert import inserir

# Chama a função inserir e obtém o id da instância e o número de dias
instancia_id, dias = inserir('dados.csv')

# Verifica se a instância foi criada antes de chamar deletar
if instancia_id and dias is not None:
    deletar_instancia(instancia_id, dias)
