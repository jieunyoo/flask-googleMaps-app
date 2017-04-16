from flask import Flask
from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from .models import Post
from .forms import PostForm
import json
from flask import jsonify

@app.route("/")
def index():
	form = PostForm()
	posts = Post.query.all()
	markedposts = json.dumps([e.serialize() for e in posts])
	return render_template("index.html", posts=markedposts)


@app.route("/submitpost", methods=['POST'])
def submitpost():
	latitude = float(request.form.get("latitude"))
	longitude = float(request.form.get("longitude"))
#	latitude = request.form['latitude']
#	longitude = request.form['longitude']
	post = Post(latitude=latitude, longitude=longitude)
	db.session.add(post)
	db.session.commit()
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(port=5000, debug=True)
