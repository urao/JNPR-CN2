#!/bin/bash

LANIF='ens3f1'
WANIF='ens3f0'

echo 'Enabling ip forwarding in the kernel'
echo 1 > /proc/sys/net/ipv4/ip_forward

echo 'Flush rules and deleting existing chains..'
iptables -F
iptables -X

echo 'Enabling forward and masquerading to all ens3f1 to ens3f0 interface for data traffic'
iptables --tables nat --append POSTROUTING --out-interface $WANIF -j MASQUERADE
iptables --append FORWARD --in-interface $LANIF -j ACCEPT

echo 'Done.'
echo '\n'
