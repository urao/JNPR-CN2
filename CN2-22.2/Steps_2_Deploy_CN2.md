#### Steps

1. Run steps to install and run [KubeSpray](https://github.com/urao/JNPR-CN2/blob/main/CN2-22.2/Steps_2_Run_KubeSpray_from_Mac.md) from your Mac

2. Download the contrail deployment manifest package version 22.2 for [K8s](https://support.juniper.net/support/downloads/?p=contrail#sw)

3. Preform below steps
```
tar -zxvf contrail-manifests-k8s-22.2.0.93.tgz
cd contrail-manifests-k8s-22.2.0.93/contrail-manifests-k8s/single_cluster
cp single_cluster_deployer_example.yaml single_cluster_deployer.yaml
```
4. Obtain credentials for hub.juniper.net from Juniper Sales Team

5. Modify deployer.yaml file to add juniper registry(hub.juniper.net) credentials
```
sed -i s/'<base64-encoded-credential>'/$ENCODED_CREDS/ single_cluster_deployer.yaml
```
6. Deploy CN2 CNI
```
kubectl apply -f single_cluster_deployer.yaml
```
7. Wait for the CN2 pods to come up and show 'RUNNING' status
```
eval 'kubectl --namespace='{contrail,contrail-system,contrail-deploy}' get pod;'
```
8. Check status of the nodes to be in READY state
```
kubectl get nodes -o wide
```

### References
* https://www.juniper.net/documentation/us/en/software/cn-cloud-native22/cn-cloud-native-k8s-install-and-lcm/topics/task/cn-cloud-native-k8s-create-kubernetes-cluster.html
* https://github.com/kubernetes-sigs/kubespray
