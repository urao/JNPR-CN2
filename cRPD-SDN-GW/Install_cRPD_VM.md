### Steps to install cRPD on VM on CentOS

1. Enable SSH service

2. Disable selinux 

3. Configure interfaces with approriate IP address using network-scripts

4. Install docker, by running below commands
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum update && yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y 
systemctl start docker
systemctl enable docker
```
5. Configure loopback interface with desired IP address
```
ip addr add 1.1.1.11/32 dev lo
```
6. If linux kernel version is 4.5 or higher to enable MPLS using below commands
```
modprobe mpls_iptunnel
modprobe mpls_router
```
7. Verify the modules are active
```
lsmod | grep mpls
```
8. Download cRPD image in tgz format from [Juniper support site](https://support.juniper.net/support/downloads/?p=cRPD#sw)
9. Load cRPD image from a tar archive
```
docker load -i junos-routing-crpd-amd64-docker-22.2R1.9.tgz
```
10. Verify the cRPD image is loaded
```
docker image ls
```
11. Create docker volumes for configuration and logs
```
docker volume create crpd-conf
docker volume create crpd-logs
```
12. By default cRPD listens on the port to allow netconf over ssh access. Once cRPD starts, it will try to bind port 22 but, sharing the same network stack of the host OS, it will find it already in use. As a result cRPD ssh daemon will fail. To avoid this, provide ssh on the different port for cRPD. You can do it by creating an alternative sshd_config file and mount into the container during creation.
13. Run cRPD,
```
docker run --rm --detach --name crpd1 -h crpd1 --net=host --privileged \
       -v crpd-conf:/config -v crpd-logs:/var/log -it crpd:22.2R1.9
```
14. Access CLI,
```
docker exec -it <container_id> cli
```
15. Licenses, is required for the BGP peering to be established.


### References
* https://www.juniper.net/documentation/us/en/software/crpd/crpd-deployment/topics/concept/understanding-crpd.html
