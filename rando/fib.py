vala = 0
valb = 1
valc = 0

loops = 0

while loops < 100:
    valc = (vala + valb)
    print(valc)
    vala = valb
    valb = valc
    loops += 1

