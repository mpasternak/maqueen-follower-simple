music.playTone(262, music.beat(BeatFraction.Eighth))
let SILA = 50
let MALA_SILA = Math.idiv(SILA, 2)
let s_lewy = 0
let s_prawy = 0
basic.forever(function on_forever() {
    
    s_lewy = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)
    s_prawy = maqueen.readPatrol(maqueen.Patrol.PatrolRight)
    if (s_lewy == 0 && s_prawy == 0) {
        maqueen.motorStop(maqueen.Motors.All)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    } else if (s_prawy == 0) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, MALA_SILA)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, SILA)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    } else if (s_lewy == 0) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, SILA)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, MALA_SILA)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, SILA)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    }
    
})
