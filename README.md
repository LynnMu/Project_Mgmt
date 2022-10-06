# Project_Mgmt

Tools and utilities for managing group projects.

Each group will be created as a team on the COGS108 organization, and given a private group repo to work on. Membership is set up so that this provides access only to their own group repo (not to any other groups, or to our private repos). Instructors (as owners) have full access to all the repos - so to all the groups repos. 

The current set-up plan is to create repos, adding the group members, with a generic README, and a copy of their project proposal. 

## Setup Instructions

### Setting Up the Google Form to collect student's self created project groups

1. See google_form_creation

### After Students Complete the Google Form Submissions

2. Follow the logic in assign_project_groups.ipynb which will

    2a. Figure out who didn't signup

    2b. Assign non-signed up people to random groups
    
    2c. Create repos for each group, and give the students write access to their new repo
    
3. TAs will manually create project groups on Canvas (People->Groups) ... these groups are needed for group level grading.  In the future this should be automated from the script in step 2
