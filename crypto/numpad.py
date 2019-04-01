numpad = {}
numpad["1"] = ""
numpad["2"] = "ABC"
numpad["3"] = "DEF"
numpad["4"] = "GHI"
numpad["5"] = "JKL"
numpad["6"] = "MNO"
numpad["7"] = "PQRS"
numpad["8"] = "TUV"
numpad["9"] = "WXYZ"
numpad["0"] = " "
numpad["*"] = "+"

def decode(taps):
    punches = taps.split("-")
    flag = ""
    for punch in punches:
        key = punch[0]
        times = len(punch)-1
        flag += numpad[key][times]
    print(flag)

if __name__ == "__main__":
    keys_pressed = "222-8-333-0-8-666-666-555"
    decode(keys_pressed)