from flask import Flask

from .index import index_bp


def register_routes(app: Flask):
	app.register_blueprint(index_bp)