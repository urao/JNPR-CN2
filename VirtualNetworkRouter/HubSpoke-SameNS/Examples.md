
# Hub-Spoke VNR, same Namespace
# NS, Subnet1 in VN1 Spoke1
# Subnet2, VN2 in Spoke2
# Subnet3, VN3 in Hub
# Connectivty VN3->VN1, VN3->VN2 but VN1-X->VN2

```
kubectl apply -f hs-same-ns-vnr.yml
for i in {1,2,3}; do kubectl -f pod${i}.yml; done
```

# Check connectivity 
* Add routes in each pod
* Check connectivity between Hub and Spoke pods, but not between spoke pods
