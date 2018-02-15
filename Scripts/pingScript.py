
f = open('AllNodes.txt')

line = f.readline()
import os

while line:
    line = f.readline()
    print(line)


    hostname = line
    response = os.system("ping -c 1 -w2" + hostname)

    if response == 0:
        print
        hostname, ' successful!'
    else:
        print
        hostname, 'not successful'
f.close()




