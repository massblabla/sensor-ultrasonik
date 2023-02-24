let jarak = 0
basic.forever(function () {
    jarak = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    basic.showNumber(jarak)
    basic.pause(500)
})
