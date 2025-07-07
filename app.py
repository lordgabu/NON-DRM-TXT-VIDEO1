from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gabu Repo</title>
    <link rel="icon" type="image/x-icon" href="https://tinypic.host/image/2ggbw">
</head>

<body style="background-color: #000; color: #fff; font-family: monospace; text-align: center; padding-top: 60px;">
    <div class="container">
        <a href="https://github.com/lordgabu" style="text-decoration: none; color: #ff3c00;">
            <p>
    />▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄<br>
    />███░████░████░████░███░██░██<br>
    />███░███░░███░░███░░███░██░██<br>
    />███░███░░███░░███░░███░██░██<br>
    />▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀<br><br>
    <b style="font-size: 18px;">v2.0.0</b>
</p>

        </a>
    </div>

    <br><br><b

    <footer style="color: white; margin-top: 80px;">
        <center>
            <img src="https://tinypic.host/image/2ggbw" width="240" height="120" alt="Gabu Logo">
            <h3>Powered By GABU</h3>
            <img src="https://tinypic.host/image/2ggbw" width="240" height="120" alt="Gabu Logo">
            <div>
                <p style="margin-top: 10px;">© 2025 Video Downloader. All rights reserved.</p>
            </div>
        </center>
    </footer>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
