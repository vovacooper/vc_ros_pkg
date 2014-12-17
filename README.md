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


