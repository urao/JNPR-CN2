# VNR Resource

* As part of CN2 a default VNRs is created for every ControlNode, below commands can be used to verify

```
kubectl get vnr -A
kubectl describe -n contrail vnr/DefaultIPFabricNetwork
kubectl get vn -A
kubectl get ri -A
```

Below command will explain different fields available for this resource
```
kubectl explain vnr.spec
```

Debug commands same as classic contrail via introspect
```
```
