# Crypto Alert Bot 🚀

Telegram alerts for crypto trading signals. Runs 24/7.

## Features

- Scans any coins (BTC, ETH, SOL, custom)
- Detects breakout signals (1h timeframe)
- Sends Entry, SL, TP to Telegram
- Automatic ATR-based stop loss
- 24/7 runnable on PC or VPS
- Easy configuration

## Setup

1. Install Python packages:
pip install ccxt requests

2. Create Telegram Bot:
- Search @BotFather in Telegram
- Send /newbot to get token
- Search @userinfobot for chat ID

3. Configure alert_bot.py:
TG_TOKEN = "your_bot_token"
TG_CHAT  = "your_chat_id"
COINS    = ["BTC/USDT", "ETH/USDT"]
CHECK_EVERY = 300

4. Run:
python alert_bot.py

## Sample Alert

SHORT - BTC/USDT
Entry: 83719.8
SL:    84589.19
TP:    81981.0

## Custom Work

I build custom bots for clients:
- Custom indicators
- Multiple exchanges
- Backtesting scripts

## Contact

GitHub: @SAYID-CRYPT
