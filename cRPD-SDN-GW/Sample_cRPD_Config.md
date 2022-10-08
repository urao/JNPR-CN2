### Sample cRPD configuration of iBGP peering with CN2 control node

```
set policy-options policy-statement lb then load-balance per-packet
set routing-instances vn1_ri instance-type vrf
set routing-instances vn1_ri vrf-target target:64512:1000
set routing-instances vn1_ri vrf-table-label
set routing-instances vn2_ri instance-type vrf
set routing-instances vn2_ri vrf-target target:64512:2000
set routing-instances vn2_ri vrf-table-label
set routing-options route-distinguisher-id 1.1.1.11
set routing-options resolution rib bgp.rtarget.0 resolution-ribs inet.0
set routing-options resolution rib bgp.l3vpn.0 resolution-ribs inet.3
set routing-options resolution rib bgp.l3vpn.0 resolution-ribs inet.0
set routing-options resolution rib bgp.evpn.0 resolution-ribs inet.0
set routing-options router-id 1.1.1.11
set routing-options autonomous-system 64512
set routing-options static route 0.0.0.0/0 next-hop 192.16.80.1
set routing-options dynamic-tunnels contrail_gre source-address 1.1.1.11
set routing-options dynamic-tunnels contrail_gre gre
set routing-options dynamic-tunnels contrail_gre destination-networks 172.16.80.0/24
set routing-options forwarding-table export lb
set protocols bgp group contrail_gw type internal
set protocols bgp group contrail_gw local-address 1.1.1.11
set protocols bgp group contrail_gw hold-time 90
set protocols bgp group contrail_gw keep all
set protocols bgp group contrail_gw log-updown
set protocols bgp group contrail_gw family inet-vpn unicast
set protocols bgp group contrail_gw family evpn signaling
set protocols bgp group contrail_gw family route-target
set protocols bgp group contrail_gw local-as 64512
set protocols bgp group contrail_gw multipath
set protocols bgp group contrail_gw neighbor 172.16.80.5 peer-as 64512
set protocols bgp group contrail_gw vpn-apply-export
```
