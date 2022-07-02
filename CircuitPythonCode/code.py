import time
import board
import busio
import adafruit_mcp9600
from adafruit_motorkit import MotorKit

i2c = busio.I2C(board.SCL, board.SDA, frequency=20000)
mcp = adafruit_mcp9600.MCP9600(i2c, address=0x60)  # sparkfun default address is 60
kit = MotorKit(i2c=i2c, address=112) # hex 70 is int 112


while True:
    print(f"Temperature at probe: {mcp.temperature}")
    print("Motor on")
    kit.motor1.throttle = 1.0
    time.sleep(2)
    print("Motor Off")
    kit.motor1.throttle = 0
    time.sleep(1) 