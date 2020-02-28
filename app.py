from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

BASE_DIR=os.path.dirname(__file__)
print(BASE_DIR)

class Config:
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='blabla'

app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)

class Posts(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    body=db.Column(db.Text(),nullable=False)
    date_posted=db.Column(db.DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return  f"{self.title}"


@app.route('/')
def hello():
    message="hello world"
    return jsonify({"message":message})

#sucessfully created posts
@app.route('/posts',methods=['POST'])
def add_post():
    title=request.json.get('title')
    body=request.json.get('body')


    new_post=Posts(title=title,body=body)
    db.session.add(new_post)
    db.session.commit()
    return  jsonify({"message":"new post created successfully"})

#successfully got all posts
@app.route('/posts',methods=['GET'])
def get_all_posts():
    posts=Posts.query.all()

    if not posts:
        return jsonify({"message":"no posts"})
    else:
        post_list = []
        p = {}
        for post in posts:
            p["title"] = post.title
            p["body"] = post.body
            p["date_posted"] = post.date_posted
            post_list.append(p)

        return jsonify({"posts": post_list})




#successfully got one post
@app.route('/posts/<int:id>',methods=['GET'])
def get_specific_post(id):
    pos_to_fetch=Posts.query.get_or_404(id)
    if pos_to_fetch:
        post = []
        p = {}
        p["title"] = pos_to_fetch.title
        p["body"] = pos_to_fetch.body
        p["date_posted"] = pos_to_fetch.date_posted
        return jsonify({"post": p})
    else:
        return jsonify({"The post doesnot exist"})

#successfully updated the posts
@app.route('/posts/<int:id>',methods=['PUT'])
def update_post(id):
    post_to_update=Posts.query.get_or_404(id)

    if post_to_update:
        post_to_update.title = request.json.get('title')
        post_to_update.body = request.json.get('body')
        db.session.commit()
        p = {}
        p["title"] = post_to_update.title
        p["body"] = post_to_update.body
        return jsonify({"post":p})
    else:
        return jsonify({"Post does not exist"})


@app.route('/posts/<int:id>' , methods=['DELETE'])
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)

    if post_to_delete:
        db.session.delete( post_to_delete )
        db.session.commit()
        return jsonify({ "message" : "Post deleted sucessfully"})
    else:
        return jsonify({"Post does not exist"})


if __name__ == "__main__":
    app.run(debug=True)