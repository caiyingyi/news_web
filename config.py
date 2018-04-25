# -*- coding:utf-8 -*-


class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'testing',
        'host': '39.108.180.114',
        'port': 27017,
    }
    host = "0.0.0.0"
    port = 80


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
