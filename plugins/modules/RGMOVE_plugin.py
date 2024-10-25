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
          if line.startswith('RGMOVE:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of RGMOVE are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+FROM:\s+(.*?),\s+TO:\s+(.*?)}', line)
              if match:
                  RG_NAME, FROM, TO = match.groups()
                  RG_NAME = RG_NAME.replace('\'','')
                  RG_NAME = RG_NAME.replace('\"','')
                  FROM = FROM.replace('\'','')
                  FROM = FROM.replace('\'','')
                  TO = TO.replace('\"','')
                  TO = TO.replace('\"','')
                  if not RG_NAME.strip() or RG_NAME.strip() == '':
                      print('Blank values are mentioned for RGNAME in RG MOVE')
                      sys.exit(1)
                  if not FROM.strip() or FROM.strip() == '':
                      print('Blank values are mentioned for FROM in RG MOVE')
                      sys.exit(1)
                  if not TO.strip() or TO.strip() == '':
                      print('Blank values are mentioned for TO in RG MOVE')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for RG MOVE: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', FROM: '', TO: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('RGMOVE:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of RGMOVE are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+RG_NAME:\s+(.*?),\s+FROM:\s+(.*?),\s+TO:\s+(.*?)}', line)
              if match:
                  RG_NAME, FROM, TO = match.groups()
                  RG_NAME = RG_NAME.replace('\'','')
                  RG_NAME = RG_NAME.replace('\"','')
                  if not RG_NAME.strip() or RG_NAME.strip() == '':
                      print('Blank values are mentioned for RGNAME in RG MOVE')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for RG MOVE: '+str(count) + '\ncorrect keys are:')
                  print("  - { RG_NAME: '', FROM: '', TO: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
if not found_abstract:
  print('Error: RG MOVE variable not found in /external_var.yml')
  sys.exit(1)
