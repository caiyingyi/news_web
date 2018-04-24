# -*- coding:utf-8 -*-
from flask import render_template, request
from . import main
from ..models import Post


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.objects.paginate(page=page, per_page=10)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)


@main.route('/<topic>')
def topic(topic):
    return render_template('topic.html', topic=topic)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    return render_template('post.html')
