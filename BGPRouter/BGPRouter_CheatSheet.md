# BGPRouter Resource

* As part of CN2 a BGPRouter is created for every ControlNode, below commands can be used to verify

```
kubectl get bgprouters -A
kubectl describe -n contrail bgprouter/cn2masternode
```
Below command will explain different fields available for this resource

```
kubectl explain bgprouter.spec.bgpRouterParameters
kubectl explain bgprouter.spec.bgpRouterReferences.attributes.session.sessionAttributes
```
Debug commands same as classic contrail via introspect

```
http://<ctrl_data_port>:8083/Snh_ShowBgpNeighborSummaryReq?search_string=
http://<ctrl_data_port>:8083/Snh_IFMapNodeTableListShowReq?
tcpdump -vvvv -ni vhost0 port 179 and host 10.88.14.101
```
