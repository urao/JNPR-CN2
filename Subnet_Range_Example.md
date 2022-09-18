
# Creation of the Subnet with IP Range - CN2

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: Subnet
metadata:
  name: subnet-v4-001
  namespace: subnet-test
  annotations:
    core.juniper.net/display-name: subnet-v4-rang
spec:
  cidr: 192.168.0.0/16
  defaultGateway: 192.168.0.1
  ranges:
  - ipRanges:
    - from: 192.168.0.10
      to: 192.168.0.250

```

* Debug Commands
```
kubectl get subnets
kubectl get sn
kubectl describe sn/subnet-v4-001
kubectl explain sn.spec --recursive
kubectl get instanceips -A | grep <podName>
kubectl get vmi -A
kubectl get pods -A | grep contrail-k8s-controller
kubetl logs <podName> -n <namespace>
```
