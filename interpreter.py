# TODO: important! this script doesn't handle time after 24:00 (e.g. 12:05 am, 2:45 am), which requires MANUAL insertion

import sys

# env vars
campus = 1 # bmc 0, hc 1
day = 0 # start from Sun

fin = open("in-day" + str(day) + ".txt", "r")
fout = open("out-day" + str(day) + "campus" + str(campus) + ".txt", "w")

for line in fin:
    line = line.replace("\t", "").replace("\n", "")
    element = line.split(",")[campus]

    # hour
    hr = int(element.split(":")[0].split(" ")[0])
    if "p.m" in element and not hr == 12:
        hr += 12

    # min
    min = 0
    temp = element.split(":")
    if len(temp) > 1:
        min = int(temp[1].split(" ")[0])

    # timestamp
    timestamp = 24*60*day + 60*hr + min

    # output
    out = "{\n\tday: " + str(day) + \
          ",\n\thour: " + str(hr) + \
          ",\n\tminute: " + str(min) + \
          ",\n\ttimestamp: " + str(timestamp) + \
          ",\n},"
    print(out, file=fout)

fin.close()
fout.close()