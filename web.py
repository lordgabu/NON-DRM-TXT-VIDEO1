from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running by GABU BHAIYA"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
  
