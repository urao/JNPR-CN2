

# Common CN2 debug commands

```
kubectl -n contrail-system logs contrail-k8s-apiserver-65d46fd7b8-jjvdz 
kubectl -n contrail-system logs contrail-k8s-controller-5f6956f669-8ng7s
kubectl api-resources --namespaced=true | grep juniper
apiservers                                        configplane.juniper.net/v1alpha1     true         ApiServer
controllers                                       configplane.juniper.net/v1alpha1     true         Controller
kubemanagers                                      configplane.juniper.net/v1alpha1     true         Kubemanager
controls                                          controlplane.juniper.net/v1alpha1    true         Control
addressgroups                    ag               core.contrail.juniper.net/v1alpha1   true         AddressGroup
applicationpolicysets            aps              core.contrail.juniper.net/v1alpha1   true         ApplicationPolicySet
bgpasaservices                   bgpaas           core.contrail.juniper.net/v1alpha1   true         BGPAsAService
bgprouters                       br               core.contrail.juniper.net/v1alpha1   true         BGPRouter
firewallpolicies                 fp               core.contrail.juniper.net/v1alpha1   true         FirewallPolicy
firewallrules                    fr               core.contrail.juniper.net/v1alpha1   true         FirewallRule
routinginstances                 ri               core.contrail.juniper.net/v1alpha1   true         RoutingInstance
subnets                          sn               core.contrail.juniper.net/v1alpha1   true         Subnet
virtualmachineinterfaces         vmi              core.contrail.juniper.net/v1alpha1   true         VirtualMachineInterface
virtualnetworkrouters            vnr              core.contrail.juniper.net/v1alpha1   true         VirtualNetworkRouter
virtualnetworks                  vn               core.contrail.juniper.net/v1alpha1   true         VirtualNetwork
vrouters                                          dataplane.juniper.net/v1alpha1       true         Vrouter
etcds                                             datastore.juniper.net/v1alpha1       true         Etcd
```
