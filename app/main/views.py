# -*- coding:utf-8 -*-
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/<category>')
def category(category):
    return render_template('category.html', category=category)
