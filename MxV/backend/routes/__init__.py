from flask import Flask

from .index import index_bp
from .join import join_bp

def register_routes(app: Flask):
	app.register_blueprint(index_bp)
	app.register_blueprint(join_bp)