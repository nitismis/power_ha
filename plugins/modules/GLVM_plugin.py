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
TYPE_IN_SYNC = ['sync']
TYPE_IN_ASYNC = ['async']
unit_of_cache_IN = ['G', 'M', 'K']
found_abstract = False
count = 0
count2 = 0
flag = 0

if create_delete == 'create_async':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('GLVM:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of GLVM are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+GLVM_name:\s+(.*?),\s+type:\s+(.*?),\s+Site1_Disk:\s+(.*?),\s+Site2_Disk:\s+(.*?),\s+cache_size:\s+(.*?),\s+unit_of_cache:\s+(.*?)}', line)
              if match:
                  GLVM_name, type, Site1_Disk, Site2_Disk, cache_size, unit_of_cache = match.groups()
                  GLVM_name = GLVM_name.replace('\'','')
                  GLVM_name = GLVM_name.replace('\"','')
                  type = type.replace('\'','')
                  Site1_Disk = Site1_Disk.replace('\'','')
                  type = type.replace('\"','')
                  Site1_Disk = Site1_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\'','')
                  cache_size = cache_size.replace('\"','')
                  cache_size = cache_size.replace('\'','')
                  unit_of_cache = unit_of_cache.replace('\"','')
                  unit_of_cache = unit_of_cache.replace('\'','')

                  if type not in TYPE_IN_ASYNC:
                      print('Error: type value incorrect for GLVM_name '+GLVM_name)
                      sys.exit(1)
                  if not GLVM_name.strip() or GLVM_name.strip() == '':
                      print('Blank values are mentioned for GLVM GLVM_name')
                      sys.exit(1)
                  if not type.strip() or type.strip() == '':
                      print('Blank values are mentioned for type in GLVM')
                      sys.exit(1)
                  if not Site1_Disk.strip() or Site1_Disk.strip() == '':
                      print('Blank values are mentioned for Site1_Disk in GLVM')
                      sys.exit(1)
                  if not Site2_Disk.strip() or Site2_Disk.strip() == '':
                      print('Blank values are mentioned for Site2_Disk in GLVM')
                      sys.exit(1)
                  if not cache_size.strip() or cache_size.strip() == '':
                      print('Blank values are mentioned for cache_size in GLVM')
                      sys.exit(1)
                  if not unit_of_cache.strip() or unit_of_cache.strip() == '':
                      print('Blank values are mentioned for unit_of_cache in GLVM')
                      sys.exit(1)
                  if unit_of_cache.strip() not in unit_of_cache_IN:
                      print('unit_of_cache is not in list of valid values')
                      sys.exit(1)

                  if not cache_size.isdigit():
                      print('cache_size are not an integer value')
                      sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for GLVM: '+str(count) + '\ncorrect keys are:')
                  print("  - { GLVM_name: '', type: '', Site1_Disk: '', Site2_Disk: '', cache_size: '', unit_of_cache: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)


if create_delete == 'create_sync':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('GLVM:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of GLVM are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+GLVM_name:\s+(.*?),\s+type:\s+(.*?),\s+Site1_Disk:\s+(.*?),\s+Site2_Disk:\s+(.*?)}', line)
              if match:
                  GLVM_name, type, Site1_Disk, Site2_Disk = match.groups()
                  GLVM_name = GLVM_name.replace('\'','')
                  GLVM_name = GLVM_name.replace('\"','')
                  type = type.replace('\'','')
                  Site1_Disk = Site1_Disk.replace('\'','')
                  type = type.replace('\"','')
                  Site1_Disk = Site1_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\'','')

                  if type not in TYPE_IN_SYNC:
                      print('Error: type value incorrect for GLVM_name '+GLVM_name)
                      sys.exit(1)
                  if not GLVM_name.strip() or GLVM_name.strip() == '':
                      print('Blank values are mentioned for GLVM GLVM_name')
                      sys.exit(1)
                  if not type.strip() or type.strip() == '':
                      print('Blank values are mentioned for type in GLVM')
                      sys.exit(1)
                  if not Site1_Disk.strip() or Site1_Disk.strip() == '':
                      print('Blank values are mentioned for Site1_Disk in GLVM')
                      sys.exit(1)
                  if not Site2_Disk.strip() or Site2_Disk.strip() == '':
                      print('Blank values are mentioned for Site2_Disk in GLVM')
                      sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for GLVM: '+str(count) + '\ncorrect keys are:')
                  print("  - { GLVM_name: '', type: '', Site1_Disk: '', Site2_Disk: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)

if create_delete == 'delete':
  with open('/external_var.yml', 'r') as f:
      for line in f:
          if line.startswith('GLVM:'):
              found_abstract = True
          elif found_abstract:
              count = count + 1
              if not line.strip():
                count = count - 1
                if count == count2:
                  print('Error: No values of GLVM are found in /external_var.yml')
                  sys.exit(1)
                else:
                  print('Validation successful')
                  sys.exit(0)
              match = re.search(r'^(?!\#)\s+\-\s+{\s+GLVM_name:\s+(.*?),\s+type:\s+(.*?),\s+Site1_Disk:\s+(.*?),\s+Site2_Disk:\s+(.*?)}', line)
              if match:
                  GLVM_name, type, Site1_Disk, Site2_Disk = match.groups()
                  GLVM_name = GLVM_name.replace('\'','')
                  GLVM_name = GLVM_name.replace('\"','')
                  type = type.replace('\'','')
                  Site1_Disk = Site1_Disk.replace('\'','')
                  type = type.replace('\"','')
                  Site1_Disk = Site1_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\"','')
                  Site2_Disk = Site2_Disk.replace('\'','')

                  if not GLVM_name.strip() or GLVM_name.strip() == '':
                      print('Blank values are mentioned for GLVM GLVM_name')
                      sys.exit(1)
                  if not type.strip() or type.strip() == '':
                      print('Blank values are mentioned for type in GLVM')
                      sys.exit(1)
                  if not Site1_Disk.strip() or Site1_Disk.strip() == '':
                      print('Blank values are mentioned for Site1_Disk in GLVM')
                      sys.exit(1)
                  if not Site2_Disk.strip() or Site2_Disk.strip() == '':
                      print('Blank values are mentioned for Site2_Disk in GLVM')
                      sys.exit(1)

              elif re.search(r'\#.*', line):
                  count2 = count2 + 1
              else:
                  print('Error: Incorrect keys found for entry in /external_var.yml for GLVM: '+str(count) + '\ncorrect keys are:')
                  print("  - { GLVM_name: '', type: '', Site1_Disk: '', Site2_Disk: ''}")
                  print("Entered keys are: ")
                  print(line)
                  sys.exit(1)
                
if not found_abstract:
  print('Error: GLVM variable not found in /external_var.yml')
  sys.exit(1)
