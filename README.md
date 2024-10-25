############################################
#  Capgemini_PROLOG_BEGIN_TAG
#  This is an automatically generated prolog.
#
#  Copyright (C) Capgemini Engineering ACT S.A.S. 2016-2023. All rights reserved.
#
#  Capgemini_PROLOG_END_TAG
############################################

#####################################################
#####################################################
# PowerHA SystemMirror Ansible Documentation - README
#####################################################
#####################################################


#################
Introduction	
#################

This README provides the necessary information and prerequisites to set up and use Ansible for PowerHA SystemMirror. PowerHA SystemMirror filesets ship ansible at /usr/es/sbin/cluster/samples directory in the form of a tar file (compressed format). After installing PowerHA SystemMirror 7.2.8 or later, you can extract ansible collections from a tar file and integrate with centralized node. A centralized node is the server that stores and manages ansible playbooks and roles. The centralized node simplifies Ansible management by providing a single location for storing and updating ansible content. You can run playbooks from the centralized node to configure PowerHA SystemMirror cluster and its resources. Whereas, a playbook is a set of instructions that defines how to automate a task or process.
This framework helps simplified installation, allows to update prerequisites before creating cluster like - updating /etc/hosts and /etc/cluster/rhosts file and helps to configure different resources like Resource group, Volume group , File system, Service IP, Network, Interfaces, Applications, WPAR, NFSv2,v3 and NFSv4. 


#################
Prerequisites	
#################

Before getting started with Ansible, ensure the following prerequisites are met.
1.	AIX: Make sure the centralized node is running AIX version 7.2 or 7.3, or later. Ansible requires these specific versions to ensure compatibility with AIX filesets.
2.	PowerHA: Install the latest PowerHA version 7.2.8, or later, on the centralized node. 
3.	Python: Install Python on both the centralized and remote servers. 
	Note: Python version 3.7.9 is tested with AIX 7.2 & 7.3, if you are using higher version, check python compatible version and use it. 
4.	Ansible: Install Ansible on the centralized node. Python is mandatory to install Ansible. Ansible package can be downloaded from below path.
	https://www.ibm.com/support/pages/aix-toolbox-linux-applications-downloads-alpha
	Verify that Ansible is installed on the centralized node by running the command:
	ansible --version 
	This displays the Ansible version is installed on your system or not.
5.	Password less SSH Connection: Establish password less SSH connections from the centralized node to the host nodes. This allows Ansible to communicate with the remote servers without requiring a password. To check Passwordless connectivity:
	ssh <remote node ip>
6.	RSH: Ensure RSH is enabled on all the nodes. Check /etc/inetd.conf to verify RSh is enabled on all nodes by uncommenting rsh related fields and then update /.rhosts with + +
7.	Tarball Extraction: Extract the Ansible filesets from the provided Tarball from PowerHA installables. The tarball is located at the centralized node at path /usr/es/sbin/cluster/samples/ansible/. To extract the files, follow these steps:
	1.	Login as a root / privileged to the centralized node
	2.	Copy the tar ball from path /usr/es/sbin/cluster/samples/ansible/ to path /
	3.	Switch to home or root directory where the tarball needs to be extracted
		# cd / or home directory
	4.	Unzip the tarball 
		# gunzip /usr/es/sbin/cluster/samples/ansible/ansible_powerha_tarball.tar.gz
	5.	Extract the contents of the tarball by running the below command.
		# tar -xvf /usr/es/sbin/cluster/samples/ansible/ansible_powerha_tarball.tar
		After the extraction, you will find two new folders in / directory.
                        /playbooks /plugins /roles 
                        /external_var.yml /ansible.cfg /sample_external_var.yml /dumpall.j2 /hosts /README_ansible_powerha.txt files
8.	Set PATH variable: Update PATH variable with the ansible binaries to locate and execute its binaries. The ansible binaries are typically installed in /opt/freeware/bin
	# export PATH=$PATH:/opt/freeware/bin
9.	Verify the ansible installed version by running below command
	# ansible --version


#####################
Deployment using Ansible
#####################

Once you have fulfilled the above prerequisites, you can start using Ansible playbooks to Install, configure different resources.
Follow these steps to get started:
1.	Update the Ansible Hosts File: Navigate to the /etc/ansible directory and open the hosts file with any available editors, we used vi. Update the file with the IP addresses of the target nodes along with the appropriate username and Python path for those nodes. This step is crucial for Ansible to identify and connect to the remote servers.
	# vi /hosts
2.	Update Ansible External Variables: Open the external_vars.yml file located in the / directory. Update the file with the required NODE_DETAILS and NODES and test case details specific to your environment. This file allows you to customize variables that will be used in your Ansible playbooks.
	# vi /external_var.yml
3.	Execute Ansible Playbooks: Once above steps are properly configured and the necessary variables updated, you can now execute Ansible playbooks. 
	Go to the path /playbooks and run the Ansible commands along with the desired tags. 
	Example: To run a playbook with specific tags, use the below command, move to the below path and run command as: 
	# cd /playbooks 
        # ansible-playbook -i /hosts demo_playbook.yml --tags <tag1>,<tag2>
	This allows you to selectively execute specific tasks or roles within the playbook based on the provided tags.


#####################
Ansible Playbook to Install/Uninstall or Configure/Unconfigure PowerHA SystemMirror 
#####################

You can use the following playbooks to install/uninstall or configure/unconfigure PowerHA SystemMirror cluster and resources, use the following commands:
	Map Hosts: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_map_hosts.yml
	Install PowerHA: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_powerha.yml --tags install
	Uninstall PowerHA: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_powerha.yml --tags uninstall
	Create a standard cluster: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_cluster.yml --tags standard
	Create a linked cluster: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_cluster.yml --tags linked
	Create a stretched cluster: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts demo_cluster.yml --tags stretched
	Remove a cluster: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_cluster.yml --tags delete
	Create a resource group: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_resource_group.yml --tags create
	Remove a resource group: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_resource_group.yml --tags delete
	Add a network: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_network.yml --tags create
	Remove a network: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_network.yml --tags delete
	Add an interface: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_interface.yml --tags create
	Remove an interface: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_interface.yml --tags delete
	Add a file system: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_file_system.yml --tags create
	Remove a file system: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_file_system.yml --tags delete
	Add an application: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts demo_applications.yml --tags create
	Remove an application: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_applications.yml --tags delete
	Add a volume group: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_volume_groups.yml --tags create
	Remove a volume group: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_volume_groups.yml --tags delete
	Add a Service IP: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_service_ip.yml --tags create
	Remove a Service IP: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_service_ip.yml --tags delete
	Start Cluster Services: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_start_stop_services.yml --tags start
	Stop Cluster Services: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_start_stop_services.yml --tags stop
	Add WPAR: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_wpar.yml --tags create
	Remove WPAR: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_wpar.yml --tags delete
	Add NFSv2v3: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_nfsv2v3.yml --tags create
	Remove NFSv2v3: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_nfsv2v3.yml --tags delete
	Add NFSv4: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_nfsv4.yml --tags create
	Remove NFSv4: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_nfsv4.yml --tags delete
	Cluster Health: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_cluster_health.yml
	Resource Group Move: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_move_resource_group.yml 
	SYNC GLVM Creation: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_glvm.yml  --tags create,sync
	SYNC GLVM Deletion: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_glvm.yml  --tags delete
	Persistent_IP Creation: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_persistent_ip.yml  --tags create
	Persistent_IP Deletion: ANSIBLE_CONFIG=/ansible.cfg ansible-playbook -i /hosts /playbooks/demo_persistent_ip.yml  --tags delete


#####################
Notes: 
#####################

1)	All the field input values are mentioned in the comments in /external_var.yml
2)	For running start and stop cluster services playbook, we dont need to update any value in /external_var.yml
3)	NODES and NODE_DETAILS in /external_var.yml are mandatory for working with any playbook.
4)	You can refer Sample_external_var.yml in / for updating external_var.yml 
5)	Check the cluster state before running any playbook

