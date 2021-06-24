"""Remove repos for project groups from Github."""

import subprocess
from auth import *

###################################################################################################
###################################################################################################

N_PROJECTS = 90

###################################################################################################
###################################################################################################

def main():

    # Set up params for Github API
    auth = 'Authorization: token ' + TOKEN
    repos_url = 'https://api.github.com/repos/COGS108'
    
    #
    for num in range(0, N_PROJECTS):

        # Make full repository name
        repo_name = 'Pr_0' + "{:02d}".format(num)
        full_repo_url = repos_url + '/' + repo_name

        # Print state
        print('DELETING ', repo_name)

        # Delete repository on COGS108 Github account
        out = subprocess.run(['curl', '-XDELETE', '-H', auth, full_repo_url],
                             stdout=subprocess.PIPE)


if __name__ == '__main__':
    main()
