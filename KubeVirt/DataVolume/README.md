
### Deploy VirtualMachines using DataVolume

1. Install Apache2 or any other webserver 
2. Copy image in /var/www/html/download folder
3. Run below manifest files to create VM
```
kubectl apply -f dv-pv.yml
kubectl apply -f upload-centos-dv.yml
kubectl apply -f centos-vm-dv.yml
```

4. Verify the VM is created
```
kubectl get dv
kubectl get vmis
```
