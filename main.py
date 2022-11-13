speed = 0
new_speed = 0

def on_pin_pressed_p0():
    global speed, new_speed
    led.set_brightness(245)
    for index in range(1000):
        speed = 0
        new_speed = 0
        speed = input.acceleration(Dimension.X)
        basic.pause(500)
        new_speed = input.acceleration(Dimension.X) * 0.5 + speed
        basic.show_number(new_speed)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global speed, new_speed
    control.reset()
    for index2 in range(20):
        led.set_brightness(255)
        speed = input.acceleration(Dimension.X)
        basic.pause(100)
        new_speed = input.acceleration(Dimension.X) * 0.1 + speed
        basic.show_number(new_speed)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
