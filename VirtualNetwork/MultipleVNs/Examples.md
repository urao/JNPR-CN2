

# Subnets, VirtualNetwork (VNs) traffic between 2 VNs using RTs

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  namespace: contrail
  name: subnet1
  annotations:
    core.juniper.net/display-name: Subnet1
    core.juniper.net/description: Subnet represents a block of IP addresses and its configuration.
spec:
  cidr: "192.168.10.0/24"
  defaultGateway: "192.168.10.1"
  ranges:
  - key: key1
    ipRanges:
      - from: "192.168.10.2"
        to: "192.168.10.100"
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetwork
metadata:
  namespace: contrail
  name: vn1
  annotations:
    core.juniper.net/display-name: VN1
    core.juniper.net/description: VirtualNetwork represents.
spec:
  v4SubnetReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: Subnet
    namespace: contrail
    name: subnet1
  routeTargetList:
    - target:64512:1000
  fabricSNAT: false
  fabricForwarding: false
  virtualNetworkProperties:
    forwardingMode: "l2_l3"
---
apiVersion: v1
kind: Pod
metadata:
  name: testvn1pod1
  namespace: contrail
  annotations:
    k8s.v1.cni.cncf.io/networks: vn1
spec:
  containers:
    - name: testvn1pod1
      image: toolbox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  namespace: contrail
  name: subnet2
  annotations:
    core.juniper.net/display-name: Subnet1
    core.juniper.net/description: Subnet represents a block of IP addresses and its configuration.
spec:
  cidr: "192.168.20.0/24"
  defaultGateway: "192.168.20.1"
  ranges:
  - key: key1
    ipRanges:
      - from: "192.168.20.2"
        to: "192.168.20.100"
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetwork
metadata:
  namespace: contrail
  name: vn2
  annotations:
    core.juniper.net/display-name: VN2
    core.juniper.net/description: VirtualNetwork represents.
spec:
  v4SubnetReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: Subnet
    namespace: contrail
    name: subnet2
  routeTargetList:
    - target:64512:1000
  fabricSNAT: false
  fabricForwarding: false
  virtualNetworkProperties:
    forwardingMode: "l2_l3"
---
apiVersion: v1
kind: Pod
metadata:
  name: testvn2pod1
  namespace: contrail
  annotations:
    k8s.v1.cni.cncf.io/networks: vn2
spec:
  containers:
    - name: testvn2pod1
      image: toolbox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
```

```
kubectl exec testvn1pod1 -- ip route add 192.20.0.0/24 via 192.10.0.1
kubectl exec testvn2pod1 -- ip route add 192.10.0.0/24 via 192.20.0.1
```

* Ping
```
kubectl exec testvn1pod1 -- ping 192.168.20.3
kubectl exec testvn2pod1 -- ping 192.168.10.3
```
