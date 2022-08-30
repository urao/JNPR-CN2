

# Isolated NS, Pod creation in default Pod Network 
# During NS creation, you can enable Fabric forwarding or SNAT

```
---
apiVersion: v1
kind: Namespace
metadata:
  name: ns-isolated
  labels:
    core.juniper.net/isolated-namespace: "true"

---
apiVersion: v1
kind: Pod
metadata:
  name: isolatedpod02
  namespace: ns-isolated
spec:
  containers:
    - name: isolatedpod02
      image: busybox
      imagePullPolicy: IfNotPresent
      command: ["bash", "-c","while true; do sleep 60s; done"]
      securityContext:
        privileged: true
        capabilities:
          add:
            - NET_ADMIN
```


```

```
