from flask import Flask
from config import config

def create_app(profile='development'):
  app = Flask(__name__)
  cfg = config[profile]
  app.config_from_object(cfg)
  return app
