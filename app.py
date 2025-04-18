from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)