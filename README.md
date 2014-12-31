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
/etc/nginx/sites-available
```
```Bash
server
{
    listen       80 default_server;
    root /home/lab_alglam/catkin_ws/src/vc_ros_pkg/www;

    location /
    {
    }
}
```

installation
===========

//git
suudo apt-get install git

//Get repository
cd /var/www/
git clone http://github.com/vovacooper/vc_ros_pkg


//Install pip
sudo apt-get install python-pip

//install virtual env for python/flask/uwsgi
sudo pip install virtualenv

//create new virtual env
virtualenv venv

//install req for python-flask
./venv/bin/pip install -r requirements.txt

//install 
sudo apt-get install nginx
sudo apt-get install uwsgi

//modify ini files for nginx/uwsgi



//for plugin but fix
mkdir -p /usr/lib/uwsgi/plugins

//MUST!!!!
apt-get install uwsgi-plugin-python
sudo chmod 777 /var/log/

//Logger
sudo mkdir /var/log/vc_ros_pkg
sudo chmod 777 vc_ros_pkg

