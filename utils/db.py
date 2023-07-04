import sqlite3

def create_connection(db_file):
    """
    Creates a connection to the SQLite database specified by db_file.

    :param db_file: Path to the SQLite file.
    :return: Connection object or None.
    """

    try:
        conn = sqlite3.connect(db_file)
        # Enable foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except sqlite3.Error as e:
        print(e)

    return None

def update_database(conn: sqlite3.Connection, file: str):
    """
    Executes all commands in the file provided as an argument on the database.

    Commands in the `file` should be separated by a semicolon.

    :param conn: Connection to the database.
    :type conn: sqlite3.Connection
    :param file: Path to the file containing the queries.
    :type file: str
    """

    # Read the file and split queries into an array
    sqlQueries = []

    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split(";")

    # Execute all queries in the array
    cursor = conn.cursor()
    for query in sqlQueries:
        cursor.execute(query)

    # Commit the changes
    conn.commit()