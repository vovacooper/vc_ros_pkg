function upFunction(e) {
      document.getElementById("demo").innerHTML = e.id;
    
      var cmdVel = new ROSLIB.Topic({
        ros : ros,
        name : 'cmd_vel_mux/input/teleop',
        messageType : 'geometry_msgs/Twist'
      });
      var cmdVelSim = new ROSLIB.Topic({
        ros : ros,
        name : '/turtle1/cmd_vel',
        messageType : 'geometry_msgs/Twist'
      });

      var vert = 0;
      if(e.id == "Up"){
          vert = 0.2;
      }else if(e.id == "Down"){
          vert = -0.2;
      }
      var ang = 0;
      if(e.id == "Left"){
          ang = 0.5;
      }else if(e.id == "Right"){
          ang = -0.5;
      }
      var twist = new ROSLIB.Message({
        linear : {
          x : vert,
          y : 0,
          z : 0
        },
        angular : {
          x : 0,
          y : 0,
          z : ang
        }
      });
cmdVel.publish(twist);
cmdVelSim.publish(twist);
  }

  document.onkeydown = function(event) {
    var key_press = String.fromCharCode(event.keyCode);
    var key_code = event.keyCode;
    document.getElementById('kp').innerHTML = key_press;
      document.getElementById('kc').innerHTML = key_code;
    var status = document.getElementById('status');
    status.innerHTML = "DOWN Event Fired For : "+key_press;


      var cmdVel = new ROSLIB.Topic({
        ros : ros,
        name : 'cmd_vel_mux/input/teleop',
        messageType : 'geometry_msgs/Twist'
      });
      var cmdVelSim = new ROSLIB.Topic({
        ros : ros,
        name : '/turtle1/cmd_vel',
        messageType : 'geometry_msgs/Twist'
      });

var vert = 0;
      if(key_code == 38){
          vert = 0.2;
      }else if(key_code == 40){
          vert = -0.2;
      }
      var ang = 0;
      if(key_code == 37){
          ang = 0.5;
      }else if(key_code == 39){
          ang = -0.5;
      }
      var twist = new ROSLIB.Message({
        linear : {
          x : vert,
          y : 0,
          z : 0
        },
        angular : {
          x : 0,
          y : 0,
          z : ang
        }
      });
cmdVel.publish(twist);
cmdVelSim.publish(twist);



  }

  var ros = new ROSLIB.Ros({
    url : 'ws://' + document.location.host + ':9090'
  });

  ros.on('connection', function() {
    console.log('Connected to websocket server.');
  });
 ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
  });

  ros.on('close', function() {
    console.log('Connection to websocket server closed.');
  });



