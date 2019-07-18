# -*- coding: utf-8 -*-
import ipaddress

net = ipaddress.ip_network("123.45.67.64/27")
print(net, type(net), net.num_addresses)

count = -1
for i in net:
    count += 1
    if not count % 5:
        print()
    print(i, end='***')

count = -1
net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
print(net6, type(net6), net6.num_addresses)

for i in net6:
    count += 1
    if not count % 5:
        print()
    print(i, end='***')
