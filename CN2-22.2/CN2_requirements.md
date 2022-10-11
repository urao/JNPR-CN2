
#### CN2 Requirements with k8s version v1.23.7

```
cluster_name: ${clustername}.cluster.local
enable_nodelocaldns: false
container_manager: crio
host_key_checking: false
etcd_deployment_type: host
download_localhost: true
download_container: false
download_run_once: true
kube_version: ${version}
kube_network_plugin: cni
kube_network_plugin_multus: false
```
