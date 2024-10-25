import sys
import re
import os

def main():
  str = ''
  my_dict = {}
  list_of_dicts = []
  my_variable = sys.argv[1:2]
  new_values = 'yes'
  create_delete = 'create'
  i = 0
  RG_NAME_VAR = 'ip'
  exit_count = 0
  # Define the lists of values for each key.
  list_of_values = ''

  my_variable = ''.join(my_variable)  
  
  if create_delete == 'create':
      if new_values == 'yes' or new_values == 'YES' or new_values == 'y' or new_values == 'Y':
          if os.path.exists("/etc/ansible/external_var.yml"):

            with open("/etc/ansible/external_var.yml", "r") as source_file:
              with open("/etc/ansible/external_var.yml.backup", "w") as backup_file:
                for line in source_file:
                  backup_file.write(line)
          else:
            pass

          # Clean up the input string
          my_variable = my_variable.replace('\',', '\';')
          my_variable = my_variable.replace('\'', '')
          my_variable = my_variable.replace('[{', '')
          my_variable = my_variable.replace('}]', '')

          pattern = r'(,(\w+):)'
          replacement = r';\2:'
          my_variable = re.sub(pattern, replacement, my_variable)

          # Split the input string into a list of strings, with each string representing a single key-value pair
          my_variable = my_variable.split(';')

          # Iterate over the list of strings and create a new dictionary for each key-value pair
          for item in my_variable:
            key, value = item.split(':')
            my_dict[key] = value

          if (len(my_dict[RG_NAME_VAR].strip())) == 0:
            print('Blank values are mentioned for IPs')
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
              print('Number of Values do not match with no of IPs for '+ key)
              exit_count = exit_count + 1

          if exit_count > 0:
            sys.exit(1)

          for key, values in my_dict.items():
            if key == 'ip':
              temp_val = values.split(',')
              for val in temp_val:
                regex = r" \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                if bool(re.match(regex, val)) == True:
                  pass
                else:
                  regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                  if bool(re.match(regex, val)) == True:
                    pass
                  else:
                    print(val + ' is not an IP address')
                    exit_count = exit_count + 1

          if exit_count > 0:
            sys.exit(1)


        # Appending multiple dicts to a list of dict
          first_element = list(my_dict.keys())[0]
          length = len(my_dict[first_element].split(','))

          for i in range(length):
            temp_dict = {}
            for key, value in my_dict.items():
              temp_dict[key] = value.split(',')[i]
            list_of_dicts.append(temp_dict)


        # writing the data to the file
          with open('/etc/ansible/external_var.yml', 'w') as f:
            f.write("\n##For MAPPING to /etc/hosts and /etc/cluster/rhosts\nNODE_DETAILS:\n")
            for i in range(len(list_of_dicts)):
                f.write(f"  - ip: "+list_of_dicts[i][RG_NAME_VAR].strip()+"\n")
                f.write("    full_name: "+list_of_dicts[i][' full_name'].strip()+"\n")
                f.write("    name: "+list_of_dicts[i][' name'].strip()+"\n")

        # writing the data to the file
          with open('/etc/ansible/external_var.yml', 'a') as f:
            f.write("\nNODES: ")
            for i in range(len(list_of_dicts)):
                if i == 0:
                  f.write(list_of_dicts[i][' name'].strip())
                else:
                  f.write(","+list_of_dicts[i][' name'].strip())

            print('Successful')
            sys.exit(0)
      else:
        with open('/etc/ansible/external_var.yml', "r") as f:
          for line in f:
            if re.match(r'^NODE_DETAILS:', line): 
              sys.exit(0)
          print('No previous entry for NODE_DETAILS is found.')
          sys.exit(1)    

if __name__ == '__main__':
  main()
