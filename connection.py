# set up PostgreSQL connection and load libraries
import  psycopg2
import psycopg2.extras
import sys
import pprint

def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='qua-kit'"

	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	print ("Connected!\n")

	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute("""SELECT author_id,COUNT(scenario.id) as n FROM SCENARIO GROUP BY author_id ORDER BY author_id""")
	db_count_submissions = cur.fetchall()
	td = db_count_submissions[1]
	# for row in db_count_submissions:
	# 	print(row["author_id"])


	# cursor.execute("SELECT * FROM criterion")
	# records = cursor.fetchall()
	# print(len(records))

if __name__ == "__main__":
	main()
