import json
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Carrega as configurações
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

token = config.get("token")
clone_pairs = config.get("clone_pairs", {})
link_replacements = config.get("link_replacements", {})

# Função para substituir links
def substituir_links(texto):
    for original, novo in link_replacements.items():
        texto = texto.replace(original, novo)
    return texto

# Função principal de clonagem
async def clonar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    origem_id = update.effective_chat.id
    mensagem = update.effective_message

    origem_str = str(origem_id)
    if origem_str in clone_pairs:
        destino = clone_pairs[origem_str]
        novo_texto = substituir_links(mensagem.text or "")

        if mensagem.text:
            await context.bot.send_message(chat_id=destino, text=novo_texto)

# Inicia o bot
if __name__ == "__main__":
    print("🟢 Clonador com marca personalizada e botões rodando!")

    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.ALL, clonar))
    application.run_polling()
