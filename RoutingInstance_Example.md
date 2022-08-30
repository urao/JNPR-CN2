
# Creation of the RouteInstance - CN2

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: RouteTarget
metadata:
  name: target-65412-7000
  annotations:
    core.juniper.net/display-name: RouteTarget
    core.juniper.net/description: A route-target extended community, or route target
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: RoutingInstance
metadata:
  name: RI01
  namespace: contrail
  annotations:
    core.juniper.net/display-name: RI01
    core.juniper.net/description: A routingInstance from the IP network
spec:
  parent: RI01
    apiVersion: contrail
    kind: VirtualNetwork
    namespace: contrail
    name: VN01
  routeTargetReferences:
     - apiVersion: core.contrail.juniper.net/v1alpha1
       kind: RouteTarget
       name: target-65412-7000
```

* Debug Commands
```
kubectl get ri -A
kubectl describe ri/ip-fabric -n contrail
kubectl explain ri.spec --recursive
```
