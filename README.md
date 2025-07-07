<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+Txt+Uploader+Bot+!" alt="Typing SVG">
</p>

<h1 align="center">📥 Txt Uploader Bot</h1>

<p align="center">A powerful Telegram Bot to download and upload NON-DRM videos from TXT files — ready to deploy anywhere 🚀.</p>

<p align="center">
  <a href="https://github.com/popeye68/NON-DRM-TXT-VIDEO/stargazers">
    <img src="https://img.shields.io/github/stars/popeye68/NON-DRM-TXT-VIDEO?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/popeye68/NON-DRM-TXT-VIDEO/fork">
    <img src="https://img.shields.io/github/forks/popeye68/NON-DRM-TXT-VIDEO?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/popeye68/NON-DRM-TXT-VIDEO/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/popeye68/NON-DRM-TXT-VIDEO?style=for-the-badge" alt="License">
  </a>
</p>

---

## 🚀 Features

✅ Download videos from TXT files (NON-DRM supported)  
✅ Upload to Telegram  
✅ Simple /start, /stop, /help, many more commands  
✅ Admin control 
✅ Easy to deploy on **Heroku**, **Render**, **Koyeb**, or **your own VPS**  
✅ Fast and lightweight
---

## 🛠 Commands

```
/start - Start the bot
/stop  - Stop the bot
/help  - Get help using the bot
```

---

## ⚙️ Deployment

You can deploy this bot with a single click on your favorite cloud service:

### 🌐 Deploy buttons

<p align="center">
  <a href="https://heroku.com/deploy?template=https://www.github.com/popeye68/NON-DRM-TXT-VIDEO">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
  </a>
  &nbsp;
  <a href="https://render.com/deploy?repo=https://github.com/popeye68/NON-DRM-TXT-VIDEO">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
  </a>
  &nbsp;
  <a href="https://app.koyeb.com/deploy?name=NON-DRM-TXT-VIDEO&repository=popeye68%2FNON-DRM-TXT-VIDEO&branch=main&instance_type=free&instances_min=0">
    <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb">
  </a>
</p>

---

## ⚙️ Required Vars / Environment Variables

| Variable    | Description                   |
|-------------|-------------------------------|
| `API_ID`    | Your Telegram API ID           |
| `API_HASH`  | Your Telegram API HASH         |
| `BOT_TOKEN` | Bot Token from [@BotFather](https://t.me/BotFather) |
| `ADMIN`     | Your Telegram user ID (Admin only) |

```env
API_ID=1234567
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
ADMIN=your_telegram_user_id
```

---

## 🖥 Manual Deployment Guide (If you want to deploy manually)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/popeye68/NON-DRM-TXT-VIDEO.git
cd NON-DRM-TXT-VIDEO
```

### 2️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Set your environment variables (API_ID, API_HASH, BOT_TOKEN, ADMIN)

You can export them manually:

```bash
export API_ID=1234567
export API_HASH=your_api_hash_here
export BOT_TOKEN=your_bot_token_here
export ADMIN=your_telegram_user_id
```

Or create a `.env` file.

### 4️⃣ Run the bot

```bash
python3 main.py
```

---

## 📚 How to use the bot

1️⃣ Start the bot with `/start`  
2️⃣ Upload a `.txt` file containing NON-DRM video links  
3️⃣ Bot will process the TXT and upload videos to Telegram  

---

## ❓ FAQ

- **Q:** Does it support DRM videos?  
  **A:** ❌ No, it works only with NON-DRM videos.

- **Q:** Can I deploy it for free?  
  **A:** ✅ Yes, on Koyeb free tier, Render free tier, or Heroku (with free dyno if available).

- **Q:** How do I become admin?  
  **A:** Put your Telegram user ID in the `ADMIN` variable.

---

## ✨ Credits

- Developed by [@popeye68](https://github.com/popeye68)  
- Inspired by open source community ❤️  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Support

If you like this project, give it a ⭐ on GitHub!  
For any issues, open an [issue](https://github.com/popeye68/NON-DRM-TXT-VIDEO/issues).

---

<p align="center">Made with ❤️ for Telegram users!</p>
