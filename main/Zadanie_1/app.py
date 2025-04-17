import datetime
from flask import Flask

counter_int = 0
cars_mails = ["Lada", "Volkswagen", "Lotus", "Mitsubishi", "Reno", "Lamborghini"]
cats_murlikin = ["Мейн-кун", "Сиамская", "Бурма", "Британская", "Сфинкс"]

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"

@app.route('/test')
def test():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                      datetime.datetime.now()

@app.route('/counter')
def counter():
    global counter_int
    counter_int += 1
    return str(counter_int)

@app.route('/cars')
def cars():
    global cars_mails
    return cars_mails;

if __name__ == '__main__':
    app.run(debug=True,
            port=5555)