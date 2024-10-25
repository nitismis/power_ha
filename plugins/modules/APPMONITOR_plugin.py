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
TYPE_IN = ['Custom', 'Process']
FAILUREACTION_IN = ['notify','fallover']
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('ApplicationMonitor:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of Application Monitor are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+PATH:\s+(.*?),\s+APPLICATIONS:\s+(.*?),\s+MONITORMETHOD:\s+(.*?),\s+FAILUREACTION:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                NAME, PATH, APPLICATIONS, MONITORMETHOD, FAILUREACTION , TYPE= match.groups()
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')
                PATH = PATH.replace('\'','')
                PATH = PATH.replace('\"','')
                APPLICATIONS = APPLICATIONS.replace('\'','')
                APPLICATIONS = APPLICATIONS.replace('\"','')
                MONITORMETHOD = MONITORMETHOD.replace('\'','')
                MONITORMETHOD = MONITORMETHOD.replace('\"','')
                FAILUREACTION = FAILUREACTION.replace('\'','')
                FAILUREACTION= FAILUREACTION.replace('\"','')
                TYPE = TYPE.replace('\'','')
                TYPE = TYPE.replace('\"','')

                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in Application monitor')
                  sys.exit(1)
                if not PATH.strip() or PATH.strip() == '':
                  print('Blank values are mentioned for PATH in Application monitor')
                  sys.exit(1)
                if not APPLICATIONS.strip() or APPLICATIONS.strip() == '':
                  print('Blank values are mentioned for APPLICATIONS in Application monitor')
                  sys.exit(1)
                if not MONITORMETHOD.strip() or MONITORMETHOD.strip() == '':
                  print('Blank values are mentioned for MONITORMETHOD in Application monitor')
                  sys.exit(1)
                if not FAILUREACTION.strip() or FAILUREACTION.strip() == '':
                  print('Blank values are mentioned for FAILUREACTION in Application monitor')
                  sys.exit(1)
                if not TYPE.strip() or TYPE.strip() == '':
                  print('Blank values are mentioned for TYPE in Application monitor')
                  sys.exit(1)
                if TYPE.upper() not in [x.upper() for x in TYPE_IN]:
                  print('The value of TYPE is not a valid value')
                  sys.exit(1)
                if FAILUREACTION.strip() not in FAILUREACTION_IN:
                  print('The value of FAILUREACTION is not a valid value')
                  sys.exit(1)


              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for APPLICATION MONITOR: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', PATH: '', APPLICATIONS: '', MONITORMETHOD: '', FAILUREACTION: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('ApplicationMonitor:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of Application Monitor are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+PATH:\s+(.*?),\s+APPLICATIONS:\s+(.*?),\s+MONITORMETHOD:\s+(.*?),\s+FAILUREACTION:\s+(.*?),\s+TYPE:\s+(.*?)}', line)
              if match:
                NAME, PATH, APPLICATIONS, MONITORMETHOD, FAILUREACTION , TYPE= match.groups()
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')

                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in Application monitor')
                  sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for APPLICATION MONITOR: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', PATH: '', APPLICATIONS: '', MONITORMETHOD: '', FAILUREACTION: '', TYPE: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)

                
if not found_abstract:
  print('Error: APPLICATION MONITOR variable not found in /external_var.yml')
  sys.exit(1)
