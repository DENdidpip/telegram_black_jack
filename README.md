# 🎰 Telegram Blackjack Bot

Simple Telegram bot for playing Blackjack (21) with registration, login system, and SQLite balance.

## 🚀 Features
- User registration and login (username + password)
- Blackjack game vs dealer
- Balance system (bet = 1)
- Starting bonus (3 points)
- Card values with proper Blackjack rules
- Reply keyboard controls
- SQLite database

## 🎮 How to Play
1. Start bot with `/start`
2. Register or log in
3. Press `🎲 play(price = 1)`
4. Choose:
   - `hit` → take a card
   - `stand` → stop and let dealer play
5. Closest to 21 wins

## 🧠 Rules
- 2–10 = face value
- J, Q, K = 10
- Ace = 1 or 11
- Over 21 = lose
- Dealer draws until 17+

## 🛠 Tech Stack
- Python 3
- pyTelegramBotAPI (telebot)
- SQLite
- python-dotenv

## 📦 Installation
```bash
pip install pyTelegramBotAPI python-dotenv