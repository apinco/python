# Imports
import xml.etree.ElementTree as et
import sqlite3

### Start functions
# Open the itunes library, read it into a string and return the string
def read_itunes_library():
    fhandle = None
    xml_string = None
    fname = 'Library.xml'
    try:
        fhandle = open(fname)
        xml_string = fhandle.read()
        return(xml_string)
    except Exception as e:
        print("failed to open", fname)
        print(repr(e))

def get_xml_root(s):
    try:
        tree = et.parse('Library.xml')
        return(tree.getroot())

    except Exception as e:
        print("failed in get_xml_root")
        print(repr(e))

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Intialize the database, then return (conn, cur)
# conn = db connect
# cur = db cursor
def initialize_db():
    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;    
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );
    
    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );
    
    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );
    
    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, 
        rating INTEGER, 
        count INTEGER
    );
    ''')
    return(conn,cur)

# Executes an sql queury inside of a try/except block
# cur = db cursor to use for execution
# s = sql string
# p = parameters to pass in (either in a tuple, or as a string)
def execute_sql(cur, query, p):
    values = None
    if type(p) is str:
        values = (p, )
    else:
        values = p

    try:
        cur.execute(query, values)
    except Exception as e:
        print("failed on query: ", query);
        print(repr(e))
        exit()
### End Functions

(conn, cur) = initialize_db()
xml_string = read_itunes_library()
root = get_xml_root(xml_string)
# Find all data corresponding to tracks in the exported
# itunes library
all = root.findall('dict/dict/dict')
for entry in all:
    if (lookup(entry, 'Track ID') is None): continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    # Artist Table
    execute_sql(cur, 'INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', artist)
    cur.execute('select id from Artist where name = ?', (artist,))
    artist_id = cur.fetchone()[0]
    # Album Table
    execute_sql(cur, 'insert or ignore into Album (title, artist_id) values( ?, ?)', (album, artist_id))
    cur.execute('select id from Album where title = ?', (album, ))
    album_id = cur.fetchone()[0]
    # Genre Table
    execute_sql(cur, 'insert or ignore into Genre (name) values ( ? )', (genre, ))
    cur.execute('select id from Genre where name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    # Track Table
    execute_sql(cur, 'insert or replace into track (title, album_id, genre_id, len, rating, count) values ( ?, ?, ?, ?, ?, ?)', ( name, album_id, genre_id, length, rating, count ))

conn.commit()

