import os, logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
# migrate = Migrate()
# cors = CORS()
socketio = SocketIO()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	# db.init_app(app)
	# migrate.init_app(app, db)
	# cors.init_app(app, resources={r"/*": {"origins": Config.CORS_ORIGIN}})
	socketio.init_app(app, async_mode=Config.ASYNC_MODE)
	
	from app.errors import bp as errors_bp
	app.register_blueprint(errors_bp)

	from app.test import bp as test_bp
	app.register_blueprint(test_bp)
	
	return app

	
from app import models