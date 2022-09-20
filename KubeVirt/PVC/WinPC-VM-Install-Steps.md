
### Deploy Windows VM using PVCs

1. Run below command to upload image on to the PVC
```
kubectl apply -f local-storage.yml
virtctl image-upload pvc windows-pvc --size=45Gi --image-path=/root/cdi/tests/22000.318.211104-1236.co_release_svc_refresh_CLIENTENTERPRISEEVAL_OEMRET_x64FRE_en-us.iso --storage-class=local-storage --access-mode=ReadWriteOnce --uploadproxy-url=https://<CDI_UPLOADER_SVC_IP>:443 --insecure
```
2. Run the manifest file to create VM
```
kubectl apply -f windows-vm-pvc.yml
```
3. Verify the VM is created
```
kubectl get vmis -A -o wide
```
