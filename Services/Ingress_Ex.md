# Service creation using service type Ingress controller

* Deploy nginx ingress controller

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.1/deploy/static/provider/cloud/deploy.yaml
```

```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nserver1-deploy
spec:
  selector:
    matchLabels:
      app: nserver1
  replicas: 3
  template:
    metadata:
      labels:
        app: nserver1
    spec:
      containers:
      - name: server1
        #image: svl-artifactory.juniper.net/atom_virtual_docker/nginxinc/nginx-unprivileged
        image: docker.io/nginx
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nserver1-svc
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nserver1
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nserver2-deploy
spec:
  selector:
    matchLabels:
      app: nserver2
  replicas: 3
  template:
    metadata:
      labels:
        app: nserver2
    spec:
      containers:
      - name: server2
        image: docker.io/nginx
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nserver2-svc
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nserver2
```

```
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nserver-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: www.server1.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nserver1-svc
            port:
              number: 80
  - host: www.server2.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nserver2-svc
            port:
              number: 80
```



```
root@cn2masternode:~/clusterip# k get ingress -A
NAMESPACE   NAME              CLASS    HOSTS                             ADDRESS        PORTS   AGE
default     nserver-ingress   <none>   www.server1.com,www.server2.com   172.16.80.35   80      21m
```

* Check connectivity using:
      curl <172.16.80.35>:80
      curl --header "Host:www.server2.com" http://172.16.80.35:80*
      curl --header "Host:www.server1.com" http://172.16.80.35:80*

## References
```
https://kubernetes.github.io/ingress-nginx/deploy/
```
