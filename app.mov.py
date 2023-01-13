from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.uazu7ta.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    count = list(db.movies.find({}, {'_id': False}))
    num = len(count) + 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('meta[property="og:image"]')['content']
    title = soup.select_one('meta[property="og:title"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'image':image,
        'title':title,
        'desc':desc,
        'star':star_receive,
        'comment':comment_receive,
        'num':num
    }
    db.movies.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movie_list})

@app.route("/movies/done", methods=["POST"])
def movie_done():
    num_receive = request.form['num_give']
    db.movies.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

# 아따.....num번호를 앞으로 땡기고싶은데...
# @app.route("/movies/done", methods=["POST"])
# def movie_update():
#     count = list(db.movies.find({}, {'_id': False}))
#     num = len(count) + 1
#     num_born = request.form['num_update']
#     db.users.update({'num': num}, {'$set': {'num': int(num_born)}})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)