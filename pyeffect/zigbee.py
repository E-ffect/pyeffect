import serial


def init():
    return serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )


def changePedalLedColor(target, r, g, b):
    request = (
        "["
        + str(target)
        + "]_[BRIDGE]_LIGHTCHANGE_{"
        + str(r)
        + ","
        + str(g)
        + ","
        + str(b)
        + "}"
    )

    ser = init()
    ser.write(str.encode(request + "\n"))
    ser.close()


def pingPedal(target):
    request = "[" + str(target) + "]_[BRIDGE]_PING_{}"

    ser = init()
    ser.write(str.encode(request + "\n"))
    ser.close()
