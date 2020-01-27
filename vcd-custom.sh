#!/bin/bash
if [ x$1 == x"precustomization" ]; then 
echo Do Precustomization tasks 
elif [ x$1 == x"postcustomization" ]; then 
echo Do Postcustomization tasks
sed -i 's/ether/eth0/' /etc/network/interfaces
fi