
## Steps to Deploy Kubernetes v1.23.5 + Juniper CN2 CNI 

1. Bring up 3 Centos 7.6 (1810) Servers or Virtual Machines, 1 deployer node, 1 master node and 1 worker node
2. Upgrade kernel version to the one supported by CN2 on master and worker node
```
sudo yum install -y wget
wget http://ftp.iij.ad.jp/pub/linux/centos-vault/centos/7.8.2003/updates/x86_64/Packages/kernel-3.10.0-1127.19.1.el7.x86_64.rpm
yum install kernel-3.10.0-1127.19.1.el7.x86_64.rpm -y
```
3. If the 'docker' is chosen as container runtime, provide dockerhub credentials on master and workder node
   to avoid seeing message 'anonymous limit of pulls'
```
docker login --username <USERNAME> --password <PASSWORD>
```
4. Install required packages on deployer VM
```
sudo yum update -y
sudo yum install -y epel-release
sudo yum install -y git net-tools sshpass wget python3-pip
sudo yum install -y python36
sudo pip3 install ansible
```
5. Create password-less, automatic login to master and worker nodes from deployer VM
```
ssh-keygen -r rsa
ssh-copy-id -i $HOME/.ssh/id_rsa.pub root@<master-node-ip>
ssh-copy-id -i $HOME/.ssh/id_rsa.pub root@<worker-node-ip>
```
6. Git clone Kubespray and perform below steps 
```
cd $HOME
git clone https://github.com/kubernetes-sigs/kubespray.git
cd kubespray
sudo pip3 install -r requirements.txt
cp -rfp inventory/sample inventory/mycluster
cd inventory/mycluster
cp inventory.ini hosts.ini
```
7. Modify hosts.ini to add Hostname and IP address of master and worker node, [sample one]()
8. Validate all the hosts are reachable
```
/usr/local/bin/ansible -i hosts.ini -m ping all
```
9. Modify k8s-cluster.yml to add kubernetes version, CNI, PD, Service CIDR address etc.. [sample one]()
10. Deploy Kubernetes
```
cd $HOME/kubespray
/usr/local/bin/ansible-playbook -i inventory/mycluster/hosts.ini cluster.yml -u root --become 
```
11. Access new k8s cluster, login into master node
```
sudo kubectl get nodes
```

```
NAME    STATUS      ROLES                  AGE   VERSION
node1   NotReady    control-plane,master   30h   v1.23.5
node2   NotReady    <none>                 30h   v1.23.5
```
12. Perform below steps on the master node 
13. Download CN2 [Deployment Manifest for K8s](https://support.juniper.net/support/downloads/?p=contrail#sw)
14. Untar the downloaded manifest file
```
tar -zxvf contrail-manifests-k8s-22.1.0.93.tgz
cd $HOME/contrail-manifests-k8s/single_cluster/
```
15. Modify deployer.yaml to change replicaset, gateway etc.. [sample one]() 
16. Login to hub.juniper.net to download the CN2 images
```
docker login hub.juniper.net --username <USERNAME> --password <PASSWORD>
```
17. Deploy Contrail CN2 CNI
```
kubectl apply -f deployer.yaml
```
18. Wait for the CN2 pods to come up and show 'RUNNING' status
```
eval 'kubectl --namespace='{contrail,contrail-system,contrail-deploy}' get pod;'
```

```
NAME                                        READY   STATUS    RESTARTS   AGE
contrail-control-0                          2/2     Running   0          30h
contrail-k8s-kubemanager-869dc9c546-d62lp   1/1     Running   0          30h
contrail-vrouter-masters-qzz57              3/3     Running   0          30h
contrail-vrouter-nodes-hb4lc                3/3     Running   0          30h
NAME                                       READY   STATUS    RESTARTS   AGE
contrail-k8s-apiserver-77d7cc56fb-mzng4    1/1     Running   0          30h
contrail-k8s-controller-7777877b44-c4zwb   1/1     Running   0          30h
NAME                                     READY   STATUS    RESTARTS   AGE
contrail-k8s-deployer-858bb45dd7-gxpcz   1/1     Running   0          30h
```
19. Login into master node and check status of the nodes
```
sudo kubectl get nodes
```

```
NAME    STATUS   ROLES                  AGE   VERSION
node1   Ready    control-plane,master   30h   v1.23.5
node2   Ready    <none>                 30h   v1.23.5
```
20. Deployment FINISHED...
