from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.lslbk.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('page.html')

@app.route("/teampage", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.teampage.insert_one(doc)

    return jsonify({'msg': '남기기 완료!'})

@app.route("/teampage", methods=["GET"])
def homework_get():
    comment_list = list(db.teampage.find({}, {'_id': False}))
    return jsonify({'comment':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


