import os

APP_PATH = os.path.dirname(os.path.realpath(__file__))
from urlparse import urlparse
from classes.logger import logger
from flask import Flask, render_template, json, send_file, redirect, request
from flask import flash, url_for, session

from flask.ext.compress import Compress
from datetime import timedelta
from classes.config import KEY
from modules.ros_module import ros_module

app = Flask(__name__)

app.jinja_env.autoescape = False

'''
Blueprints
'''
app.register_blueprint(ros_module)
'''
Config
'''
app.config["SECRET_KEY"] = KEY
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=730)
app.config["SESSION_COOKIE_NAME"] = "impo_session"

app.config["WTF_CSRF_ENABLED"] = False


Compress(app)


@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/index")
def ros():
    return render_template("index1.html")


@app.errorhandler(400)
def bad_request(error):
    return json.dumps({"error": str(error)}), 400


@app.errorhandler(401)
def unauthorized(error):
    return json.dumps({"error": str(error)}), 401


@app.errorhandler(404)
def not_found(error):
    return json.dumps({"error": str(error)}), 404


@app.errorhandler(500)
def server_error(error):
    logger.error(error)
    return json.dumps({"error": str(error)}), 500


'''
Main
'''
if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=port, ssl_context="adhoc")
    app.run(host="0.0.0.0", port=5000)
