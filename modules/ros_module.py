__author__ = 'vovacooper'
import os
from flask import Blueprint, request, render_template, send_file, Response, redirect, json

from providers.geo_ip_provider import GeoIpProvider

from classes.logger import logger

from classes.localDB import localDB

########################################################################################################################

ros_module = Blueprint('ros_module', __name__, url_prefix="/ros")

########################################################################################################################
#Landing page
########################################################################################################################

@ros_module.route("/get_widget_list", methods=['POST', 'GET'])
def get_widget_list():
    """
    :return: the widgets.
    """
    return json.dumps(localDB.getData()["widgets"])


@ros_module.route("/get_saved_names", methods=['POST', 'GET'])
def get_saved_names():
    """
    :return: list of save names.
    """
    return json.dumps(localDB.getData()["users"])


@ros_module.route("/get_saved_serialization", methods=['POST', 'GET'])
def get_saved_serialization():
    """
    :return: serialization.

    @savename - the name of the serialization
    """
    request_data = \
        {
            "method": "GET",
            "ip": request.remote_addr,
            "user": request.args.get("user", "default"),
        }
    return json.dumps(localDB.getData()["serialization"][request_data["user"]])


@ros_module.route("/save_serialization", methods=['POST', 'GET'])
def save_serialization():
    """
    saves serialization state for a name
    :return:

    @data - the serialization data
    @savename - the name of the save
    """
    if request.method == 'GET':
        request_data = \
            {
                "method": "GET",
                "ip": request.remote_addr,
                "user": request.args.get("user", "default"),
                "serialization": request.args.get("serialization", None)
            }
    else:
         request_data = \
            {
                "method": "GET",
                "ip": request.remote_addr,
                "user": request.form.get("user", "default"),
                "serialization": request.form.get("serialization", None)
            }
    if request_data["serialization"] == None or request_data["user"] == None:
        return {"status": "Error - please send serialization and User"}

    data = localDB.getData()
    data["serialization"][request_data["user"]] = request_data["serialization"]
    localDB.saveData(data)

    return json.dumps({"status": "OK"})


@ros_module.route("/", methods=['POST', 'GET'])
def index():
    """
    :return: a widget

    @callback - JSONP method name, make ? as default
    @widget - [button,cmd,depth,graph,joystick,keypad,led,log,rgb], log is the default widget
    @ros_host_ip - the ip of the ROS host machine - default is the web server IP
    @ros_host_port - the IP of the ROS machine, default is 9090
    @topic - the topic to publish/subscribe to
    @messagetype - the messagetype of the topic
    @name - the name of the widget
    @freq - the freq of the continues CMD to be sent to ROS
    """
    try:
        if request.method == 'GET':
            request_data = \
                {
                    "method": "GET",
                    "ip": request.remote_addr,
                    "callback": request.args.get("callback", False),
                    "ros_host_ip": request.args.get("ros_host_ip", "document.location.hostname"),
                    "ros_host_port": request.args.get("ros_host_port", "9090"),
                    "widget": request.args.get("widget", "log"),
                    "topic": request.args.get("topic", "/turtle1/cmd_vel"),
                    "messagetype": request.args.get("messagetype", "geometry_msgs/Twist"),
                    "name": request.args.get("name", "Simulator"),
                    "freq": request.args.get("freq", 1),
                }
        else:
            request_data = \
                {
                    "method": "POST",
                    "ip": request.remote_addr,
                    "callback": request.form.get("callback", False),
                    "postRequestData": request.form,
                    "ros_host_ip": request.form.get("ros_host_ip", "document.location.host"),
                    "widget": request.form.get("widget", "log"),
                    "topic": request.form.get("topic", "/turtle1/cmd_vel"),
                    "messagetype": request.form.get("messagetype", "geometry_msgs/Twist"),
                    "name": request.form.get("name", "S'imulator"),
                    "freq": request.form.get("freq", 1),
                }

        response_json = render_template("widgets/widget_ros_" + request_data["widget"] + ".html", data=request_data)

        if request_data["callback"]: #JSONP
            response_json = "{0}({1})".format(request_data["callback"], json.dumps({"html": response_json}))
            return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
        else: #NOT JSONP
            return response_json
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response




'''
TEST area
'''

@ros_module.route("/joystick", methods=['POST', 'GET'])
def vc_rog_widget_joystick():
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


