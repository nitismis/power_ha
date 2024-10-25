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
          if line.startswith('ApplicationController:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of Application Controller are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+PATH:\s+(.*?),\s+STARTSCRIPT:\s+(.*?),\s+STOPSCRIPT:\s+(.*?)}', line)
              if match:
                NAME, PATH, STARTSCRIPT, STOPSCRIPT = match.groups()
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')
                PATH = PATH.replace('\'','')
                PATH = PATH.replace('\"','')
                STARTSCRIPT = STARTSCRIPT.replace('\'','')
                STARTSCRIPT = STARTSCRIPT.replace('\"','')
                STOPSCRIPT = STOPSCRIPT.replace('\'','')
                STOPSCRIPT = STOPSCRIPT.replace('\"','')
                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in Application controller')
                  sys.exit(1)
                if not PATH.strip() or PATH.strip() == '':
                  print('Blank values are mentioned for PATH in Application controller')
                  sys.exit(1)
                if not STARTSCRIPT.strip() or STARTSCRIPT.strip() == '':
                  print('Blank values are mentioned for STARTSCRIPT in Application controller')
                  sys.exit(1)
                if not STOPSCRIPT.strip() or STOPSCRIPT.strip() == '':
                  print('Blank values are mentioned for STOPSCRIPT in Application controller')
                  sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for APPLICATION CONTROLLER: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', PATH: '', STARTSCRIPT: '', STOPSCRIPT: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('ApplicationController:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of Application Controller are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+NAME:\s+(.*?),\s+PATH:\s+(.*?),\s+STARTSCRIPT:\s+(.*?),\s+STOPSCRIPT:\s+(.*?)}', line)
              if match:
                NAME, PATH, STARTSCRIPT, STOPSCRIPT = match.groups()
                NAME = NAME.replace('\'','')
                NAME = NAME.replace('\"','')
                if not NAME.strip() or NAME.strip() == '':
                  print('Blank values are mentioned for NAME in Application controller')
                  sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for APPLICATION CONTROLLER: '+str(count) + '\ncorrect keys are:')
                  print("  - { NAME: '', PATH: '', STARTSCRIPT: '', STOPSCRIPT: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: APPLICATION CONTROLLER variable not found in /external_var.yml')
  sys.exit(1)
