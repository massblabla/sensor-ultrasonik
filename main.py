jarak = 0

def on_forever():
    global jarak
    jarak = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(jarak)
    basic.pause(500)
basic.forever(on_forever)
