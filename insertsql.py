#--coding:utf-8--
import psycopg2

def testsql():
	conn = psycopg2.connect(database="audio", user="postgres", password="111111", host="182.225.5.101", port="5432")

	print "Opened database successfully"

	for i in range(1,10000):
		cur = conn.cursor()
		cur.execute("sql");
		conn.commit()

	print "Insert successfully"


if __name__ == '__main__':
	testsql()