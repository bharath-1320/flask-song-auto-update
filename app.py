from flask import Flask
app = Flask(__name__)

@app.route('/')
def rhyme():
    return """
    <html>
    <head>
        <title>Twinkle Twinkle</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                padding: 40px;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                font-size: 28px;
                text-align: center;
                margin-bottom: 20px;
            }
            p {
                font-size: 18px;
                color: #555;
                text-align: center;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>My Facourite Rhyme</h1>
            <p>Twinkle Twinkle Little Star</p>
            <p>How I wonder what you are!</p>
            <p>Up above the world so high,</p>
            <p>Like a diamond in the sky.</p>

            <p>Twinkle Twinkle Little Star</p>
            <p>How I wonder what you are!</p>
            <p>Up above the world so high,</p>
            <p>Like a diamond in the sky.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

