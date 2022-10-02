## Service creation using service type LoadBalancer
```
---
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: lb-external-vn
  annotations:
    juniper.net/networks: '{
        "ipamV4Subnet": "172.16.80.32/27",
        "fabricSNAT": false,
        "importRouteTargetList" : ["target:64512:10000"],
        "exportRouteTargetList" : ["target:64512:10001"]
    }'
  namespace: contrail-k8s-kubemanager-cn2-cluster-local-contrail
  #namespace: contrail
  labels:
    service.contrail.juniper.net/externalNetworkSelector: "default-external"
spec:
  config: '{
    "cniVersion": "0.3.1",
    "type": "contrail-k8s-cni"
  }'
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginxc
        image: nginx
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
  - name: http
    port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: nginx
  type: LoadBalancer
```


```
root@cn2masternode:~/clusterip# k get svc
NAME         TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)          AGE
kubernetes   ClusterIP      10.233.0.1    <none>         443/TCP          22d
nginx-svc    LoadBalancer   10.233.3.50   172.16.80.34   8080:30110/TCP   11m
```

* Check connectivity using curl <172.16.80.34>:8080
