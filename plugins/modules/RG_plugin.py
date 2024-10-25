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
cl_type = sys.argv[2]
STARTUP = ['OHN', 'OFAN', 'OAAN', 'OUDP']
FALLOVER = ['FNPN', 'FUDNP', 'BO']
FALLBACK = ['NFB', 'FBHPN']
SITE_POLICY = ['ignore', 'primary', 'either', 'both']
found_abstract = False
count = 0
count2 = 0
flag = 0

if create_delete == 'create':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('RGNAMES:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of RG are found in RGNAMES in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+name:\s+(.*?),\s+STARTUP:\s+(.*?),\s+FALLOVER:\s+(.*?),\s+FALLBACK:\s+(.*?),\s+SITE_POLICY:\s+(.*?)}', line)
              if match:
                  print(match.groups())
                  rg_name, startup, fallover, fallback, site_policy = match.groups()
                  rg_name = rg_name.replace('\'','')
                  rg_name = rg_name.replace('\"','')
                  startup = startup.replace('\'','')
                  fallover = fallover.replace('\'','')
                  startup = startup.replace('\"','')
                  fallover = fallover.replace('\"','')
                  fallback = fallback.replace('\"','')
                  fallback = fallback.replace('\'','')
                  if cl_type == 'site':
                      site_policy = site_policy.replace('\"','')
                      site_policy = site_policy.replace('\'','')
                  if not rg_name.strip() or rg_name.strip() == '':
                      print('Blank values are mentioned are mentioned for RG name')
                      sys.exit(1)
                  else:
                      if startup not in STARTUP:
                          print('Error: startup value incorrect for RG '+rg_name)
                          sys.exit(1)
                      if fallover not in FALLOVER:
                          print('Error: fallover value incorrect for RG '+rg_name)
                          sys.exit(1)
                      if fallback not in FALLBACK:
                          print('Error: fallback value incorrect for RG '+rg_name)
                          sys.exit(1)  
                      if (cl_type == 'site') and (site_policy not in SITE_POLICY):
                          print('Error: SITE POLICY value incorrect for RG '+rg_name)
                          sys.exit(1) 
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for RG: '+str(count) + '\ncorrect keys are:')
                  print("  - { name: '', STARTUP: '', FALLOVER: '', FALLBACK: '', SITE_POLICY: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
else:
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('RGNAMES:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of RG are found in RGNAMES in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+name:\s+(.*?),\s+STARTUP:\s+(.*?),\s+FALLOVER:\s+(.*?),\s+FALLBACK:\s+(.*?)}', line)
              if match:
                  rg_name, startup, fallover, fallback = match.groups()
                  rg_name = rg_name.replace('\'','')
                  rg_name = rg_name.replace('\"','')
                  if not rg_name.strip() or rg_name.strip() == '':
                      print('Blank values are mentioned are mentioned for RG name')
                      sys.exit(1)
              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for RG: '+str(count) + '\ncorrect keys are:')
                  print("  - { name: '', STARTUP: '', FALLOVER: '', FALLBACK: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: RGNAMES variable not found in /external_var.yml')
  sys.exit(1)
