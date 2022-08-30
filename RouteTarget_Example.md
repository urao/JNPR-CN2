
# Creation of the RouteTarget - CN2

```
---
apiVersion: core.contrail.juniper.net/v1alpha1
kind: RouteTarget
metadata:
  name: target-65412-7000
  annotations:
    core.juniper.net/display-name: RouteTarget
    core.juniper.net/description: A route-target extended community, or route target
```

* Debug Commands
```
k get rt
k describe rt/target-65412-7000
k explain rt.spec --recursive
```
