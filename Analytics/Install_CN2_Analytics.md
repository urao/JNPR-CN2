
### Steps to install CN2 Analytics on existing CN2 Cluster on Ubuntu OS

1. Install [Helm](https://helm.sh)
```
sudo snap helm
```
2. Requirement is to have a VIP address for the analytics deployment
3. Download contrail analytics package from [Juniper support site](https://support.juniper.net/support/downloads/?p=contrail#sw)
4. Install contrail analytics
```
kubectl create namespace contrail-analytics
helm -n contrail-analytics install analytics contrail-analytics-<version>.tgz --set externalIP=<VIP_ADDRESS>
```
5. Wait couple of minutes
6. Check contrail analytics pods come up and is in RUNNING state
```
helm -n contrail-analytics list
kubectl get pods -n contrail-analytics
```


### References
* https://www.juniper.net/documentation/us/en/software/cn-cloud-native22/cn-cloud-native-feature-guide/cn-cloud-native-network-feature/topics/concept/cn-cloud-native-analytics.html
* https://helm.sh
