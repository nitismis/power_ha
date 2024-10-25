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
TYPE_IN = ['enhanced', 'standard', 'compressed', 'large']
BLOCK_SIZE_IN = ['4096','512','1024','2048']
SIZE_PER_UNIT_IN = ['megabytes', 'gigabytes']
found_abstract = False
count = 0
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('FS:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of FS are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+TYPE:\s+(.*?),\s+VOLUME_GROUP:\s+(.*?),\s+UNITS:\s+(.*?),\s+SIZE_PER_UNIT:\s+(.*?),\s+BLOCK_SIZE:\s+(.*?)}', line)
              if match:
                  NAME, TYPE, VOLUME_GROUP, UNITS, SIZE_PER_UNIT, BLOCK_SIZE = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')
                  TYPE = TYPE.replace('\'','')
                  VOLUME_GROUP = VOLUME_GROUP.replace('\'','')
                  TYPE = TYPE.replace('\"','')
                  VOLUME_GROUP = VOLUME_GROUP.replace('\"','')
                  UNITS = UNITS.replace('\"','')
                  UNITS = UNITS.replace('\'','')
                  SIZE_PER_UNIT = SIZE_PER_UNIT.replace('\"','')
                  SIZE_PER_UNIT = SIZE_PER_UNIT.replace('\'','')
                  BLOCK_SIZE = BLOCK_SIZE.replace('\"','')
                  BLOCK_SIZE = BLOCK_SIZE.replace('\'','')

                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for FS name')
                      sys.exit(1)
                  if not TYPE.strip() or TYPE.strip() == '':
                      print('Blank values are mentioned for TYPE in FS')
                      sys.exit(1)
                  if not VOLUME_GROUP.strip() or VOLUME_GROUP.strip() == '':
                      print('Blank values are mentioned for VOLUME_GROUP in FS')
                      sys.exit(1)
                  if not UNITS.strip() or UNITS.strip() == '':
                      print('Blank values are mentioned for UNITS in FS')
                      sys.exit(1)
                  if not SIZE_PER_UNIT.strip() or SIZE_PER_UNIT.strip() == '':
                      print('Blank values are mentioned for SIZE_PER_UNIT in FS')
                      sys.exit(1)
                  if not BLOCK_SIZE.strip() or BLOCK_SIZE.strip() == '':
                      print('Blank values are mentioned for BLOCK_SIZE in FS')
                      sys.exit(1)
                  if TYPE.upper() not in [x.upper() for x in TYPE_IN]:
                      print('TYPE is not in list of valid values')
                      sys.exit(1)
                  if SIZE_PER_UNIT.strip() not in SIZE_PER_UNIT_IN:
                      print('SIZE_PER_UNIT is not in list of valid values')
                      sys.exit(1)
                  if BLOCK_SIZE.strip() not in BLOCK_SIZE_IN:
                      print('BLOCK_SIZE is not in list of valid values')
                      sys.exit(1)

                  if not UNITS.isdigit():
                      print('UNITS are not an integer value')
                      sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for FS: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', TYPE: '', VOLUME_GROUP: '', UNITS: '', SIZE_PER_UNIT: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('FS:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of FS are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+TYPE:\s+(.*?),\s+VOLUME_GROUP:\s+(.*?),\s+UNITS:\s+(.*?),\s+SIZE_PER_UNIT:\s+(.*?),\s+BLOCK_SIZE:\s+(.*?)}', line)
              if match:
                  NAME, TYPE, VOLUME_GROUP, UNITS, SIZE_PER_UNIT, BLOCK_SIZE = match.groups()
                  NAME = NAME.replace('\'','')
                  NAME = NAME.replace('\"','')

                  if not NAME.strip() or NAME.strip() == '':
                      print('Blank values are mentioned for FS name')
                      sys.exit(1)
                  
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for FS: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', TYPE: '', VOLUME_GROUP: '', UNITS: '', SIZE_PER_UNIT: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: FS variable not found in /external_var.yml')
  sys.exit(1)
