import sqlite3
import re

def get_org(line):
    email = re.findall('\S*@(\S*)', line)
    return(email[0])

def create_db():
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
    return (conn, cur)

# Open the fix
fhandle = open('mbox.txt')
(conn, cur) = create_db()
for line in fhandle:
    if not line.startswith('From:'):
        continue
    org = get_org(line)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()
