Discord Nuke Bot

Este é um bot para Discord escrito em Python utilizando a biblioteca discord.py. O bot possui um comando que realiza uma série de ações destrutivas em um servidor, incluindo a exclusão de canais, criação de novos canais, envio de mensagens em massa, banimento de membros, entre outras ações. Este bot é apenas para fins educacionais e não deve ser usado em servidores reais sem permissão explícita.
Requisitos

    Python 3.8 ou superior

    Bibliotecas Python: discord.py, colorama, asyncio

Instalação

    Clone o repositório:
    bash
    Copy

    git clone https://github.com/c728x/nukediscord.git
    cd nukediscord

    Instale as dependências:
    bash
    Copy

    pip install -r requirements.txt

    Configure o bot:

        Crie um arquivo config.json na raiz do projeto com o seguinte conteúdo:
        json
        Copy

        {
          "TOKEN": "SEU TOKEN AQUI OH"
        }

        Substitua SEU TOKEN AQUI OH pelo token do seu bot Discord.

#Uso

    Inicie o bot:
    bash
    Copy

    python principal.py

    Comandos disponíveis:

        >nuke: Executa o comando de "nuke" no servidor onde o comando foi executado. Este comando realiza uma série de ações destrutivas, incluindo:

            Exclusão de todos os canais existentes.

            Criação de 50 novos canais de texto e 50 canais de voz.

            Envio de mensagens em massa em todos os novos canais de texto.

            Banimento e expulsão de todos os membros do servidor.

            Alteração do nome do servidor e dos nicknames dos membros.

            Criação de 50 novas roles.

Aviso Legal

Este bot foi criado apenas para fins educacionais e de aprendizado. O uso deste bot em servidores Discord sem a permissão explícita dos administradores do servidor é altamente desencorajado e pode resultar em consequências legais. O autor deste código não se responsabiliza por qualquer uso indevido deste software.
Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o código.
