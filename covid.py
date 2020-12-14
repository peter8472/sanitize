import csvsqlite3
from pathlib import Path

if __name__ == "__main__":
    source  = Path.home() / "OneDrive"
    x = (list(source.glob("List*")))
    filename = x[0]
    print(filename)


    tbl = csvsqlite3.tablemaker("covid")
    tbl.save_to_database(filename, 'infect', fieldstring='''
    
    
    regnum TEXT, ingredients TEXT, name TEXT, company TEXT,
    virus TEXT, duration DECIMAL, forumulation TEXT, surfaces TEXT,
    sites TEXT, emergingclaim TEXT, date DATETIME'''
    
    
    , drop=True)
    # tbl.save_to_database(filename, 'columns', drop=True)
