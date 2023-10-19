### -*- coding: utf-8 -*-
### """
### Created on Mon Oct 16 15:12:29 2023 <br/>
### @author: Humphery_Ufuoma <br/>
### Project : getting data from github repositories(through selenium library) and 
### sending to google spreadsheet with gspread package
### """
# Repository on projects done with Data Epic <br/>

## This Project Utilizes the Gspread Package to push data/datasets to a Google SpreadSheet <br/>
-> Requirements to accomplish this projects are in the requirements.txt file <br/>

## input data is gotten from github repo : https://github.com/Humphery7?tab=repositories <br/>

## Process
 -> The Script uses the selenium library to get data from Github user account, data gotten are listed<br/>
    1. Repository names<br/>
    2. Language used<br/>
    3. Description of repository<br/>
    4. Datetime Repository was posted/last updated<br/>

-> After sucessful scrapping of the data from github, the data are used to create a pandas dataframe and are updated on a Google SpreadSheet using Gspread Package <br/>

## output result on spreadsheet is on : https://docs.google.com/spreadsheets/d/1omeaygKjly8K47I58mUb1hlRgU80wyXQ1iBSI1bPsdw/edit#gid=0
