import ccxt, time, requests
from datetime import datetime

# ============ CONFIG ============
TG_TOKEN = "YOUR_BOT_TOKEN_HERE"
TG_CHAT  = "YOUR_CHAT_ID_HERE"
COINS    = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]
CHECK_EVERY = 300

# ============ TELEGRAM ============
def send(msg):
    try:
        requests.get(
            f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            params={"chat_id": TG_CHAT, "text": msg, "parse_mode": "Markdown"}
        )
    except Exception as e:
        print("TG error:", e)

# ============ EXCHANGE ============
ex = ccxt.binance({"enableRateLimit": True})

# ============ LOGIC ============
def analyze(symbol):
    d = ex.fetch_ohlcv(symbol, "1h", limit=100)
    H = [d[i][2] for i in range(1, len(d)-1) if d[i][2] > d[i-1][2] and d[i][2] > d[i+1][2]]
    L = [d[i][3] for i in range(1, len(d)-1) if d[i][3] < d[i-1][3] and d[i][3] < d[i+1][3]]
    if not H or not L:
        return None
    c, h, l = d[-1][4], H[-1], L[-1]
    atr = sum([max(d[i][2]-d[i][3], abs(d[i][2]-d[i-1][4]), abs(d[i][3]-d[i-1][4]))
               for i in range(1, len(d))][-14:]) / 14
    if c > h:
        sl = l - atr * 0.5
        return {"dir": "LONG", "entry": c, "sl": sl, "tp": c + (c - sl) * 2}
    elif c < l:
        sl = h + atr * 0.5
        return {"dir": "SHORT", "entry": c, "sl": sl, "tp": c - (sl - c) * 2}
    return None

# ============ MAIN LOOP ============
send("Bot Started: " + ", ".join(COINS))
last = {}

while True:
    try:
        for coin in COINS:
            sig = analyze(coin)
            if sig and last.get(coin) != sig['dir']:
                send(f"*{sig['dir']}* — {coin}\n\nEntry: `{round(sig['entry'],4)}`\nSL: `{round(sig['sl'],4)}`\nTP: `{round(sig['tp'],4)}`\n\n_{datetime.now().strftime('%H:%M %d-%b')}_")
                last[coin] = sig['dir']
                print(f"Sent: {coin} {sig['dir']}")
            elif not sig:
                last[coin] = None
        time.sleep(CHECK_EVERY)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
