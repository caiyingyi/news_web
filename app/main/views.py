# -*- coding:utf-8 -*-
from flask import render_template, request, redirect
from . import main
from ..models import Post


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.objects.paginate(page=page, per_page=10)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)


@main.route('/topic/<topic>')
def topic(topic):
    page = request.args.get('page', 1, type=int)
    todo = Post.objects(topic=topic)
    pagination = todo.paginate(page=page, per_page=10)
    posts = pagination.items
    return render_template('topic.html', posts=posts, topic=topic, pagination=pagination)


@main.route('/analysis', methods=['GET', 'POST'])
def analysis():
    return redirect("https://datav.aliyun.com/share/d0a7559e0e5d8ab9d64a51182c01e804")


@main.route('/<topic>/<id>', methods=['GET', 'POST'])
def post(topic, id):
    post = Post.objects.get_or_404(_id=id)
    return render_template('post.html', post=post)
