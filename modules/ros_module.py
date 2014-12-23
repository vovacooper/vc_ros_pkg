__author__ = 'vovacooper'
import os
from flask import Blueprint, request, render_template, send_file, Response, redirect, json

from providers.geo_ip_provider import GeoIpProvider

from classes.logger import logger
########################################################################################################################

ros_module = Blueprint('ros_module', __name__, url_prefix="/ros")



########################################################################################################################
#Landing page
########################################################################################################################
@ros_module.route("/")
def index():
    return render_template("7zip/index.html")


@ros_module.route("/img", methods=['POST', 'GET'])
def vc_rog_widget_img():
    try:
        if request.method == 'GET':
            request_data = \
                {
                    "method": "GET",
                    "ip": request.remote_addr,
                    "callback": request.args.get("callback", False),
                    "tags": request.args.get("tags", False),
                }
        else:
            request_data = \
                {
                    "method": "POST",
                    "ip": request.remote_addr,
                    "callback": request.args.get("callback", False),
                    "last": request.form.get('last', 'None'),
                    "name": request.form.get('name', 'None'),
                    "postRequestData": request.form
                }

        response_json = render_template("widgets/widget_img.html")

        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps({"html": response_json}))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response


@ros_module.route("/log", methods=['POST', 'GET'])
def vc_rog_widget_log():
    return render_template("widgets/widget_log.html")


@ros_module.route("/keypad", methods=['POST', 'GET'])
def vc_rog_widget_keypad():
    return render_template("widgets/widget_robot_control.html")


@ros_module.route("/joystick", methods=['POST', 'GET'])
def vc_rog_widget_joystick():
    render_template("widgets/widget_robot_control_joy.html")
    try:
        if request.method == 'GET':
            request_data = \
                {
                    "method": "GET",
                    "ip": request.remote_addr,
                    "callback": request.args.get("callback", False),
                    "tags": request.args.get("tags", False),
                }
        else:
            request_data = \
                {
                    "method": "POST",
                    "ip": request.remote_addr,
                    "callback": request.args.get("callback", False),
                    "last": request.form.get('last', 'None'),
                    "name": request.form.get('name', 'None'),
                    "postRequestData": request.form
                }

        #init data provider
        data_provider = GeoIpProvider(request_data)
        #get data from provider
        response_data = data_provider.get_data()
        #make json
        response_json = json.dumps(response_data)

        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps(response_data))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response
