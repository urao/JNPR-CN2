
# Multi-Mesh VNR in same namespace - CN2
# Pods created in VN1 and VN2 in namespace NS1 cannot talk to each other by default, so
# create Mesh vnr1, Pods created in VN3 and VN4 in namespace NS1 cannot talk to each 
# other, create Mesh vnr2, now import Mesh vnr1 into vnr2 and vice-versa for pods in
# VN1, VN2, VN3 and VN4 talk to each other.
