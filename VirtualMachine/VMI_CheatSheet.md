# VirtualNetwork Resource

* As part of CN2 default VM/VMIs is created for every Cluster, below commands can be used to verify

```
kubectl get vm
kubectl get vmi
kubectl describe vmi/webserver-5371c518
```

Below command will explain different fields available for this resource
```
kubectl explain vm
kubectl explain vm.spec --recursive
kubectl explain vmi
kubectl explain vmi.spec --recursive
kubectl explain vmi.spec.allowedAddressPairs --recursive
```

Debug commands same as classic contrail via introspect
```
```
