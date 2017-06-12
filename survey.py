from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def info():
    return render_template('info.html',full_name="Krista Neumeyer",location="Washington D.C.",language="Python", comments="No comments at this time." )




app.run(debug=True)