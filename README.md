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
add this
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

modify this file
```Bash
/etc/uwsgi/apps-available/uwsgi.ini
```
Add
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




installation
===========

//git
```Bash
sudo apt-get install git
```

//Get repository
```Bash
cd /var/www/
git clone http://github.com/vovacooper/vc_ros_pkg
```

//Install pip
```Bash
sudo apt-get install python-pip
```
//install virtual env for python/flask/uwsgi
sudo pip install virtualenv

//create new virtual env
```Bash
virtualenv venv
```

//install req for python-flask
```Bash
./venv/bin/pip install -r requirements.txt
```

//install 
```Bash
sudo apt-get install nginx
sudo apt-get install uwsgi
```

//modify ini files for nginx/uwsgi

//for plugin fix
```Bash
mkdir -p /usr/lib/uwsgi/plugins
```
//MUST!!!!
```Bash
apt-get install uwsgi-plugin-python
```

//Logger permitions
```Bash
sudo mkdir /var/log/vc_ros_pkg
sudo chmod 777 vc_ros_pkg
```

//Video jpeg
```Bash
sudo apt-get install ros-groovy-mjpeg-server
```

