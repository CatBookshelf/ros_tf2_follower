# ros_tf2_follower
In this package we created a ros package as practice for the usage of tf2 in ROS.

The goal was to create a launchfile that spawns 3 turtles from turtlesim on a simulation window, where the second turtle follows the first turtle as in [tf2 tutorials](http://wiki.ros.org/tf2/Tutorials/Introduction%20to%20tf2), and the third turtle follows the second turtle from behind too.

The first turtle has to be able to be moved around with the arrow keys, allowing us to see the following of the other two turtles from behind.

Aditionally the amount of times the first turtle collides with the wall has to be stored and able to be accessed at any point on the simulation, taking into account that if the turtle has not been separated from the wall, then it has to stay as one collision.

## Installation
The process for this package to be installed on your ros environment is easy, and as follows:
1. Go to your workspace folder
2. Open your src folder
3. Clone this repository to your src folder

## Running and obtaining data
#### Launching the package scripts
There is only one command to be executed for the user to launch the package: 

```bash
$ roslaunch ros_tf2_follower turtle_tf2_demo2.launch 
```

#### Controlling the turtle1 
The control keys for the movement of the turtle are as follows:
- Arrow key up : Allows the turtle to go forwards.
- Arrow key down : Allows the turtle to go backwards.
- Arrow key left : Allows the turtle to turn counter clockwise.
- Arrow key right : Allows the turtle to turn clockwise.  
#### Obtaining the amount of collisions
The amount of collisions of the first turtle are being stored and published on a topic, so if you want to recover the amount of collisions the turtle1 has had with the walls you just have to subscribe to the topic ***/turtle1/collisions***, either in another script, or by echoing the topic with the following command:

```bash
$ rostopic echo /turtle1/collisions
```

