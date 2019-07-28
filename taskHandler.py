#!/usr/bin/python
import sys, getopt, time, requests
from pathPlanning import planPath
def main(argv):
    ngrokServer=""
    argument = ''
    usage = 'usage: script.py -f <sometext>'
    basePosition= (0,0)
    # parse incoming arguments
    try:
        opts, args = getopt.getopt(argv,"hf:",["customer=","vendor=","server="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("--server"):
            ngrokServer= arg
        elif opt in ("--customer"):
            customerPosition= arg
        elif opt in ("--vendor"):
            vendorPosition= arg
    # print output
    # print("Start : %s" % time.ctime())
    print('Base position is', basePosition)
    print('Customer position is', customerPosition)
    print('Vendor position is', vendorPosition)
    # print("End : %s" % time.ctime())
    # RUN PATH PLANNING THRE TIMES
    path1= planPath(basePosition, vendorPosition)
    # SEND RES TO SERVER
    r = requests.post(ngrokServer, data={'path1': [[[0,0],0], [[1.65,0],1], [[2.3,-0.55],0], [[2.3,-1.65],0]] })

if __name__ == "__main__":
    main(sys.argv[1:])