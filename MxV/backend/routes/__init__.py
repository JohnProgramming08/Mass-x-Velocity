from flask import Flask

from .index import index_bp
from .join import join_bp
from .home import home_bp
from .topics import topics_bp

def register_routes(app: Flask):
	app.register_blueprint(index_bp)
	app.register_blueprint(join_bp)
	app.register_blueprint(home_bp)
	app.register_blueprint(topics_bp)