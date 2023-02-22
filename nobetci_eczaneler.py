import requests
from bs4 import BeautifulSoup
import telegram

bot_token = 'BOT_TOKEN' # Telegram bot tokenınızı buraya girin
bot = telegram.Bot(token=bot_token)
chat_id = 'CHAT_ID' # Telegram sohbet ID'sini buraya girin

response = requests.get('https://www.eczaneler.gen.tr/nobetci-istanbul')
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='table table-striped table-hover table-bordered')
table_rows = table.find_all('tr')

message = "İstanbul'da Bugün Nöbetçi Olan Eczaneler:\n"
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    message += f"\n{row[0]}\nAdres: {row[1]}\nTelefon: {row[2]}"

bot.send_message(chat_id=chat_id, text=message)
