from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import pdb

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@52.79.236.114', 27017)
db = client.articles

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
  result = list(db.articles.find({}, {'_id': 0}))
  # result = list(db.articles.find({}))
  return jsonify({'result':'success', 'msg' : 'Get connected', 'dbresult':result})

@app.route('/memo', methods=['POST'])
def saving():
  title_receive = request.form["input-title"]
  comment_receive = request.form["input-text"]

  # db에 넣기
  articles = {"title": title_receive, "comment": comment_receive}
  db.articles.insert_one(articles)
  # pdb.set_trace()

  # db.articles.drop()
  return jsonify({'result':'success'})

@app.route('/update', methods=["POST"])
def update_api():
  id_received = request.form["id"]
  # title_received = request.form["title"]
  # content_received = request.form["comment"]

  # target_star = db.articles.find_one({'id': int(id_received)}, {'_id':False})
  print(id_received)
  # new_like = target_star["like"]+1
  # db.movie_star.update_one({'id':int(id_received)}, {'$set':{'like':new_like}})
  # pdb.set_trace()
  return jsonify({'result':'success'})

@app.route('/delete', methods=["POST"])
def delete_api():
  id_received = request.form["id"]
  db.articles.delete_one({'id': int(id_received)})
  return jsonify({'result':'success'})
  
if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)
