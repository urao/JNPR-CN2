
# Mesh VNR, same Namespace
# NS, Subnet1, Subnet2, VN1, VN2 and VNR 

```
---
apiVersion: v1
kind: Namespace
metadata:
  name: same-ns-mesh
  labels:
    ns: same-ns-mesh
spec:
  finalizers:
  - kubernetes
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  namespace: same-ns-mesh
  name: subnet1-mesh
  annotations:
    core.juniper.net/display-name: Subnet1Mesh
    core.juniper.net/description: Subnet represents a block of IP addresses and its configuration.
spec:
  cidr: "172.168.10.0/24"
  defaultGateway: "172.168.10.254"
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  namespace: same-ns-mesh
  name: subnet2-mesh
  annotations:
    core.juniper.net/display-name: Subnet2Mesh
    core.juniper.net/description: Subnet represents a block of IP addresses and its configuration.
spec:
  cidr: "172.168.20.0/24"
  defaultGateway: "172.168.20.254"
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetwork
metadata:
  namespace: same-ns-mesh
  name: vn1-smesh
  annotations:
    core.juniper.net/display-name: VN1-smesh
    core.juniper.net/description: VirtualNetwork represents.
  labels:
    vn: linux
spec:
  v4SubnetReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: Subnet
    namespace: same-ns-mesh
    name: subnet1-mesh
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetwork
metadata:
  namespace: same-ns-mesh
  name: vn2-smesh
  annotations:
    core.juniper.net/display-name: VN2-smesh
    core.juniper.net/description: VirtualNetwork represents.
  labels:
    vn: linux
spec:
  v4SubnetReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: Subnet
    namespace: same-ns-mesh
    name: subnet2-mesh
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetworkRouter
metadata:
  namespace: same-ns-mesh
  name: vnr01
  annotations:
    core.juniper.net/display-name: vnr01
  labels:
      vnr: linux
spec:
  type: mesh
  virtualNetworkSelector:
    matchLabels:
      vn: linux

```
* Pods creation

```
---
apiVersion: v1
kind: Pod
metadata:
  name: testvn1pod1
  namespace: same-ns-mesh
  annotations:
    k8s.v1.cni.cncf.io/networks: vn1-smesh
spec:
  containers:
    - name: testvn1pod1
      image: busybox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
---
apiVersion: v1
kind: Pod
metadata:
  name: testvn2pod1
  namespace: same-ns-mesh
  annotations:
    k8s.v1.cni.cncf.io/networks: vn2-smesh
spec:
  containers:
    - name: testvn2pod1
      image: busybox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
```

* Check connectivity between VN1 and VN2

```
kubectl exec -it pod/testvn2pod1 -n same-ns-mesh -- ip route add 172.168.10.0/24 via 172.168.20.254
kubectl exec -it pod/testvn1pod1 -n same-ns-mesh -- ip route add 172.168.20.0/24 via 172.168.10.254
kubectl exec -it pod/testvn1pod1 -n same-ns-mesh -- ping 172.168.20.1
```
