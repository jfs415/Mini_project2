#JON HEALY
#MINI_PROJECT2
#FILTER_PACKETS.PY
#FILTERES PACKETS FROM THE 5 NODES TO ONLY INCLUDE ICMP ECHO REQUEST/REPLY
#WRITES THE FILTERED PACKETS TO CORESSPONDING NODE OUTPUT FILES

import sys

#Files to read from
ex = "example.txt"
node1 = "Node1.txt"
node2 = "Node2.txt"
node3 = "Node3.txt"
node4 = "Node4.txt"
node5 = "Node5.txt"

#Filtered files
newex = "filtered_example.txt"
newNode1 = "filtered_node1.txt"
newNode2 = "filtered_node2.txt"
newNode3 = "filtered_node3.txt"
newNode4 = "filtered_node4.txt"
newNode5 = "filtered_node5.txt"

def read(file, file2):

    #Basic file IO
    f = open(file, 'r')
    fw = open(file2, 'a')
    line = f.readline()
    header = line # The header line of the packets
    fw.write(header)

    while line:
        line = f.readline()
        if 'Echo (ping) request' in line:
            fw.write(line)
            while line != header:
                line = f.readline()
                fw.write(line)

                #Break loop at EOF
                if not line:
                    break
                
        elif 'Echo (ping) reply' in line:
            fw.write(line)
            while line != header:
                line = f.readline()
                fw.write(line)

                #Break loop at EOF
                if not line:
                    break
    #File cleanup
    f.close()
    fw.close()

def filter():
    #read(ex, newex)
    read(node1, newNode1)
    print("Completed node 1")
    read(node2, newNode2)
    print("Completed node 2")
    read(node3, newNode3)
    print("Completed node 3")
    read(node4, newNode4)
    print("Completed node 4")
    read(node5, newNode5)
    print("Completed node 5")

filter()
