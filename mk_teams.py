"""Create teams of project groups on Github."""

import json

##########################################################################################
##########################################################################################

IDS_FILE = ''
GROUPS_FILE = ''

##########################################################################################
##########################################################################################

def main():
    """   """

    # Load project groups
    with open(GROUPS_FILE, 'r') as fp:
        groups = json.load(fp)

    # Load github account names
    with open(IDS_FILE, 'r') as fp:
        github_accts = json.load(fp)

    # Loop through groups
    for group, members in groups.items():

        # Get github user names for group members
        mem_ids = []
        for member in members:
            try:
                mem_ids.append(github_accts[member])
            except KeyError:
                print('No ID for', member)

        # Create Github team
        #TODO

if __name__ == "__main__":
    main()
