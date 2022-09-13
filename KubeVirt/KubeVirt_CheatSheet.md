# KubeVirt Resource

```
kubectl -n kubevirt get kubevirt
kubectl get vmis -o wide -A
kubectl patch virtualmachine cirrosvm --type merge -p '{"spec":{"running":true}}'
```

```
virtctl start cirrosvm
virtctl stop cirrosvm
virtctl restart cirrosvm
virtctl migrate cirrosvm
virtctl console cirrosvm
virtctl expose vmi cirrosvm --name=cirrosvm-ssh --port=20222 --target-port=22 --type=NodePort
```
