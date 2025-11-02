from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rent-modal')
def rent_modal():
    return render_template('rent_modal.html')

@app.route('/car-detail')
def car_detail():
    return render_template('car_detail.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/main')
def main():
    # Редирект на главную
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)