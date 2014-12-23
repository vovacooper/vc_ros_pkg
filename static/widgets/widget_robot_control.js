/////////////////////////////
//init
/////////////////////////////
var ros;
var tpkVel;
var tpkVelSim;

$(document).ready(function() {
   console.log("111111111111");

  try {
    ros = new ROSLIB.Ros({
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
  }
  catch(err) {
      console.log('Error connecting to ROS: ', err);
  }
  tpkVel = new ROSLIB.Topic({
    ros : ros,
    name : 'cmd_vel_mux/input/teleop',
    messageType : 'geometry_msgs/Twist'
  });
  tpkVelSim = new ROSLIB.Topic({
    ros : ros,
    name : '/turtle1/cmd_vel',
    messageType : 'geometry_msgs/Twist'
  });

});


/////////////////////////////
//JoyStick
/////////////////////////////
$( window ).load(function() {
  console.log("222222222222222222222");
  x=$("#joystickcontainer").position();
  
  console.log("touchscreen is", VirtualJoystick.touchScreenAvailable() ? "available" : "not available");

  var joystick  = new VirtualJoystick({
    container : document.getElementById('joystickcontainer'),
    mouseSupport  : true,
    container_pos : { x: x.left , y: x.top},
    limitStickTravel: true,
  });
  joystick.addEventListener('touchStart', function(){
    console.log('down')
  })
  joystick.addEventListener('touchEnd', function(){
    console.log('up')
  })
  setInterval(function(){
    var dx = joystick.deltaX();
    var dy = joystick.deltaY();
    if( Math.abs(dx) < 2 && Math.abs(dy) < 2  ){
      return;
    }
    var twist = generateTwistMsg(dy/100 , dx/100);
    tpkVel.publish(twist);
    tpkVelSim.publish(twist);
    //var outputEl  = document.getElementById('result');
    //outputEl.innerHTML  = '<b>Result:</b> '
    //  + ' dx:' + joystick.deltaX()
    //  + ' dy:' + joystick.deltaY()
    //  + (joystick.right() ? ' right'  : '')
    //  + (joystick.up()    ? ' up'   : '')
    //  + (joystick.left()  ? ' left' : '')
    //  + (joystick.down()  ? ' down'   : '') 
  }, 1/10 * 1000);
});



/////////////////////////////
//Buttons
/////////////////////////////
function generateTwistMsg(x,y){
  var twist = new ROSLIB.Message({
    linear : {
      x : x,
      y : 0,
      z : 0
    },
    angular : {
      x : 0,
      y : 0,
      z : y
    }
  });
  return twist;
}
function moveTurtleButtonUp(e) {
  //document.getElementById("demo").innerHTML = e.id;
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

  var twist = generateTwistMsg(vert , ang);

  tpkVel.publish(twist);
  tpkVelSim.publish(twist);
}

/////////////////////////////
//KeyBoard
/////////////////////////////
document.onkeydown = function(event) {
  //var key_press = String.fromCharCode(event.keyCode);
  var key_code = event.keyCode;
  //document.getElementById('kp').innerHTML = key_press;
  //document.getElementById('kc').innerHTML = key_code;
  //var status = document.getElementById('status');
  //status.innerHTML = "DOWN Event Fired For : "+key_press;

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
  var twist = generateTwistMsg(vert , ang);
  tpkVel.publish(twist);
  tpkVelSim.publish(twist);
}




