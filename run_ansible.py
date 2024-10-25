############################################
#  Capgemini_PROLOG_BEGIN_TAG
#  This is an automatically generated prolog.
#
#  Copyright (C) Capgemini Engineering ACT S.A.S. 2016-2023. All rights reserved.
#
#  Capgemini_PROLOG_END_TAG
###########################################

import os
import subprocess
import sys
import yaml
maps_abstract = False
cluster_abstract = False
rg_abstract = False
glvm_abstract = False
network_abstract = False
interface_abstract = False
service_ip_abstract = False
vg_abstract = False
fs_abstract = False
persistent_abstract = False
inventory_path = "/hosts"
os.environ['ANSIBLE_CONFIG']= "/ansible.cfg"

with open(r'/external_var.yml', 'r') as f:
    data = yaml.safe_load(f)

try:
    node = data['NODE_DETAILS']
    print("found the NODE_DETAILS in external_var.yml file")
    maps_abstract = True
    maps_playbook = "/playbooks/demo_map_hosts.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, maps_playbook]
    maps_result = subprocess.run(cmd, capture_output=True)
    if maps_result.returncode ==0:
        print(maps_playbook, "playbook execution is completed. Execution flow is ", maps_result.stdout.decode('utf-8'))
    else:
        print(maps_playbook, "playbook execution failed", maps_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml'.format(ke))
    sys.exit(1)

try:
    power_ha = data['POWERHA_BLD_PATH']
    powerha_abstract = True
    powerha_playbook = "/playbooks/demo_PowerHA.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, powerha_playbook, '--tags', 'install']
    powerha_result = subprocess.run(cmd, capture_output=True)
    if powerha_result.returncode ==0:
        print(powerha_playbook, "playbook execution is completed. Execution flow is ", powerha_result.stdout.decode('utf-8'))
    else:
        print(powerha_playbook, "playbook execution failed", powerha_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml'.format(ke))
    sys.exit(1)

try:
    cls_type = data['Cluster_Type']
    if cls_type == "Linked":
        cluster_abstract = True
        #import pdb; pdb.set_trace()
        cluster_playbook = "/playbooks/demo_cluster.yml"
        cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, cluster_playbook, '--tags', 'linked']
        linked_result = subprocess.run(cmd, capture_output=True)
        if linked_result.returncode ==0:
            print(cluster_playbook, "playbook execution is completed. Execution flow is ", linked_result.stdout.decode('utf-8'))
        else:
            print(cluster_playbook, "playbook execution failed", linked_result.stdout.decode('utf-8'))
            sys.exit(1)
    elif cls_type == "Standard":
        cluster_abstract = True
        cluster_playbook = "/playbooks/demo_cluster.yml"
        cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, cluster_playbook, '--tags', 'standard']
        standard_result = subprocess.run(cmd, capture_output=True)
        if standard_result.returncode ==0:
            print(cluster_playbook, "playbook execution is done. Execution flow is ", standard_result.stdout.decode('utf-8'))
        else:
            print(cluster_playbook, "playbook execution failed", standard_result.stdout.decode('utf-8'))
            sys.exit(1)
    elif cls_type == "Stretched":
        cluster_abstract = True
        cluster_playbook = "/playbooks/demo_cluster.yml"
        cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, cluster_playbook, '--tags', 'stretched']
        stretched_result = subprocess.run(cmd, capture_output=True)
        if stretched_result.returncode ==0:
            print(cluster_playbook, "playbook execution is done. Execution flow is ", stretched_result.stdout.decode('utf-8'))
        else:
            print(cluster_playbook, "playbook execution failed", stretched_result.stdout.decode('utf-8'))
            sys.exit(1)

except KeyError as ke:
    print('Key {} Not Found in /external_var.yml'.format(ke))
    sys.exit(1)

try:
    net_data = data['NETWORK']
    network_abstract = True
    network_playbook = "/playbooks/demo_network.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, network_playbook, '--tags', 'create']
    network_result = subprocess.run(cmd, capture_output=True)
    if network_result.returncode ==0:
        print(network_playbook, "playbook execution is completed. Execution flow is ", network_result.stdout.decode('utf-8'))
    else:
        print(network_playbook, "playbook execution failed", network_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping'\
          ' /playbooks/demo_network.yml playbook execution'.format(ke))

try:
    net_data = data['PERSISTENT_IP']
    persistent_abstract = True
    persistent_playbook = "/playbooks/demo_persistent_ip.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, persistent_playbook, '--tags', 'create']
    persistent_result = subprocess.run(cmd, capture_output=True)
    if persistent_result.returncode ==0:
        print(persistent_playbook, "playbook execution is completed. Execution flow is ", persistent_result.stdout.decode('utf-8'))
    else:
        print(persistent_playbook, "playbook execution failed", persistent_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping '\
          'the /playbooks/demo_persistent_ip.yml playbook execution'.format(ke))

try:
    inf_data = data['INTERFACES']
    interface_abstract = True
    interface_playbook = "/playbooks/demo_interface.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, interface_playbook, '--tags', 'create']
    interface_result = subprocess.run(cmd, capture_output=True)
    if interface_result.returncode ==0:
        print(interface_playbook, "playbook execution is completed. Execution flow is ", interface_result.stdout.decode('utf-8'))
    else:
        print(interface_playbook, "playbook execution failed", interface_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping '\
          '/playbooks/demo_interface.yml playbook execution'.format(ke))

try:
    ser_data = data['SERVICE_IP']
    service_ip_abstract = True
    service_ip_playbook = "/playbooks/demo_service_ip.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, service_ip_playbook, '--tags', 'create']
    service_ip_result = subprocess.run(cmd, capture_output=True)
    if service_ip_result.returncode ==0:
        print(service_ip_playbook, "playbook execution is completed. Execution flow is ", service_ip_result.stdout.decode('utf-8'))
    else:
        print(service_ip_playbook, "playbook execution failed", service_ip_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml hence skipping'\
          ' /playbooks/demo_service_ip.yml playbook execution'.format(ke))

try:
    cls = data['Cluster_Type']
    glvm_data = data['GLVM']
    if cls == "Linked":
        glvm_abstract = True
        glvm_playbook = "/playbooks/demo_glvm.yml"
        cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, glvm_playbook, '--tags', 'create,sync']
        glvm_result = subprocess.run(cmd, capture_output=True)
        if glvm_result.returncode ==0:
            print(glvm_playbook, "playbook execution is completed. Execution flow is ", glvm_result.stdout.decode('utf-8'))
        else:
            print(glvm_playbook, "playbook execution failed", glvm_result.stdout.decode('utf-8'))
            sys.exit(1)
    else:
        print("cluster type is not linked hence skipping the GLVM creation.")
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping '\
          'the /playbooks/demo_glvm.yml playbook execution'.format(ke))

try:
    rg_data= data['RGNAMES']
    rg_abstract = True
    rg_playbook = "/playbooks/demo_resource_group.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, rg_playbook, '--tags', 'create']
    rg_result = subprocess.run(cmd, capture_output=True)
    if rg_result.returncode ==0:
        print(rg_playbook, "playbook execution is completed. Execution flow is ", rg_result.stdout.decode('utf-8'))
    else:
        print(rg_playbook, "playbook execution failed", rg_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml hence skipping '\
          'the /playbooks/demo_resource_group.yml playbook execution'.format(ke))

try:
    vg_data = data['VG']
    vg_abstract = True
    vg_playbook = "/playbooks/demo_volume_groups.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, vg_playbook, '--tags', 'create']
    vg_result = subprocess.run(cmd, capture_output=True)
    if vg_result.returncode ==0:
        print(vg_playbook, "playbook execution is completed. Execution flow is ", vg_result.stdout.decode('utf-8'))
    else:
        print(vg_playbook, "playbook execution failed", vg_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping '\
          'the /playbooks/demo_volume_groups.yml playbook execution'.format(ke))

try:
    fs_data = data['FS']
    if vg_abstract:
        fs_abstract = True
        fs_playbook = "/playbooks/demo_file_system.yml"
        cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, fs_playbook, '--tags', 'create']
        fs_result = subprocess.run(cmd, capture_output=True)
        if fs_result.returncode ==0:
            print(fs_playbook, "playbook execution is completed. Execution flow is ", fs_result.stdout.decode('utf-8'))
        else:
            print(fs_playbook, "playbook execution failed", fs_result.stdout.decode('utf-8'))
            sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml Hence skipping '\
          'the /playbooks/demo_file_system.yml playbook execution'.format(ke))

try:
    vg_rg_data = data['VG_RG']
    VG_RG_abstract = True
    VG_RG_playbook = "/playbooks/demo_add_vg_to_rg.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, VG_RG_playbook]
    vg_rg_result = subprocess.run(cmd, capture_output=True)
    if vg_rg_result.returncode ==0:
        print(VG_RG_playbook, "playbook execution is completed. Execution flow is ", vg_rg_result.stdout.decode('utf-8'))
    else:
        print(VG_RG_playbook, "playbook execution failed", vg_rg_result.stdout.decode('utf-8'))
        sys.exit(1)
except KeyError as ke:
    print('Key {} Not Found in /external_var.yml hence skipping '\
          'the /playbooks/demo_add_vg_to_rg.yml playbook execution'.format(ke))

try:
    rg_ser_data = data['SERVICE_IP_RG']
    ServiceIP_RG_abstract = True
    ServiceIP_playbook = "/playbooks/demo_add_service_ip_to_rg.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, ServiceIP_playbook]
    ServiceIP_rg_result = subprocess.run(cmd, capture_output=True)
    if ServiceIP_rg_result.returncode ==0:
        print(ServiceIP_playbook, "playbook execution is completed. Execution flow is ", ServiceIP_rg_result.stdout.decode('utf-8'))
    else:
        print(ServiceIP_playbook, "playbook execution failed", ServiceIP_rg_result.stdout.decode('utf-8'))
        sys.exit(1)

except KeyError as ke:
    print('Key {} Not Found in /external_var.yml '\
          'hence skipping the /playbooks/demo_add_service_ip_to_rg.yml playbook execution'.format(ke))

try:
    app_c_data = data['ApplicationController']
    app_m_data = data['ApplicationMonitor']
    app_playbook = "/playbooks/demo_applications.yml"
    cmd = ['/opt/freeware/bin/ansible-playbook', '-i', inventory_path, app_playbook, '--tags', 'create']
    app_result = subprocess.run(cmd, capture_output=True)
    if app_result.returncode ==0:
        print(app_playbook, "playbook execution is completed. Execution flow is ", app_result.stdout.decode('utf-8'))
    else:
        print(app_playbook, "playbook execution failed", app_result.stdout.decode('utf-8'))
        sys.exit(1)

except KeyError as ke:
    print('Key {} Not Found in /external_var.yml '\
          'hence skipping the /playbooks/demo_applications.yml playbook execution'.format(ke))