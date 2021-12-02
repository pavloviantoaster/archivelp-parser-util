

def convert_ticks(ticks):
    sec = int((ticks / 1000) % 60)
    min = int((ticks / 1000) / 60)
    frames = int((ticks % 1000) * 0.076)
    #print('{0:02d}'.format(min) + ":" + '{0:02d}'.format(sec) + ":" + '{0:02d}'.format(frames))
    return str('{0:02d}'.format(min) + ":" + '{0:02d}'.format(sec) + ":" + '{0:02d}'.format(frames))




while 1:
    ticks = int(input("Enter value: "))
    print(convert_ticks(ticks))