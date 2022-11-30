#### Steps to upgrade from CN2 version 22.2 to 22.3

0. Login into CN2 version 22.2 cluster

1. Download the contrail deployment manifest package version 22.3 for [K8s](https://support.juniper.net/support/downloads/?p=contrail#sw)

2. Perform below steps
```
tar -zxvf contrail-manifests-k8s-22.3.0.71.tgz
cd contrail-manifests-k8s/single_cluster
cp single_cluster_deployer_example.yaml single_cluster_deployer.yaml
```
3. Modify the image registry and controlData interfaces

4. Deploy CN2 22.3 image
```
kubectl apply -f contrail-manifests-k8s/single_cluster/single_cluster_deployer.yaml
```

5. Wait the contrail pods to come up and show `RUNNING` status
```
eval 'kubectl --namespace='{contrail,contrail-system,contrail-deploy}' get pod;'
```
6. Check contrail-status command
```
cp ~/contrail-tools/kubectl-contrailstatus /usr/local/bin
chmod +x /usr/local/bin/kubectl-contrailstatus
```

```
kubectl-contrailstatus --all
```
