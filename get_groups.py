"""Extract Project Groups from COGS108 Assignment-4"""

import os
import re
import json

##########################################################################################
##########################################################################################

FILE_DIR = '/Users/thomasdonoghue/Desktop/A4/'
GR_DIR = '/Users/thomasdonoghue/Desktop/Groups/'

##########################################################################################
##########################################################################################

def main():

    groups = dict()
    all_students = []

    files = os.listdir(FILE_DIR)
    nb_files = [f for f in files if '.ipynb' in f]

    pattern = re.compile('[A,U]\d{8}')

    n_students = 0

    for ind, nb_file in enumerate(nb_files):

        cur_group = []
        cur_name = 'Gr_' + '{0:03d}'.format(ind)

        with open(os.path.join(FILE_DIR, nb_file), 'r') as nbf:

            for line in nbf:
                if re.search(pattern, line):
                    sid = re.search(pattern, line).group()
                    cur_group.append(sid)
                    all_students.append(sid)

            if not cur_group:
                print('Empty group membership for file', nb_file)
                continue

        n_students += len(cur_group)
        groups[cur_name] = cur_group

        ## Copy over proposal to group directory

        # Create group specific directory, move notebook into it
        os.mkdir(os.path.join(GR_DIR, cur_name))
        os.rename(os.path.join(FILE_DIR, nb_file),
                  os.path.join(GR_DIR, cur_name, 'ProjectProposal.ipynb'))

        # Create txt file with group memberships
        with open(os.path.join(GR_DIR, cur_name, cur_name + '.txt'), 'w') as fp:
            for student in cur_group:
                fp.write(student + '\n')

    n_groups = len(groups)

    print('Got', n_groups, 'groups totalling', n_students, 'students.')

    # Check for any duplicate students (indicative of duplicate groups)
    if len(set(all_students)) != len(all_students):
        print('There are duplicated students!')

    # Save out group membership information
    with open('groups.json', 'w') as fp:
        json.dump(groups, fp, sort_keys=True, indent=2)

    # Save out list of students in groups
    with open('students.txt', 'w') as fp:
        for student in all_students:
            fp.write(student + '\n')

if __name__ == "__main__":
    main()
