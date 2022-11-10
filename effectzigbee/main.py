import serial


def init():
    return serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )


def ledColor(r, g, b):
    ser = init()
    ser.write(str.encode("led=" + str(r) + "," + str(g) + "," + str(b) + "\n"))
    ser.close()
