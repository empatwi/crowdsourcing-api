# empatwi-crowdsourcing-api
Esse repositório contém a API back-end da plataforma Crowdsourcing do projeto Empatwi.
Essa API é responsável por toda a conexão o banco de dados na nuvem, sendo possível acessá-lo via dois endpoints (GET e PUT).

## Instruções

1. É pré-requisito possuir uma versão do Python 3.x, o gerenciador de pacotes pip e a biblioteca de virtualenvironment instalados em sua máquina
1. Primeiramente, é necessário criar um ambiente virtual (`python -m venv venv`)
1. Ative o venv `venv\scripts\activate` no Windows ou `source venv/bin/activate` no Linux
1. Em seguida, instalar as dependências do requirements.txt (`pip install -r requirements.txt`)
1. Para rodar a API, `python src\main.py`
1. Ao acessar `localhost:5000/api`, será possível visualizar o Swagger e testar a API

> Todas as variáveis de ambiente (como Connection String do banco) estão localizadas em um arquivo `.env` local, acessado pela biblioteca `decouple`.