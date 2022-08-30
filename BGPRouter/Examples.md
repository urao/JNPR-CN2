

# Single CN2 Control Node BGP Peering with Spine-01

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: BGPRouter
metadata:
  namespace: contrail
  name: vqfx-spine-01
  annotations:
    core.juniper.net/display-name: SPINE-01
    core.juniper.net/description: Represents configuration of BGP peers.
spec:
  parent:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: RoutingInstance
    namespace: contrail
    name: default
  bgpRouterParameters:
    vendor: Juniper
    routerType: router
    address: 172.16.100.1
    identifier: 172.16.100.1
    addressFamilies:
      family:
        - route-target
        - inet-vpn
        - e-vpn
  bgpRouterReferences:
    - apiVersion: core.contrail.juniper.net/v1alpha1
      kind: BGPRouter
      namespace: contrail
      name: cn2masternode
```
