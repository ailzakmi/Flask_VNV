import datetime
import random
from flask import Flask

counter_int = 0
cars_mails = ["Lada", "Volkswagen", "Lotus", "Mitsubishi", "Reno", "Lamborghini"]
cats_murlikin = ["Мейн-кун", "Сиамская", "Бурма", "Британская", "Сфинкс", "Корниш-рекс", "Русская голубая", "Шотландская вислоухая", "Манчкин"]

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
    return ', '.join(cars_mails)

@app.route('/cats')
def cats():
    return random.choice(cats_murlikin)

@app.route('/get_time/now')
def get_time_now():
    current_time = str(datetime.datetime.now())
    return "Текущее время: {" + current_time + "}"

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = str(datetime.datetime.now() + datetime.timedelta(hours=1))
    return "Через час будет: {" + current_time_after_hour + "}"

@app.route('/get_random_word')
def get_random_word():
    return "Книги нет, но вы держитесь."

if __name__ == '__main__':
    app.run(debug=True,
            port=5555)