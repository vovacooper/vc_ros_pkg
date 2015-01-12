vc_ros_pkg
==========

ROS package


place the package under 
```Bash
~/catkin_ws/src path
```
run catkin_make from 
```Bash
~/catkin_ws folder
```



installation
===========

Git
```Bash
sudo apt-get install git
```

Get repository
```Bash
cd /var/www/
git clone http://github.com/vovacooper/vc_ros_pkg
```

Install pip
```Bash
sudo apt-get install python-pip
```


nginx configuration:
-------------------

nginx install:
```Bash
apt-get install nginx
```
configure
```Bash
/etc/nginx/sites-available/default
```
/etc/nginx/sites-available/default
```Bash
server
{
    listen       80 default_server;
    location /
    {
        uwsgi_pass unix:/var/run/vc_ros_pkg.sock;
        include uwsgi_params;
    }
}
```
UWSGI configuration
-------------------

UWSGI install:
```Bash
apt-get install uwsgi
```
modify this file
```Bash
/etc/uwsgi/apps-available/uwsgi.ini
```
/etc/uwsgi/apps-available/uwsgi.ini
```Bash
[uwsgi]

master = true
socket = /var/run/vc_ros_pkg.sock

chmod-socket = 666
chown-socket = www-data:www-data

chdir = /var/www/vc_ros_pkg
virtualenv = /var/www/vc_ros_pkg/venv

module = web
callable = app
```

configurations
-------------------

Install virtual env for python/flask/uwsgi
```Bash
sudo pip install virtualenv
```

Create new virtual env
```Bash
virtualenv venv
```

Install req for python-flask
```Bash
./venv/bin/pip install -r requirements.txt
```

for plugin fix
```Bash
mkdir -p /usr/lib/uwsgi/plugins
```
MUST!!!!
```Bash
apt-get install uwsgi-plugin-python
```

Logger permitions
```Bash
sudo mkdir /var/log/vc_ros_pkg
sudo chmod 777 vc_ros_pkg
```

My Test's
-------------------
Video jpeg
```Bash
sudo apt-get install ros-groovy-mjpeg-server
```

