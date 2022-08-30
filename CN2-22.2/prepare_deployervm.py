#!/usr/bin/python
# -------------------------------------------------
# This python script will install required packages
# on the deployer VM to install CN2 cluster
# Tested for CN2 22.2 software version
# -------------------------------------------------
import os, sys, logging, getpass, time
import argparse
import paramiko
from socket import error as SocketError
import warnings
#from cryptography.utils import DeprecatedIn25
#warnings.simplefilter('ignore', DeprecatedIn25)

class SetDeployerVMConfig(object):
    def __init__(self, address):
        self.hostip= ipaddress
        self.username = 'root'
        self.password = 'c0ntrail123'
        self.k8s_version = 'v1.23.7'

    def connect_2_device(self):
        print('Connecting to Deployer VM.......:  '+ self.hostname)
        conf = paramiko.SSHConfig()
        conf.parse(open(os.path.expanduser('~/.ssh/config')))
        host = conf.lookup(self.hostip)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.hostip, username=self.username, password=self.password, \
                                sock=paramiko.ProxyCommand(host.get('proxycommand')), banner_timeout=200)
            #print self.client
            print('\nSuccessfully connected to Deployer VM .. : '+ self.hostip)
            return self.client
        except SocketError as err:
            print('\nSocket error: ')
            print(err.message)
            return None
        except paramiko.AuthenticationException as err:
            print('\nConnect failed, Auth error : ')
            print(err.message)
            return None
        except Exception as err:
            print('\nConnect failed, unknown error type : ')
            print(err.message)
            return None

    def configure_it(self):
        print('Building deployer VM ..... '+ self.hostip)

        with open('/Users/urao/.ssh/id_rsa.pub', 'r') as f:
            ssh_data = f.read().rstrip()
            print(ssh_data)

        #check bufsize=0. 1. -1 for
        stdin, stdout, stderr = self.client.exec_command("ls")
        for line in iter(stdout.readline, ""):
            print(line)

        #Basics
        self.client.exec_command("echo \'HISTTIMEFORMAT="%d/%m/%y %T "\' >> ~/.bashrc")
        self.client.exec_command("echo \'HISTTIMEFORMAT="%F %T "\' >> ~/.bashrc")
        self.client.exec_command("source ~/.bashrc")

        #Install pkgs
        self.client.exec_command("setenforce 0")
        self.client.exec_command("sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux")
        self.client.exec_command("systemctl disable firewalld; systemctl stop firewalld; systemctl mask firewalld")
        self.client.exec_command("yum update -y")
        time.sleep(30)
        self.client.exec_command("yum install epel-release -y")
        self.client.exec_command("yum install git wget sshpass bash-completion -y")
        self.client.exec_command("cd /var/tmp/")
        self.client.exec_command("wget https://bootstrap.pypa.io/pip/2.7/get-pip.py")
        self.client.exec_command("python get-pip.py")
        self.client.exec_command("cd")
        time.sleep(30)
        self.client.exec_command("pip install --upgrade pip setuptools")
        self.client.exec_command("python -m pip install ansible-core==2.11.11")
        self.client.exec_command("python -m pip install ansible")
        self.client.exec_command("python -m pip install -U cryptography")

        # generate sshkeys and copy to k8s nodes
        self.client.exec_command("ssh-keygen -t rsa -N ''")
        self.client.exec_command("touch /root/password.txt")
        self.client.exec_command("echo {} > /root/password.txt".format(self.password))
        for k8snode in ():
            self.client.exec_command("sshpass -f /root/password.txt ssh-copy-id -i ~/.ssh/id_rsa.pub root@{}".format(k8snode))
        self.client.exec_command("rm /root/password.txt")


        #clone kubespray and install k8s
        self.client.exec_command("git clone https://github.com/kubernetes-sigs/kubespray.git")
        self.client.exec_command("cd /root/kubespray && cp requirements-2.11.txt requirements-2.11.txt.orig")
        self.client.exec_command("echo -e \"ansible==4.10.0\nansible-core==2.11.11\njinja2==2.11.3\nnetaddr==0.7.19\npbr==5.4.4\njmespath==0.9.5\nruamel.yaml==0.16.10\nMarkupSafe==1.1.1\" > /root/kubespray/requirements-2.11.txt")
        self.client.exec_command("cd /root/kubespray && pip install -r requirements-2.11.txt")
        #declare -a IPS=(master,10.10.1.3 wnode0,10.10.1.4 wnode1,10.10.1.5)
        #CONFIG_FILE=inventory/mycluster/hosts.yml python contrib/inventory_builder/inventory.py ${IPS[@]}
        #export KUBE_CONTROL_HOSTS=1
        #cp -r inventory/sample inventory/mycluster

        #check k8s installed
        self.client.exec_command("curl -LO https://dl.k8s.io/release/{}/bin/linux/amd64/kubectl".format(self.k8s_version))
        self.client.exec_command("sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl")
        self.client.exec_command("kubectl version --client")
        #copy admin.conf file from master node on to deployervm
        #check node status

        #kubectl bash completion
        #source /usr/share/bash-completion/bash_completion
        #echo 'source <(kubectl completion bash)' >>~/.bashrc
        #echo 'alias k=kubectl' >>~/.bashrc
        #echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
        self.client.exec_command("reboot")
        print("Configured Deployer VM device successful and rebooted.......\n")

    def close_it(self):
        print('Closing connection......' + self.hostname + '\n')
        self.client.close()

def parse_options(args):
    parser = argparse.ArgumentParser(
        description='Provide Deployer VM IP address (Ex: 192.168.10.11)'
            )
    parser.add_argument('-ip', '--ipaddress', required=True, help='Deployer VM IP address')

    opt = parser.parse_args()
    return opt

def main(argv):
    options = parse_options(argv)
    deployervm = SetDeployerVMConfig(options.ipaddress)
    res = deployervm.connect_2_device()
    if res is not None:
        deployervm.configure_it()
        deployervm.close_it()

if __name__ == "__main__":
    main(sys.argv[1:])

