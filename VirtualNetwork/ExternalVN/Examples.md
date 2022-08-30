# Subnets, SNAT VirtualNetwork (VNs) that can communicate with each other

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  namespace: contrail
  name: subnet3
  annotations:
    core.juniper.net/display-name: Subnet3
    core.juniper.net/description: Subnet represents a block of IP addresses and its configuration.
spec:
  cidr: "192.168.30.0/24"
  defaultGateway: "192.168.30.254"
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualNetwork
metadata:
  namespace: contrail
  name: externalvn
  annotations:
    core.juniper.net/display-name: EXTERNALVN
    core.juniper.net/description: VirtualNetwork represents.
spec:
  v4SubnetReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: Subnet
    namespace: contrail
    name: subnet3
  routeTargetList:
    - target:64512:5000
  fabricSNAT: true
---
apiVersion: v1
kind: Pod
metadata:
  name: externalvnpod1
  namespace: contrail
  annotations:
    k8s.v1.cni.cncf.io/networks: vn1
spec:
  containers:
    - name: externalvnpod1
      image: busybox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
```


* On GW VM/Node
```
Run the shell script in this folder to forward traffic from control_data port to internet facing port
Add route from the pod network to the default vrouter GW (in this case 172.16.80.1)
route add -net 192.168.30.0/24 gw 172.16.80.1
```

* Ping
```
kubectl exec -it pod/externalvnpod1 -n contrail -- ping 8.8.8.8
```
