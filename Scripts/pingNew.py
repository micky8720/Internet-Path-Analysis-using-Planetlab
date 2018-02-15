import pyping
f = open('AllNodes.txt')

line = f.readline()

while line:

    print(line)
    r = pyping.ping('whitefall.planetlab.cs.umd.edu')
    if r.ret_code == 0:
        file = open('finalList.txt','a+')
        file.write(line)
        file.close()
    else:
        print("Promescent")
f.close( )




