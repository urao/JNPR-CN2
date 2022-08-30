

# Subnets, VirtualNetwork (VNs) is a collection of EPs (VMI, IPs, MACs) that can communicate with each other

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
```
