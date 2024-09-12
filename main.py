from functools import namedtuple
import sqlite3

DB_PATH = 'passwords.db'

Login = namedtuple('Login', ['site', 'username', 'password'])
PasswordPolicy = namedtuple('PasswordPolicy', 
    ['length', 'use_lowercase', 'use_uppercase', 'use_numbers', 'use_special_chars'],
    defaults=[12, 1, 1, 1, 1])

def get_logins(db_path: str='passwords.db', site: str=''):
    """Returns a list of named tuples."""
    logins = []
    try:
        # Connect to specified DB, will create it if nonexistent
        con = sqlite3.connect(db_path)
        curs = con.cursor()
        
        if site:
            logins = curs.execute(f'SELECT * FROM logins WHERE site={site};')
        else:
            logins = curs.execute('SELECT * FROM logins;').fetchall()

        con.close()
    except sqlite3.Error as error:
        print(f'An error occured when reading from DB:\n{error}')
    
    return logins

def add_logins(logins: list, db_path:str='passwords.db'):
    try:
        con = sqlite3.connect(db_path)
        curs = con.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS logins (
                site TEXT NOT NULL,
                username TEXT,
                password TEXT);
            """)
        for login in logins:
            curs.execute(
                'INSERT INTO logins (site, username, password) ' + 
                f'VALUES("{login.site}", "{login.username}", "{login.password}");')
            
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print(f'An error occured when writing to DB:\n{error}')

def generate_password():
    pass

def main():
    pass

if __name__ == '__main__':
    main()
