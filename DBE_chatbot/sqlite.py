import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cur.execute("CREATE TABLE `rule_codes` (  `id` int(11) PRIMARY KEY,  `rule_name` varchar(200) DEFAULT NULL,  `rule_code` varchar(100) DEFAULT NULL,  `rule_description` varchar(500) DEFAULT NULL,  `severity` varchar(15) DEFAULT NULL,  `error_type` varchar(100) DEFAULT NULL,  `le_allowed` varchar(100) DEFAULT NULL,  `document_owner` varchar(100) DEFAULT NULL,  `link` varchar(200) DEFAULT NULL,  `jira_issues` varchar(100) DEFAULT NULL,  `document_status` varchar(40) DEFAULT NULL,  `product` varchar(50) DEFAULT NULL,  `rule_label` varchar(200) DEFAULT NULL) ;")
    #cur.execute("DROP TABLE rule_codes;")
    #cur.execute("""UPDATE rule_codes SET link = '<a href = https://confluence.in.here.com' || link || 'target="_blank">' || rule_code || '</a>';""")
    cur.execute("""UPDATE    rule_codes SET       link = REPLACE(link, 'target="_blank"', ' target="_blank"')""")
    
    rows = cur.fetchall()

    for row in rows:
        print(row)



def main():
    database = r"C:\Users\saseendr\Desktop\DBE_chatbot\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        

        print("2. Query all tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()