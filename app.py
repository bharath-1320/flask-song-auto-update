from flask import Flask
app = Flask(__name__)

@app.route('/')
def rhyme():
    return """
    <h1>Twinkle Twinkle Little Star</h1>
    <p>How I wonder what you are!</p>
    <p>Up above the world so high,</p>
    <p>Like a diamond in the sky.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

