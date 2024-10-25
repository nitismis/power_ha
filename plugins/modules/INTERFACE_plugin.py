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
          if line.startswith('INTERFACES:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of INTERFACES are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+NETWORK:\s+(.*?),\s+NODE:\s+(.*?),\s+INTERFACE:\s+(.*?),\s+IP:\s+(.*?)}', line)
              if match:
                  NAME, NETWORK, NODE, INTERFACE, IP  = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')
                  NETWORK = NETWORK.replace('\'','')
                  NETWORK = NETWORK.replace('\"','')
                  NODE = NODE.replace('\'','')
                  NODE = NODE.replace('\"','')
                  INTERFACE = INTERFACE.replace('\'','')
                  INTERFACE = INTERFACE.replace('\"','')
                  IP = IP.replace('\'','')
                  IP = IP.replace('\"','')
                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for NAME in interface')
                      sys.exit(1)
                  if not NETWORK.strip() or NETWORK.strip() == '':
                      print('Blank values are mentioned for NETWORK in Interface')
                      sys.exit(1)
                  if not NODE.strip() or NODE.strip() == '':
                      print('Blank values are mentioned for NODE in interface')
                      sys.exit(1)
                  if not INTERFACE.strip() or INTERFACE.strip() == '':
                      print('Blank values are mentioned for INTERFACE in Interface')
                      sys.exit(1)
                  if not IP.strip() or IP.strip() == '':
                      print('Blank values are mentioned for IP in interface')
                      sys.exit(1)
                  if str(INTERFACE).strip() not in str(NAME).strip() :
                      print('INTERFACE name do not match with the Interface type')
                      sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for INTERFACE: '+str(count) + '\ncorrect keys are:')
                  print("  - {NAME: '',NETWORK: '', NODE: '', INTERFACE: '', IP: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('INTERFACES:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of INTERFACES are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+NETWORK:\s+(.*?),\s+NODE:\s+(.*?),\s+INTERFACE:\s+(.*?),\s+IP:\s+(.*?)}', line)
              if match:
                  NAME, NETWORK, NODE, INTERFACE, IP  = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')
                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for NAME in interface')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for INTERFACE: '+str(count) + '\ncorrect keys are:')
                  print("  - {NAME: '',NETWORK: '', NODE: '', INTERFACE: '', IP: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: INTERFACE variable not found in /external_var.yml')
  sys.exit(1)