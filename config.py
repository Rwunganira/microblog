from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
basedir=os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'python.datasciencesr@gmail.com'
    MAIL_PASSWORD = 'Metropolis1!'
    ADMINS = ['python.datasciencesr@gmail.com', 'samuel.rwunganira@gmail.com']
    POSTS_PER_PAGE = 10
