
# Mesh VNR, same Namespace
# NS1, Subnet1, Subnet2, VN1, VN2 and VNR1
# NS2, Subnet3, Subnet4, VN3, VN4 and VNR2 

* Configuration is same Multi-MeshVNR-SameNS only different in the VNR configuration
* as below

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetworkRouter
metadata:
  namespace: ns1-mmesh
  name: ns1-mvnr01
  annotations:
    core.juniper.net/display-name: ns1-mvnr01
  labels:
      vnr: web
spec:
  type: mesh
  virtualNetworkSelector:
    matchLabels:
      vn: web
  import:
    virtualNetworkRouters:
      - virtualNetworkRouterSelector:
          matchLabels:
            vnr: db
        namespaceSelector:
          matchLabels:
            ns: ns2-mmesh
```

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetworkRouter
metadata:
  namespace: ns2-mmesh
  name: ns2-mvnr01
  annotations:
    core.juniper.net/display-name: ns2-mvnr01
  labels:
      vnr: db
spec:
  type: mesh
  virtualNetworkSelector:
    matchLabels:
      vn: db
  import:
    virtualNetworkRouters:
      - virtualNetworkRouterSelector:
          matchLabels:
            vnr: web
        namespaceSelector:
          matchLabels:
            ns: ns1-mmesh
```

* Add routes in each of pod
* Check connectivity between pods in VN1, VN2, VN3 and VN4
