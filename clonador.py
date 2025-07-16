import json
import asyncio
from telethon import TelegramClient, events
from telegram import Bot
from telegram.error import TelegramError

# Carregar configurações
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
bot_token = config["token"]
clone_pairs = config["clone_pairs"]
link_replacements = config.get("link_replacements", {})

# Converter os IDs de origem para inteiros
CANAIS_ORIGEM = [int(origem) for origem in clone_pairs.keys()]

# Inicializar cliente da conta pessoal
client = TelegramClient("cloner_session", api_id, api_hash)

# Inicializar bot do Telegram
bot = Bot(token=bot_token)

def substituir_links(texto: str) -> str:
    for original, substituto in link_replacements.items():
        texto = texto.replace(original, substituto)
    return texto

@client.on(events.NewMessage(chats=CANAIS_ORIGEM))
async def handler(event):
    origem = str(event.chat_id)  # Mantém como string para buscar no dicionário
    destino = clone_pairs.get(origem)

    if not destino:
        # Isso agora é improvável, mas ainda deixamos como segurança
        print(f"[IGNORADO] Canal {origem} não está mapeado.")
        return

    texto = substituir_links(event.raw_text)

    try:
        await bot.send_message(chat_id=destino, text=texto)
        print(f"[ENVIADO] Mensagem clonada de {origem} para {destino}.")
    except TelegramError as e:
        print(f"[ERRO] Falha ao enviar mensagem para {destino}: {e}")

async def main():
    print("🟢 Clonador híbrido rodando! Sessão pessoal lendo, Bot enviando.")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
