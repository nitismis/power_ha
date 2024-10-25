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
TYPE_IN = ['original', 'big', 'scalable', 'legacy']
found_abstract = False
count = 0
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('VG:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of VG are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+NODES:\s+(.*?),\s+PHYSICAL_VOLUMES:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                  vg_name, NODES, PHYSICAL_VOLUMES, TYPE = match.groups()
                  vg_name = vg_name.replace('\'','')
                  vg_name = vg_name.replace('\"','')
                  NODES = NODES.replace('\'','')
                  PHYSICAL_VOLUMES = PHYSICAL_VOLUMES.replace('\'','')
                  NODES = NODES.replace('\"','')
                  PHYSICAL_VOLUMES = PHYSICAL_VOLUMES.replace('\"','')
                  TYPE = TYPE.replace('\"','')
                  TYPE = TYPE.replace('\'','')
                  if not vg_name.strip() or vg_name.strip() == '':
                      print('Blank values are mentioned for VG name')
                      sys.exit(1)
                  if not NODES.strip() or NODES.strip() == '':
                      print('Blank values are mentioned for NODES in VG')
                      sys.exit(1)
                  if not PHYSICAL_VOLUMES.strip() or PHYSICAL_VOLUMES.strip() == '':
                      print('Blank values are mentioned for PHYSICAL_VOLUMES in VG')
                      sys.exit(1)
                  else:
                      if TYPE.upper() not in [x.upper() for x in TYPE_IN]:
                          print('Error: TYPE value incorrect for VG '+vg_name)
                          sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for VG: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', NODES: '', PHYSICAL_VOLUMES: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('VG:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of VG are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+NODES:\s+(.*?),\s+PHYSICAL_VOLUMES:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                  vg_name, NODES, PHYSICAL_VOLUMES, TYPE = match.groups()
                  vg_name = vg_name.replace('\'','')
                  vg_name = vg_name.replace('\"','')
                  if not vg_name.strip() or vg_name.strip() == '':
                      print('Blank values are mentioned for VG name')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for VG: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', NODES: '', PHYSICAL_VOLUMES: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: VGNAMES variable not found in /external_var.yml')
  sys.exit(1)
