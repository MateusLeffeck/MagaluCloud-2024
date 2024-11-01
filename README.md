# Hack or Treat - Magalu Cloud

## Descrição e Justificativa

O projeto foi desenvolvido para o Hackathon do MagaluHack. Propomos criar uma solução que facilitará a criação, gerenciamento, execução e deleção de instâncias na Magalu Cloud. A solução seria constituída por uma interface web para que os usuários pudessem personalizar as máquinas virtuais conforme a sua necessidade. Usando o Terraform, criaríamos uma VM base na Magalu Cloud, e a partir dessa máquina virtual, os usuários poderiam solicitar novas VMs para uso específico.

O projeto giraria em torno do uso de código Python, como scripts de web crawlers, por exemplo. Os códigos ficariam funcionando na VM base e o seu processamento seria feito na Magalu Cloud, utilizando os recursos de nuvem de forma eficiente e personalizada.

## I. Motivação

Com a cada vez mais crescente demanda de recursos computacionais em nuvem, é essencial ter ferramentas que facilitem o uso destes recursos. Foi pensando nisso que desenvolvemos este projeto. Nosso objetivo era desenvolver uma plataforma para simplificar e automatizar a criação e gestão de instâncias em nuvem, de modo que os usuários finais pudessem focar em suas aplicações e esquecer da infraestrutura.

## Desafios Voltados ao Contexto no Magalu

**Principais desafios encontrados:**

- **Documentação da Magalu Cloud**: Como a tecnologia é bem nova, a documentação oficial sobre a Magalu Cloud encontrava-se confusa e incompleta, o que dificultou um entendimento rápido das suas funcionalidades. E como ela não tinha tanto tempo de vida, também faltavam soluções prontas para basear o nosso produto, o que dificultou bastante a engenharia das nossas soluções para solucionar os problemas existentes.

- **Conhecimento em Terraform**: Nossa equipe tinha tido superficialmente algum contato com o uso do Terraform até então, o que limitou bastante nossa capacidade e possibilidades de desenvolver soluções para o Hackathon.

- **Utilização da API da Magalu Cloud**: Ao utilizarmos a API da Magalu, encontramos falta de clareza, informações nem sempre condizentes com a realidade e falta de informações em vários níveis. Isso acabou tornando a evolução mais lenta em diversos momentos; até mesmo os monitores do evento, em boa parte, não souberam nos ajudar.

**Como Superamos os Desafios:**

- **Pesquisa e Aprendizado Autônomo**: Buscamos informações em fóruns e comunidades de desenvolvedores para complementar a documentação oficial, descobrindo soluções alternativas e entendendo melhor as ferramentas.

- **Testes e Experimentação**: Realizamos vários testes para entender o comportamento das ferramentas, o que nos ajudou a contornar a falta de exemplos práticos.

- **Trabalho em Equipe**: A comunicação aberta e constante nos permitiu compartilhar conhecimentos e resolver problemas mais rapidamente.

- **Interação com Mentores**: Apesar das limitações, buscamos auxílio com os monitores e organizadores sempre que possível, alinhando expectativas e obtendo orientações.

**Resultados e Aprendizados:**

- **Conhecimento Técnico**: Aprendemos na prática sobre a Magalu Cloud, sua API e o Terraform, ampliando nossas habilidades.

- **Resiliência**: Aprimoramos nossa capacidade de lidar com obstáculos, mantendo o foco no objetivo final.

- **Colaboração**: Fortalecemos o trabalho em equipe, valorizando a soma das habilidades individuais.

## Funcionalidades Principais

- **Interface Web Intuitiva**: Desenvolvida com HTML5, CSS3 e Bootstrap 5.

- **Formulário Personalizável**:
  - Dados do usuário: nome e email.
  - Configurações da instância:
    - Nome da instância.
    - Dias de uso.
    - Tipo de máquina (vCPU, RAM, Disco).
    - Upload de scripts Python e arquivos de requisitos (.txt).
    - Opção de IP público.
    - Chave SSH para acesso.
    - Tempo de resposta esperado.

- **Armazenamento de Dados**: Solicitações registradas em arquivos CSV.

- **Automação de Processos**:
  - **Criação de Instâncias**: Script `insert.py` para criar instâncias via API da Magalu Cloud.
  - **Deleção de Instâncias**: Script `delet.py` para remover instâncias após o período definido.
  - **Execução de Scripts**: Possibilidade de executar scripts enviados pelos usuários nas instâncias.

- **Monitoramento e Web Scraping**: Exemplo com o script `webscrapping.py`, que coleta a cotação do Bitcoin a cada 3 minutos.

## Arquitetura do Projeto

### Front-end

- **HTML5 e CSS3**: Estrutura e estilo das páginas.
- **Bootstrap 5**: Componentes responsivos e prontos para uso.
- **Formulários**: Inputs organizados e validados para uma interface clara.

### Back-end

- **Flask**: Framework web em Python para rotas e processamento de dados.
- **CSV**: Armazenamento simples dos dados das solicitações.
- **Integração com a API Magalu Cloud**:
  - `insert.py`: Cria instâncias conforme especificações.
  - `delet.py`: Deleta instâncias após o uso.
  - **Segurança**: Variáveis de ambiente para chaves de API.

### Scripts Adicionais

- **`webscrapping.py`**: Coleta a cotação do Bitcoin periodicamente.

## Fluxo de Funcionamento

1. **Acesso ao Sistema**: O usuário abre a aplicação web.

2. **Preenchimento do Formulário**: Insere dados pessoais e configurações da instância, faz upload de scripts e seleciona o tipo de máquina.

3. **Submissão**: Dados são processados pelo servidor Flask e registrados em `dados.csv`.

4. **Criação da Instância**: O `insert.py` é executado, criando a instância na Magalu Cloud.

5. **Execução de Scripts**: Os scripts do usuário são executados na instância.

6. **Finalização**: Após o período definido, o `delet.py` remove a instância.

## Objetivos Alcançados

- **Automação**: Gestão automática do ciclo de vida das instâncias.

- **Personalização**: Instâncias adaptadas às necessidades dos usuários.

- **Economia**: Otimização de custos ao deletar instâncias ociosas.

- **Facilidade de Uso**: Interface acessível mesmo para quem não tem conhecimento avançado em nuvem.

## Tecnologias Utilizadas

- **Front-end**: HTML5, CSS3, Bootstrap 5.

- **Back-end**: Python 3, Flask.

- **Bibliotecas**: Requests, BeautifulSoup, CSV, dotenv.

- **Controle de Versão**: Git.

- **API**: Magalu Cloud API.

## Como Executar o Projeto

### Pré-requisitos

- Python 3
- Pip
- (Opcional) Virtualenv
- Chave de API da Magalu Cloud

### Passos

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/MateusLeffeck/MagaluCloud-2024.git
   cd MagaluCloud-2024
   ```

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar Variáveis de Ambiente**:
   - Crie um arquivo `.env` com:
     ```
     API_KEY=suachavedeapi
     ```

4. **Executar a Aplicação**:
   ```bash
   python app.py
   ```
   - Acesse `http://localhost:5000` no navegador.

6. **Usar a Aplicação**:
   - Preencha o formulário e envie para criar uma instância.

7. **Scripts de Gerenciamento**:
   - **Criar Instância**:
     ```bash
     python insert.py
     ```
   - **Deletar Instância**:
     ```bash
     python delet.py
     ```
   - **Web Scraping** (exemplo de código enviado):
     ```bash
     python webscrapping.py
     ```

## Contribuidores

- **Diego Lemos**
  - Email: [diego.lemos@usp.br](mailto:diego.lemos@usp.br)
- **Mateus Bernal Leffeck**
  - Email: [mateusleffeck@usp.br](mailto:mateusleffeck@usp.br)
- **Julia Carvalho Ribeiro**
  - Email: [julia_ribeiro@usp.br](mailto:julia_ribeiro@usp.br)
- **José Gustavo Victor Pinheiro Alencar**
  - Email: [josegustavovictor@usp.br](mailto:josegustavovictor@usp.br)