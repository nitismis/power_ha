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
          if line.startswith('WPAR:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of WPAR are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+WPAR_SERVICE_IP:\s+(.*?),\s+APP_SCRIPTS_PATH:\s+(.*?),\s+APP_NAME:\s+(.*?),\s+VG_NAME:\s+(.*?),\s+FS_NAME:\s+(.*?)}', line)
              if match:
                NAME, WPAR_SERVICE_IP, APP_SCRIPTS_PATH, APP_NAME, VG_NAME, FS_NAME = match.groups()
                WPAR_SERVICE_IP = WPAR_SERVICE_IP.replace('\'','')
                WPAR_SERVICE_IP = WPAR_SERVICE_IP.replace('\"','')
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')
                APP_SCRIPTS_PATH = APP_SCRIPTS_PATH.replace('\'','')
                APP_SCRIPTS_PATH = APP_SCRIPTS_PATH.replace('\"','')
                APP_NAME = APP_NAME.replace('\'','')
                APP_NAME = APP_NAME.replace('\"','')
                VG_NAME = VG_NAME.replace('\'','')
                VG_NAME = VG_NAME.replace('\"','')
                FS_NAME = FS_NAME.replace('\'','')
                FS_NAME = FS_NAME.replace('\"','')

                if not WPAR_SERVICE_IP.strip() or WPAR_SERVICE_IP.strip() == '':
                  print('Blank values are mentioned for Service IP in WPAR')
                  sys.exit(1)
                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in WPAR')
                  sys.exit(1)
                if not APP_SCRIPTS_PATH.strip() or APP_SCRIPTS_PATH.strip() == '':
                  print('Blank values are mentioned for APP SCRIPT PATH in WPAR')
                  sys.exit(1)
                if not APP_NAME.strip() or APP_NAME.strip() == '':
                  print('Blank values are mentioned for APP NAME in WPAR')
                  sys.exit(1)
                if not VG_NAME.strip() or VG_NAME.strip() == '':
                  print('Blank values are mentioned for VG NAME in WPAR')
                  sys.exit(1)
                if not FS_NAME.strip() or FS_NAME.strip() == '':
                  print('Blank values are mentioned for FS NAME in WPAR')
                  sys.exit(1)


              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for WPAR: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', WPAR_SERVICE_IP: '', APP_SCRIPTS_PATH: '', APP_NAME: '', , VG_NAME: '', FS_NAME: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('WPAR:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of WPAR are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+WPAR_SERVICE_IP:\s+(.*?),\s+APP_SCRIPTS_PATH:\s+(.*?),\s+APP_NAME:\s+(.*?),\s+VG_NAME:\s+(.*?),\s+FS_NAME:\s+(.*?)}', line)
              if match:
                NAME, WPAR_SERVICE_IP, APP_SCRIPTS_PATH, APP_NAME, VG_NAME, FS_NAME = match.groups()
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')
                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in WPAR')
                  sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for WPAR: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', WPAR_SERVICE_IP: '', APP_SCRIPTS_PATH: '', APP_NAME: '', , VG_NAME: '', FS_NAME: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: WPAR variable not found in /external_var.yml')
  sys.exit(1)
