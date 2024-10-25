############################################
#  Capgemini_PROLOG_BEGIN_TAG
#  This is an automatically generated prolog.
#
#  Copyright (C) Capgemini Engineering ACT S.A.S. 2016-2023. All rights reserved.
#
#  Capgemini_PROLOG_END_TAG
###########################################

import re
import sys
create_delete = sys.argv[1]
found_abstract = False
count = 0
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('NFSv2v3:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of NFSv2v3 are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+NFS_SERVICE_IP:\s+(.*?),\s+VG_NAME:\s+(.*?),\s+MOUNT_POINT:\s+(.*?),\s+NETWORK:\s+(.*?),\s+FILE_SYSTEM:\s+(.*?)}', line)
              if match:
                RG_NAME, NFS_SERVICE_IP, VG_NAME, MOUNT_POINT, NETWORK, FILE_SYSTEM  = match.groups()
                RG_NAME = RG_NAME.replace('\'','')
                RG_NAME = RG_NAME.replace('\"','')
                NFS_SERVICE_IP = NFS_SERVICE_IP.replace('\'','')
                NFS_SERVICE_IP = NFS_SERVICE_IP.replace('\"','')
                VG_NAME = VG_NAME.replace('\'','')
                VG_NAME = VG_NAME.replace('\"','')
                MOUNT_POINT = MOUNT_POINT.replace('\'','')
                MOUNT_POINT = MOUNT_POINT.replace('\"','')
                NETWORK = NETWORK.replace('\'','')
                NETWORK = NETWORK.replace('\"','')
                FILE_SYSTEM = FILE_SYSTEM.replace('\'','')
                FILE_SYSTEM = FILE_SYSTEM.replace('\"','')

                if not RG_NAME.strip() or RG_NAME.strip() == '':
                  print('Blank values are mentioned for RG_NAME in NFSv2v3')
                  sys.exit(1)
                if not NFS_SERVICE_IP.strip() or NFS_SERVICE_IP.strip() == '':
                  print('Blank values are mentioned for Service IP in NFSv2v3')
                  sys.exit(1)
                if not VG_NAME.strip() or VG_NAME.strip() == '':
                  print('Blank values are mentioned for VG_NAME in NFSv2v3')
                  sys.exit(1)
                if not MOUNT_POINT.strip() or MOUNT_POINT.strip() == '':
                  print('Blank values are mentioned for Mount Point in NFSv2v3')
                  sys.exit(1)
                if not NETWORK.strip() or NETWORK.strip() == '':
                  print('Blank values are mentioned for Network in NFSv2v3')
                  sys.exit(1)
                if not FILE_SYSTEM.strip() or FILE_SYSTEM.strip() == '':
                  print('Blank values are mentioned for File system in NFSv2v3')
                  sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for NFSv2v3: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', NFS_SERVICE_IP: '', VG_NAME: '', MOUNT_POINT: '', NETWORK: '', FILE_SYSTEM: '' }")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('NFSv2v3:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of NFSv2v3 are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+NFS_SERVICE_IP:\s+(.*?),\s+VG_NAME:\s+(.*?),\s+MOUNT_POINT:\s+(.*?),\s+NETWORK:\s+(.*?),\s+FILE_SYSTEM:\s+(.*?)}', line)
              if match:
                RG_NAME, NFS_SERVICE_IP, VG_NAME, MOUNT_POINT, NETWORK, FILE_SYSTEM  = match.groups()
                RG_NAME = RG_NAME.replace('\'','')
                RG_NAME = RG_NAME.replace('\"','')

                if not RG_NAME.strip() or RG_NAME.strip() == '':
                  print('Blank values are mentioned for RG_NAME in NFSv2v3')
                  sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for NFSv2v3: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', NFS_SERVICE_IP: '', VG_NAME: '', MOUNT_POINT: '', NETWORK: '', FILE_SYSTEM: '' }")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)

                
if not found_abstract:
  print('Error: NFSv2v3 variable not found in /external_var.yml')
  sys.exit(1)
