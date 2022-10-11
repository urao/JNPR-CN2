#### Steps to deploy K8s from Mac using kubespray

1. Install python3.9 and virtualenv on Mac
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python@3.9
curl https://bootstrap.pypa.io/get-pip.py | python3.9
pip install virtualenv

```
2. Create virtual env venv

```
virtualenv venv --system-site-packages
source venv/bin/activate
ansible --version      #check version 2.12.5
```
3. Git clone repo

```
git clone https://github.com/kubernetes-sigs/kubespray.git
cd kubespray
pip install -r requirements-2.12.txt
cd inventory
cp -rfp sample  cn2cluster
```

4. Append k8s-cluster.yml with [CN2 requirements](https://github.com/urao/JNPR-CN2/blob/main/CN2-22.2/CN2_requirements.md) for K8s install
5. Create [hosts.ini](https://github.com/urao/JNPR-CN2/blob/main/CN2-22.2/hosts.ini) file with node information, IP address, ansible_user

6. Run the deployment
```
cd ../
ansible -i inventory/cn2cluster/hosts.ini -m ping all
ansible-playbook -i inventory/cn2cluster/hosts.ini --become-user=root cluster.yml
```

6. Copy kube config file from the master node on to MAC
```
cd ~/
mkdir .kube
touch .kube/config
```

7. Install kubectl on Mac
```
curl -LO "https://dl.k8s.io/release/v1.25.0/bin/darwin/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
sudo chown root: /usr/local/bin/kubectl
```

8. SSH tunnel to master node
```
ssh -L 6443:127.0.0.1:6443 root@<master_node_ip_address>
```

9. Verify K8s nodes are in NotReady State
```
kubectl get nodes -o wide
```
