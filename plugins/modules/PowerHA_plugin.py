############################################
#  Capgemini_PROLOG_BEGIN_TAG
#  This is an automatically generated prolog.
#
#  Copyright (C) Capgemini Engineering ACT S.A.S. 2016-2023. All rights reserved.
#
#  Capgemini_PROLOG_END_TAG
###########################################

import sys
import re

def main():
  str = ''
  my_dict = {}
  list_of_dicts = []
  my_variable = sys.argv[1:2]
  new_values = sys.argv[2]
  i = 0
  RG_NAME_VAR = 'PHA_BUILD'
  exit_count = 0
  # Define the lists of values for each key.
  list_of_values = ''
  my_variable = ''.join(my_variable) 
  if new_values == 'yes' or new_values == 'YES' or new_values == 'y' or new_values == 'Y':
      # Clean up the input string
      my_variable = my_variable.replace('\',', '\';')
      my_variable = my_variable.replace('\'', '')
      my_variable = my_variable.replace('[{', '')
      my_variable = my_variable.replace('}]', '')

      # Split the input string into a list of strings, with each string representing a single key-value pair
      my_variable = my_variable.split(';')

      # Iterate over the list of strings and create a new dictionary for each key-value pair
      for item in my_variable:
        key, value = item.split(':')
        my_dict[key] = value

      if (len(my_dict[RG_NAME_VAR].strip())) == 0:
        print('Blank values are mentioned for RG_MOVE ')
        sys.exit(1)

      for key, values in my_dict.items():
        if not values or values == ' ':
          print('Blank values are mentioned for '+key)
          exit_count = exit_count + 1

      if exit_count > 0:
        sys.exit(1)

      # Check if number of all the values is the same 
      num_values = len(my_dict[RG_NAME_VAR].split(','))
      for key, values in my_dict.items():
        if len(values.split(',')) != num_values:
          print('Number of Values do not match with no of RGs for '+ key)
          exit_count = exit_count + 1

      if exit_count > 0:
        sys.exit(1)
#      print("length check is done")

    # Appending multiple dicts to a list of dict
      first_element = list(my_dict.keys())[0]
      length = len(my_dict[first_element].split(','))

      for i in range(length):
        temp_dict = {}
        for key, value in my_dict.items():
          temp_dict[key] = value.split(',')[i]
        list_of_dicts.append(temp_dict)

    # writing the data to the file
      with open('/external_var.yml', 'a') as f:
        f.write("\n## PowerHA Absolute Build Path datils\nPOWERHA_BLD_PATH:\n")
        for i in range(len(list_of_dicts)):
            f.write(f"  - PHA_BUILD: "+list_of_dicts[i][RG_NAME_VAR].strip()+"\n")
        print('Successful')
        sys.exit(0)
  else:
    with open('/external_var.yml', "r") as f:
      for line in f:
        if 'MOUNT_DETAILS:' in line: 
          sys.exit(0)
      print('No previous entry for PowerHA NFS mount details are not found.')
      sys.exit(1)    

if __name__ == '__main__':
  main()
