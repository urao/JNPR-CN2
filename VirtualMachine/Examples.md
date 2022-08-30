

# VirtualMachine, VMIs 

```
cat > aap.yaml <<EOF
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: allowedAddressPairs
metadata:
  name: aap01
  annotations:
    core.juniper.net/display-name: AAP01
    core.juniper.net/description: AllowedAddressPair testing 
spec:
  allowedAddressPair: 
    - addressMode: "active-standby"
      ip:
        ipPrefix: "192.168.10.10"
        ipPrefixLen: "32"
      mac: "00:01:02:03:04:05"
EOF
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualMachine
metadata:
  name: virtualmachine01
  annotations:
    core.juniper.net/display-name: VIRTUALMACHINE01
    core.juniper.net/description: VM represents the compute container
spec:
  serverType: container
  serverName: default-pod
  serverNamespace: default-ns
  serverClusterName: default-cluster
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: VirtualMachineInterface
metadata:
  namespace: contrail
  name: vmi01
  annotations:
    core.juniper.net/display-name: VMI01
    core.juniper.net/description: VirtualMachine Interface.
spec:
  virtualMachineInterfaceMacAddresses:
    macAddress: 
      - 00:11:22:55:66:33
  virtualNetworkReference:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: VirtualNetwork
    namespace: contrail
    name: vn1
  virtualMachineReference:
    - apiVersion: core.contrail.juniper.net/v1alpha1
      kind: VirtualMachine
      name: virtualmachine01
```
* Patch AllowedAddressPair to VMI

```
kubectl patch --namespace default-ns VirtualMachineInterface vmi01 -p "$(cat ./aap.yaml)" 
```
