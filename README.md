# Analisador de Emoções

## Discentes

-   [Igor Lima Rocha](https://github.com/igorroc)
-   [Isaac Nascimento Lima](https://github.com/inlima)
-   [João Victor Oliveira Rupp](https://github.com/jvrupp)

## Sobre o projeto

O projeto consiste em um analisador de emoções, que tem como objetivo identificar a emoção de uma pessoa através de uma frase enviada por ela. O projeto foi desenvolvido em Python, utilizando a biblioteca NLTK (Natural Language Tool Kit) para a análise de sentimentos.

## Como instalar/configurar

Antes de tudo, você precisa do **Python 3.8** instalado na sua máquina. Para isso, siga esse link:

[https://www.python.org/downloads/release/python-380/](https://www.python.org/downloads/release/python-380/#:~:text=Files-,Version,-Operating%20System)

e escolha a versão adequada para o seu sistema operacional.

Após isso, você precisa clonar o repositório para a sua máquina. Siga os comandos abaixo:

```bash
git clone https://github.com/igorroc/Socket.git

cd Socket
```

Daqui em diante, recomenda-se a utilização do **Power Shell** no Windows ou do **terminal nativo** no Linux.

Dentro da pasta do projeto, você precisa configurar o ambiente virtual. Para isso, execute o comando abaixo:

```bash
python -m venv venv
```

Após isso, você precisa ativar o ambiente virtual. Para isso, execute o comando abaixo:

```bash
.\venv\Scripts\Activate.ps1
```

E então, você pode instalar as dependências do projeto. Para isso, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

## Erros

Caso você receba o erro abaixo:

```bash
File .\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
```

Execute o comando abaixo para resolver o problema:

```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```

E tente novamente.

## Como executar

Para executar o projeto, você precisa executar o arquivo **servidor.py** em um terminal e **client.py** em outro. Para isso, execute os comandos abaixo:

```bash

python ./server.py

python ./client.py

```
