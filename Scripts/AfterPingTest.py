import sys
import os
import subprocess as sp
from subprocess import Popen, PIPE, STDOUT
from time import sleep
from os import waitpid, execv, read, write
array = []
index = 0
COMMAND="uptime"
host="albany_ccn9"
with open("first.txt", "r") as f:
  for line in f:
    array.append(line.strip())
    ip = array[index]
    hostname = "albany_ccn9"
    st = hostname+"@"+ip
    print(st)
    ss = sp.Popen(['ssh', st ,  COMMAND],
                       stdin=sp.PIPE,
                       stdout=sp.PIPE,
                       stderr=sp.PIPE)
    result = ss.stdout.readlines()

    if result == []:
        error = ss.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print(result)
        print("reachable  :: " + array[index])
        with open('finalList.txt', 'a+') as f:
            print(result[0])
            f.write(array[index])
            f.write(result[0])
            f.write("\n")
        print (result)
    index += 1;