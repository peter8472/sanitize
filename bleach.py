'''
search the list-N database. This uses the new format
https://cfpub.epa.gov/giwiz/disinfectants/index.cfm
'''
import csvsqlite3
from pathlib import Path
'''
"EPA Registration Number" TEXT,
"Active Ingredient(s)" TEXT,
"Product Name" TEXT,
"Company" TEXT,
"Follow the disinfection directions and preparation for the following virus" TEXT,
"Contact Time (in minutes)" TEXT,
"Formulation Type" TEXT,
"Surface Type" TEXT,
"Use Site" TEXT,
"Emerging Viral Pathogen Claim?" TEXT
'''
colname = ['reg', 'ingred','name', 'company', 
        'directions', 'contact', 'forumulation', 'surface', 
        'site', 'claim']
if __name__ == "__main__":
    fn =  Path.home() / "OneDrive" / "sanitize" / "List N Tool COVID-19 Disinfectants  US EPA20201207.csv"
    maker = csvsqlite3.tablemaker("listN.sqlite")
    maker.save_to_database(fn,tablename="dis",colnames=colname)