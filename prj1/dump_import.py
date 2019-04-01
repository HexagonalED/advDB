import pymysql
import pymysql.cursors
import argparse

# Connect to the database
connection = pymysql.connect(host='s.snu.ac.kr',
                             port=3306,
                             user='ADB2017_20651',
                             password='ADB2017_20651',
                             db='ADB2017_20651',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
parser = argparse.ArgumentParser()
parser.add_argument("DUMPDIR")
args = parser.parse_args()

file = open(args.DUMPDIR)

try:
    with connection.cursor() as cursor:
        for line in file:
            if line.strip():
                cursor.execute(line)
    connection.commit()

except Warning as warn:
    print(warn)
