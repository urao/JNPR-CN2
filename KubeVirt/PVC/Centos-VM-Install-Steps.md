
### Deploy VM using PVCs

1. Run below command to upload image on to the PVC
```
kubectl apply -f local-storage.yml
virtctl image-upload pvc centos-pvc --size=15Gi --image-path=/root/cdi/tests/CentOS-7-x86_64-GenericCloud.qcow2 --storage-class=local-storage --access-mode=ReadWriteOnce --uploadproxy-url=https://<CDI_UPLOADER_SVC_IP>:443 --insecure
```
2. Run the manifest file to create VM
```
kubectl apply -f centos-vm.yml
```
3. Verify the VM is created
```
kubectl get vmis -A -o wide
```
