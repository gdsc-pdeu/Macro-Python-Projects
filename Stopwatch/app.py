import time

h, m, s = 0, 0, 0
while True:
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0

    time.sleep(1)
    print(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2),end = "\r")
