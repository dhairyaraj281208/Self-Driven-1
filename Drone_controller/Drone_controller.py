from controller import Robot, Keyboard

robot = Robot()
keyboard = Keyboard()

timestep = 64


imu= robot.getDevice("inertial unit")
imu.enable(timestep)

f_l = robot.getDevice("front left propeller")
f_r = robot.getDevice("front right propeller")
r_l = robot.getDevice("rear left propeller")
r_r = robot.getDevice("rear right propeller")

f_l.setPosition(float('inf'))
f_l.setVelocity(576)
f_r.setPosition(float('inf'))
f_r.setVelocity(576)
r_l.setPosition(float('inf'))
r_l.setVelocity(576)
r_r.setPosition(float('inf'))
r_r.setVelocity(576)

keyboard.enable(timestep)



while robot.step(timestep) != -1:
    key_pressed= keyboard.getKey()
    print(key_pressed)

    if(key_pressed == 87):
        f_l.setVelocity(500)
        f_r.setVelocity(500)

