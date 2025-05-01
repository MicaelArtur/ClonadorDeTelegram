Painel de Clonagem de Canais Telegram + Substituição de Links
Este projeto é composto por:

Um painel web para configurar a clonagem de canais e a substituição de links de forma prática.

Um bot do Telegram que escuta mensagens em canais de origem e as replica em canais de destino, substituindo links automaticamente por seus links de afiliados.

📂 Estrutura do Projeto
Arquivo	Função
app.py	Painel web para gerenciar canais e links afiliados
clonador.py	Bot Telegram para clonagem de mensagens
config.json	Arquivo de configuração (token do bot, pares de canais, links afiliados)
requirements.txt	Dependências necessárias para rodar o projeto
style.css	Estilo visual do painel web
index.html	Estrutura HTML do painel web
iniciar_bot.bat	Script para iniciar o bot rapidamente
iniciar_painel.bat	Script para iniciar o painel rapidamente

⚙️ Como Funciona
Painel de Configuração (app.py):

Permite adicionar canais de origem e destino para clonagem.

Permite cadastrar links para serem substituídos automaticamente.

Salva as configurações no arquivo config.json.

Bot de Clonagem (clonador.py):

Escuta mensagens dos canais de origem configurados.

Substitui qualquer link nas mensagens de acordo com o cadastro.

Envia a mensagem modificada para o canal de destino.

🛠️ Como Rodar o Projeto
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure seu config.json com o token do seu bot do Telegram:

json
Copiar
Editar
{
    "token": "SEU_TOKEN_AQUI",
    "clone_pairs": {},
    "link_replacements": {}
}
Inicie o painel:

bash
Copiar
Editar
python app.py
Inicie o bot:

bash
Copiar
Editar
python clonador.py
Ou use os arquivos .bat fornecidos para Windows.

🖥️ Acesso ao Painel
Abra o navegador e acesse:

cpp
Copiar
Editar
http://127.0.0.1:5000/
✨ Tecnologias Utilizadas
Flask (painel web)

Python Telegram Bot (bot de clonagem)

HTML + CSS (painel visual)

Telethon (em dependências futuras, se expandir)

Python 3.10+

📜 Observações
O painel salva automaticamente qualquer nova configuração.

Não esqueça de garantir que o seu bot tem permissão de admin nos canais envolvidos.

Este projeto é apenas uma base inicial — você pode expandir com botões interativos, envio de mídias, entre outros.
