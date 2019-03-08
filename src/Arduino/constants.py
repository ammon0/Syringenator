##	@file src/pi/constants.py
#	Constants shared across the whole system.
#	Includes constants used by both the arduino sketch and the the python script.
#	The format of `constants.in` is three whitespace sparated columns:
#
#	[NAME] [value] [comments]
#
#	Any changes must be made in `constants.in` and followed by running:
#
#	`make constants`
#
#	--ABD
#
#	@copyright Copyright &copy; 2019 by the authors. All rights reserved.
#
#	This file has been autogenerated, CHANGES MADE HERE WILL NOT PERSIST

## The minimum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_AZIMUTH_MIN = 0
## The maximum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_AZIMUTH_MAX = 0
## The minimum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_RANGE_MIN = 0
## The maximum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_RANGE_MAX = 0
## The minimum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_ORIENT_MIN = 0
## The maximum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_ORIENT_MAX = 0
## The minimum target center x-value that allows a pickup
PICKUP_X_MIN = 0
## The maximum target center x-value that allows a pickup
PICKUP_X_MAX = 0
## The minimum target center y-value that allows a pickup
PICKUP_Y_MIN = 0
## The maximum target center y-value that allows a pickup
PICKUP_Y_MAX = 0
## A place holder for troubleshooting etc.
ARDUINO_NULL = 0x00
## If the arduino needs to acknowledge something
ARDUINO_STATUS_ACK = 0x01
## If the arduino needs to indicate it is ready
ARDUINO_STATUS_READY = 0x02
## Report that the pick failed
ARDUINO_STATUS_PICK_FAIL = 0x03
## Report that the pick succeded
ARDUINO_STATUS_PICK_SUCCESS = 0x04
## Report a general arm failure
ARDUINO_STATUS_ARM_FAULT = 0x05
## Report an obstacle detected
ARDUINO_STATUS_OBSTACLE = 0x06
## serial command the arduino to rotate the robot, followed by one signed byte indicating magnitude and direction
ARDUINO_ROTATE = 0x10
## serial command the arduino to advance the robot, followed by one signed byte indicating magnitude and direction
ARDUINO_MOVE = 0x11
## serial command the arduino to follow the line
ARDUINO_LINE_FOLLOW = 0x12
## serial command the arduino to call the park action sequence
ARDUINO_ARM_PARK = 0x20
## serial command the arduino to call the dispose action sequence
ARDUINO_ARM_DISPOSE = 0x21
## serial command the arduino to attempt a pick, followed by three bytes: azimuth, range, and orientation
ARDUINO_ARM_PICKUP = 0x22
## Arduino pin for port motor forward
PORT_MOTOR_FWD = None
## Arduino pin for port motor reverse
PORT_MOTOR_REV = None
## Arduino pin for starboard motor forward
STBD_MOTOR_FWD = None
## Arduino pin for starboard motor reverse
STBD_MOTOR_REV = None
## Arduino pin for the port line sensor
PORT_LINE_SENSE = None
## Arduino pin for the starboard line sensor
STBD_LINE_SENSE = None
## Arduino pin for the port forward obstacle sensor
PORT_FWD_OBSTACLE = None
## Arduino pin for the port aft obstacle sensor
PORT_AFT_OBSTACLE = None
## Arduino pin for the starboard forward obstacle sensor
STBD_FWD_OBSTACLE = None
## Arduino pin for the starboard aft obstacle sensor
STBD_AFT_OBSTACLE = None
## Arduino pin for communication with the xArm
ARM_CONTROL = None
