s_prawy = 0
s_lewy = 0
music.play_tone(262, music.beat(BeatFraction.EIGHTH))
SILA = 50
MALA_SILA = SILA / 2

def on_forever():
    global s_lewy, s_prawy
    s_lewy = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
    s_prawy = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)
    if s_lewy == 0 and s_prawy == 0:
        maqueen.motor_stop(maqueen.Motors.ALL)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    elif s_prawy == 0:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, MALA_SILA)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, SILA)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    elif s_lewy == 0:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, SILA)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, MALA_SILA)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, SILA)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
basic.forever(on_forever)
