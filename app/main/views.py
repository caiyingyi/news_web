# -*- coding:utf-8 -*-
from flask import Flask
from . import main

app = Flask(__name__)


@main.route('/')
def hello_world():
    return 'Hello World!'