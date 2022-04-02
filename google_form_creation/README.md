# Populating Google Form with PID and Name Options

In the past, we ran into problems when students would input typos when manually adding their teammates' names and PIDS. To solve this, we developed a Google Apps script that can populate a Google Form via columns of a Google Sheet.

Here is the example sheet: https://docs.google.com/spreadsheets/d/1a-ir30F9LewFuVCRPZzGKKo61LYqg8kNtqYTUxaZgWc/edit#gid=0

Here is the example form: https://docs.google.com/forms/d/1f7NrwnPOeefhM2DpcaA3P5ILVryrsI2Gj76J8ThSVWc/edit?pli=1&pli=1&no_redirect=true

## Setup and Instructions

The "Name" and "PID" column should be filled by downloading the Canvas gradebook and copying the columns to the Google Sheet. Then, using Google Sheet/Excel functions, we can fill the other columns (ie.: "Group Member #1", "Group Member #2", etc) with the values that we want as dropdown options in the Google Form.

Then, you must name the Google Form question with the same name as the Google Sheets column (ie.: "Group Member #1", "Group Member #2", etc).

From there, you can simply run the script by pressing the button that is connected to the Google Apps script.

To connect a Google Apps Script to your Google Form, go to your Google sheet, then Extensions -->  Apps Script. Use the code provided from this repo "google_apps_script.txt". We saved the code in a .txt file since its the fastest way to extract the code via copy paste (its actually a Code.gs file, using Google Scripting). 

The only modifications to the script needed are:

const GOOGLE_SHEET_NAME = "COGS 118A: Test Sheet";
const GOOGLE_FORM_ID = "1f7NrwnPOeefhM2DpcaA3P5ILVryrsI2Gj76J8ThSVWc";

...where the Google Sheet name must be replaced with the name of the sheet you are using to create the dropdown values, and the Google Form ID (which is found by taking substring/URL extension of the Google Form URL).

This script can then be connected to a "button" or drawing, by creating a shape and adding the Apps script by using the function name (ex.: populateCOGS118AGoogleForms).


## Usage

After setting up the Sheet, Apps Script, and Form, press the button to run the script!

If students enroll late, you may need to redownload the Canvas gradebook, update the Google Sheet values, and press the script button again.

## Youtube Tutorial

Here is a tutorial on the full process: https://www.youtube.com/watch?v=Z-gCwZ0lXd8
