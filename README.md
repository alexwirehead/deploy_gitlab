Config and deploy test Gitlab env 
=========
The Ansible role for configuring and deploying Gitlab to explore Gitlab CI/CD 


Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

external_ip: you-external-instance-ip. defaul: 127.0.0.1

Dependencies
------------

All dependencies on a host-machine are installed by playbook ```install_docker.yml```
