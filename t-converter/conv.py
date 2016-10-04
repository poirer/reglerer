import sys

def convertToFahrenheit(t):
    return t * 9 / 5 + 32

def convertToCelsius(t):
    return (t - 32) * 5 / 9

if len(sys.argv) > 1 :
    t = sys.argv[1]
else:
    t = input("Enter temperature ")
if len(sys.argv) > 2:
    d = sys.argv[2]
else:
    d = input("What is target scale ")
t = float(t)
if d == "F":
    f = convertToFahrenheit(t)
elif d == "C":
    f = convertToCelsius(t)
else:
    raise "Invalid or unsupported temperature scale"
print("Temperaturn is %.1f" % f, " degrees %s" % d)
