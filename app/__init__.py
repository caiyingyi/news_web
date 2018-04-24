# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import config
from flask_moment import Moment
from flask_mongoengine import MongoEngine
import datetime

bootstrap = Bootstrap()
moment = Moment()
mongo_db = MongoEngine()


# 自定义jinjia2的过滤器
def transform_timestamp(timestamp):
    d = datetime.datetime.fromtimestamp(timestamp)
    result = d.strftime("%Y-%m-%d")
    return result


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    mongo_db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 注册jinjia2的自定义过滤器
    env = app.jinja_env
    env.filters['transform_timestamp'] = transform_timestamp

    return app
