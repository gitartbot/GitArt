import time
import os
import array

colors = array('i', [0, 1, 4, 6, 10])
day = int(time.strftime("%j"))

for i in range(0, colors[day % len(colors)]):
    os.system('echo "." >> README.md')
    