
# Mesh VNR, same Namespace
# NS, Subnet1, Subnet2, VN1, VN2 and VNR1
# Subnet3, Subnet4, VN3, VN4 and VNR2

```
kubectl apply -f multi-mesh-same-ns-vnr1.yml
kubectl apply -f multi-mesh-same-ns-vnr2.yml
for i {1..4}; do kubectl apply -f podvn{i}.yml; done
```
* Configure routes on each pod
* Verify connectivity between the pods
