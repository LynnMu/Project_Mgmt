"""Create repos for project groups on Github."""

import json
import base64
from auth import *

##########################################################################################
##########################################################################################

TEAM_IDS_FILE = ''

README_CONTENT = ''
README_CONTENT = base64.b64encode(README_CONTENT)

##########################################################################################
##########################################################################################


def main():
    """   """

    # Set up params for Github API
    auth = 'Authorization: token ' + TOKEN
    repos_url = 'https://api.github.com/orgs/COGS108/repos'

    # Load project team IDs
    with open(TEAM_IDS_FILE, 'r') as fp:
        teams = json.load(fp)

    # Loop through teams
    for group, team_id in teams.items():

        # Init repository name
        repo_name = 'Pr_' + group[-3]

        # Set up repository information
        repo_dat = '{"name":"' + repo_name + '",' + \
                    '"description":"Project repo for ' + group + '",'+ \
                    '"private":true,' + \
                    '"team_id":' + team_id + '}'

        # Create repository on COGS108
        out = subprocess.run(['curl', '-XPOST', '-H', auth, repos_url, '-d', repo_dat],
                             stdout=subprocess.PIPE)

        # Initialzie URL to add a README file
        readme_url = 'https://api.github.com/repos/COGS108/' + \
                     repo_name + '/contents/README.md'

        # Set up README data
        readme_dat = '{"path": "README.md",' + \
                     '"message":"Add README to project repo.",' + \
                     '"committer":{"name":"Tom Donoghue", "email":"tdonoghue@ucsd.edu"},' + \
                     '"content":"' + README_CONTENT + '"}'

        # Add README file to group project repo
        subprocess.run(['curl', '-i', '-X', 'PUT', '-H', auth, '-d', repo_dat, readme_url],
                       stdout=subprocess.PIPE)


if __name__ == "__main__":
    main()
