
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()



def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)
  #app.config['SECRET_KEY'] = 'hard to guess string'
  bootstrap.init_app(app)
  '''mail.init_app(app)
  moment.init_app(app)
  db.init_app(app)'''
  from main.__init__  import main as main_blueprint
  app.register_blueprint(main_blueprint)





  return app
