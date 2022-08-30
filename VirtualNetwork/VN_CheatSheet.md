# VirtualNetwork Resource

* As part of CN2 default Subnet/VirtualNetworks is created for every Cluster, below commands can be used to verify
* Also you can create new subnets/virtualnetworks shown in the examples 

```
kubectl get subnet -A
kubectl describe subnet default-podnetwork-pod-v4-subnet -n contrail-k8s-kubemanager-cn2-cluster-local-contrail
kubectl get vn -A
kubectl describe -n contrail vn/ip-fabric
```

Below command will explain different fields available for this resource
```
kubectl explain subnet.spec --recursive
kubectl explain vn.spec --recursive
kubectl explain vn.spec.providerNetworkReference
kubectl explain vn.spec.virtualNetworkProperties
```

Debug commands same as classic contrail via introspect
```
```
