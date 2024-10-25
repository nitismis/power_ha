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
TYPE_IN = ['XD_data', 'XD_ip', 'ether']
count = 0
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('NETWORK:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of NETWORK are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                  NAME, TYPE = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')
                  TYPE = TYPE.replace('\'','')
                  TYPE = TYPE.replace('\"','')
                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for NAME in NETWORK')
                      sys.exit(1)
                  if not TYPE.strip() or TYPE.strip() == '':
                      print('Blank values are mentioned for TYPE in NETWORK')
                      sys.exit(1)
                      sys.exit(1)
                  if TYPE.upper() not in [x.upper() for x in TYPE_IN]:
                      print('TYPE is not in list of valid values for Network  '+NAME)
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for NETWORK: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('NETWORK:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of NETWORK are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                  NAME, NETWORK = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')
                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for NAME in NETWORK')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for NETWORK: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: NETWORK variable not found in /external_var.yml')
  sys.exit(1)
