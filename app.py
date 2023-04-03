from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def index():
    data_from = requests.get(
        'https://api.dailymotion.com/videos?channel=sport&limit=10')
    data_formated_json = data_from.json()
    print(data_formated_json)
    return render_template('index.html', data=data_formated_json['list'])


@app.route('/news.html')
def about():
    data_from = requests.get(
        'https://api.dailymotion.com/videos?channel=news&limit=10')
    data_formated_json = data_from.json()
    print(data_formated_json)
    return render_template('news.html', data=data_formated_json['list'])


@app.route('/music.html')
def music():
    data_from = requests.get(
        'https://api.dailymotion.com/videos?channel=music&limit=10')
    data_formated_json = data_from.json()
    print(data_formated_json)
    return render_template('music.html', data=data_formated_json['list'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
