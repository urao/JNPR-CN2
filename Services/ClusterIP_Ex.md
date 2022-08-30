# Service creation using service type ClusterIP
```
---
apiVersion: v1
kind: Namespace
metadata:
  name: svc-ns
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  namespace: svc-ns
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
  namespace: svc-ns
spec:
  ports:
  - name: http
    port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: nginx
  type: ClusterIP
```
* Check connectivity using curl <cluster_ip>:30777
