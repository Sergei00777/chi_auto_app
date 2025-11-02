from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rent-modal')
def rent_modal():
    return render_template('rent_modal.html')

if __name__ == '__main__':
    app.run(debug=True)