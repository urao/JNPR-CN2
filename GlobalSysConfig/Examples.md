

# Modify AS #, ASN bytes in GlobalSystemConfig

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: default-global-system-config
metadata:
  namespace: contrail
  name: vqfx-spine-01
  annotations:
    core.juniper.net/display-name: Default Global System Config
    core.juniper.net/description: Represents all global configuration for the contrail.
spec:
  enable4bytesAS: false
  autonomousSystem: 65333
  bgpRouterReferences:
    - apiVersion: core.contrail.juniper.net/v1alpha1
      kind: BGPRouter
      namespace: contrail
      name: cn2masternode
```
