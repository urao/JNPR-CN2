

# Global Vrouter configuration for the cluster

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: GlobalVrouterConfig
metadata:
  name: default-global-vrouter-config
  annotations:
    core.juniper.net/display-name: Default Global Vrouter Configuration
    core.juniper.net/description: Represents global vrouter configuration for the cluster.
spec:
  parent:
    apiVersion: core.contrail.juniper.net/v1alpha1
    kind: GlobalVrouterConfig
    name: default-global-vrouter-config
  encapsulationPriorities:
    encapsulation: 
      - MPLSoUDP
      - MPLSoGRE
      - VXLAN
  linklocalServices:
    linklocalServiceEntry:
      - ipFabricServiceIP:
        - 192.168.0.16
        ipFabricServicePort: 6443
        linklocalServiceIP: 10.96.0.1
        linklocalServiceName: kubernetes
        linklocalServicePort: 443
  portTranslationPools:
    pools:
      - portRange:
          startPort: 56000
          endPort:   57023
        protocol: tcp
      - portRange:
          startPort: 57024
          endPort:   58047
        protocol: udp
  flowExportRate : 1000
```
