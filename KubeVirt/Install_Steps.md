
# Install steps of KubeVirt version v0.56.0 on Ubuntu 20.04

1. Check if hardware virtualization is supported or not on the cluster
```
    * apt install libvirt-clients
    * virt-host-validate qemu
```

2. If hardware virtualization is not supported, enable emulations in the kubevirt-cr yaml and deploy it.

3. Check for the manifest files with the configuration

4. During KubeVirt deploy, enable features like DataVolumes and LiveMigration using 
   featureGates option under spec.configuration

5. Run below deployment commands
```
kubectl apply -f kubevirt-operator.yaml
kubectl apply -f kubevirt-cr.yaml
```

6. Install virtctl client tool to manage VirtualMachineInstance operations
```
export VERSION=v0.41.0
wget https://github.com/kubevirt/kubevirt/releases/download/${VERSION}/virtctl-${VERSION}-linux-amd64
mv virtctl-${VERSION}-linux-amd64 virtctl
chmod +x virtctl
mv virtctl /usr/local/bin
```

7. Below is the steps to install containerized-data-importer(CDI)
```
export VERSION=$(curl -s https://api.github.com/repos/kubevirt/containerized-data-importer/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
kubectl create -f https://github.com/kubevirt/containerized-data-importer/releases/download/$VERSION/cdi-operator.yaml
kubectl create -f https://github.com/kubevirt/containerized-data-importer/releases/download/$VERSION/cdi-cr.yaml

```




### References
https://kubevirt.io

https://kubevirt.io/user-guide/operations/virtctl_client_tool/

https://github.com/kubevirt/containerized-data-importer

