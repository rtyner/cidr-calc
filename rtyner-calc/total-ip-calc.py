import sys
import netaddr
from netaddr import IPNetwork

in_file = sys.argv[1]

with open(in_file,'r') as i:
    lines = i.readlines()
    for line in lines:
        ip = IPNetwork(line)
        x += ip.size
        
        
# testing some shit here
        #ip_size = []
        #ip_size.append(ip.size)
        #print(ip_size)
        #sum(ip_size)
       # ip_size = sum(ip_count)
       # print(ip_size)