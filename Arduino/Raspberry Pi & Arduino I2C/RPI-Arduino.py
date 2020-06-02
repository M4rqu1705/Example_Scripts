import smbus

bus = smbus.SMBus(1)

ADDRESS = 0x04

def write(value):
    if isinstance(value, int) and abs(value) < 256:
        bus.write_byte(ADDRESS, abs(value))

def writeString(string):
    for char in str(string):
        num = ord(char)
        write(num)
    return -1

def read():
    number = bus.read_byte(ADDRESS)
    return number

def read_available():
    try:
        result = bus.read_byte(ADDRESS)
        return result
    except OSError:
        return False

writeString("Hello World!")
number = read()
# Will just be a '!'
print(number)
