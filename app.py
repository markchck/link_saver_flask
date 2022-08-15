from curses import meta
from email import header
from http import client
from pydoc import describe
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@52.79.236.114', 27017)
db = client.articles

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
  result = list(db.articles.find({}, {'_id': 0}))
  return jsonify({'result':'success', 'msg' : 'Get connected', 'dbresult':result})

@app.route('/memo', methods=['POST'])
def saving():
  # 클라이언트로부터 데이터 받기
  url_receive = request.form["url_give"]
  comment_receive = request.form["comment_give"]

  # meta tag 스크래핑 하기
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
  }
  data = requests.get(url_receive, headers=headers)
  soup = BeautifulSoup(data.text, "html.parser")
  og_image = soup.select_one('meta[property="og:image"]')["content"]
  og_title = soup.select_one('meta[property="og:title"]')["content"]
  og_description = soup.select_one('meta[property="og:description"]')["content"]
  
  # db에 넣기
  articles = {"url": url_receive, "comment": comment_receive, "image": og_image, "title": og_title, "description":og_description}
  db.articles.insert_one(articles)

  return jsonify({'result':'success'})

  
if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)
