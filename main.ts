let speed = 0
let new_speed = 0
input.onPinPressed(TouchPin.P0, function () {
    led.setBrightness(245)
    for (let index = 0; index < 1000; index++) {
        speed = 0
        new_speed = 0
        speed = input.acceleration(Dimension.X)
        basic.pause(500)
        new_speed = input.acceleration(Dimension.X) * 0.5 + speed
        basic.showNumber(new_speed)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    control.reset()
    for (let index = 0; index < 20; index++) {
        led.setBrightness(255)
        speed = input.acceleration(Dimension.X)
        basic.pause(100)
        new_speed = input.acceleration(Dimension.X) * 0.1 + speed
        basic.showNumber(new_speed)
    }
})
