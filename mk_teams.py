"""Create teams of project groups on Github."""

import json
import subprocess
from auth import *

##########################################################################################
##########################################################################################

GIT_IDS_FILE = '/Users/SP/Documents/05-COGS108/108GitOrg/Utilities/grading/A1/git_ids.json'
GROUPS_FILE = 'groups.json'

##########################################################################################
##########################################################################################

def main():
    """   """

    # Set up params for Github API
    auth = 'Authorization: token ' + TOKEN
    teams_url = 'https://api.github.com/orgs/COGS108/teams'

    # Load project groups
    with open(GROUPS_FILE, 'r') as fp:
        groups = json.load(fp)

    # Load github account names
    with open(GIT_IDS_FILE, 'r') as fp:
        github_accts = json.load(fp)

    # Initialize dictionary to save team IDs
    teams_ids = dict()

    # Loop through groups
    for group, members in groups.items():

        # Get github user names for group members
        mem_ids = []
        for member in members:
            try:
                mem_ids.append(github_accts[member])
            except KeyError:
                print('No ID for', member)

        # Set up description for team
        team_params = '{"name":"' + group + \
                      '", "description":"Project team for ' + group + '"}'

        # Create Github team
        out = subprocess.run(['curl', '-XPOST', '-H', auth, teams_url,
                             '-d', team_params], stdout=subprocess.PIPE)

        # Get new team Github id, add to dictionary
        team_id = json.loads(out.stdout)['id']
        teams_ids[group] = team_id

        # Add members to team
        for mem_id in mem_ids:

            # Built the URL for current student and team
            mem_url = 'https://api.github.com/teams/' + str(team_id) + \
                      '/memberships/' + mem_id

            # Add the current student to github team
            out = subprocess.run(['curl', '-XPUT', '-i', '-H', auth,  mem_url],
                                 stdout=subprocess.PIPE)

    # Save out team ids
    with open('team_ids.json', 'w') as fp:
        json.dump(teams_ids, fp, sort_keys=True, indent=2)


if __name__ == "__main__":
    main()
