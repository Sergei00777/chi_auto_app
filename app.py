from flask import Flask, render_template

app = Flask(__name__)

# Главная страница с каталогом
@app.route('/')
def index():
    return render_template('index.html')

# Страницы автомобилей
@app.route('/car/toyota-corolla')
def toyota_corolla():
    return render_template('car_detail.html')

@app.route('/car/lynk-co')
def lynk_co():
    return render_template('lynk_co.html')

@app.route('/car/mitsubishi-l200')
def mitsubishi_l200():
    return render_template('mitsubishi_l200.html')

@app.route('/car/toyota-land-cruiser-200')
def toyota_land_cruiser_200():
    return render_template('toyota_land_cruiser_200.html')

@app.route('/car/geely-icon')
def geely_icon():
    return render_template('geely_icon.html')

@app.route('/car/haval-f7')
def haval_f7():
    return render_template('haval_f7.html')

@app.route('/car/geely-jiaji')
def geely_jiaji():
    return render_template('geely_jiaji.html')

@app.route('/car/lixiang-l7')
def lixiang_l7():
    return render_template('lixiang_l7.html')

@app.route('/car/geely-xingyue')
def geely_xingyue():
    return render_template('geely_xingyue.html')

@app.route('/car/geely-coolray')
def geely_coolray():
    return render_template('geely_coolray.html')

# Модальные окна и вспомогательные страницы
@app.route('/rent-modal')
def rent_modal():
    return render_template('rent_modal.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)