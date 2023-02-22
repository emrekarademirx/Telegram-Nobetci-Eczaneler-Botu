# Telegram Nöbetçi Eczaneler Botu

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu Telegram botu, [eczaneler.gen.tr](https://www.eczaneler.gen.tr) web sitesinden İstanbul'daki nöbetçi eczane bilgilerini alarak kullanıcılara anlık bildirimler gönderir.

## Kullanım

Telegram botu ile etkileşime geçmek için, botunuzu Telegram uygulamasında arayın. Botu başlatmak için `/start` komutunu kullanın. Bot, nöbetçi eczaneler hakkında güncel bilgileri vermek için hazır olacaktır.

## Gereksinimler

- Python 3.x
- `python-telegram-bot` kütüphanesi
- `requests` kütüphanesi
- `beautifulsoup4` kütüphanesi

## Kurulum

1. Bu depoyu klonlayın veya indirin.

2. Telegram bot token'ınızı alın. Bunun için BotFather botunu kullanabilirsiniz.

3. Gerekli Python kütüphanelerini yüklemek için terminalde proje klasörüne gidin ve şu komutları sırasıyla çalıştırın:

pip install python-telegram-bot
pip install requests
pip install beautifulsoup4


4. `bot.py` dosyasını bir düzenleyicide açın ve `BOT_TOKEN` değişkenini Telegram botunuzun token'ı ile değiştirin.

5. `bot.py` dosyasını çalıştırmak için şu komutu çalıştırın:


python bot.py


Bu, belirtilen web sitesinden alınan nöbetçi eczane bilgilerini Telegram botunuza gönderecektir.

6. Telegram botunuzun sohbet ID'sini bulun. BotFather botunu kullanarak sohbet ID'sini bulabilirsiniz.

7. `bot.py` dosyasında `CHAT_ID` değişkenini bulun ve Telegram botunuzla iletişim kurmak istediğiniz sohbetin ID'si ile değiştirin.

## Lisans

Bu proje, [MIT lisansı](LICENSE) altında lisanslanmıştır.
