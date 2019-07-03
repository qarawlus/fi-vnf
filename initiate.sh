#!/bin/sh


brctl addbr br0
ifconfig sf-eth0 0.0.0.0 promisc
ifconfig sf-eth1 0.0.0.0 promisc
brctl addif br0 sf-eth0
brctl addif br0 sf-eth1
ifconfig br0 10.0.0.3

iptables -m physdev --physdev-in sf-eth0 -A FORWARD -j NFQUEUE --queue-num 1


#iptables -t raw -A PREROUTING -p tcp --destination-port 9001 -j NFQUEUE --queue-num 1

# iptables -t raw -A PREROUTING -p tcp --destination-port 9001 -j NFQUEUE --queue-num 1

# iptables -t nat -A POSTROUTING -o eth0-j MASQUERADE