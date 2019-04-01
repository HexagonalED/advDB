import pymysql.cursors
import json
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('punkt')
# Connect to the database
connection = pymysql.connect(host='s.snu.ac.kr',
                             port=3306,
                             db='ADB2017_20651',
                             user='ADB2017_20651',
                             password='ADB2017_20651',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

inverted_wiki_create_sql = "CREATE TABLE IF NOT EXISTS inv_wiki(term varchar(1000), id int(11));"


cur = connection.cursor()

wiki_select_sql = "SELECT * FROM wiki;"
cur.execute(wiki_select_sql)

rows = cur.fetchall()

inv_wiki_insert_sql = "INSERT INTO inv_wiki (term, id) VALUES"
cur.execute(inverted_wiki_create_sql)
for r in rows :
    token = word_tokenize(r["text"])
    token = list(set(token))
    id = str(r["id"])
    words_string = ""
    for word in token:
        words_string+=" (\""+word+"\","+id+"),"
    q=(inv_wiki_insert_sql+words_string)[:-1]+";"
    print(q)
    cur.execute(q)


    #print(token)
    #rws = word_tokenize(r)
    #print(rws)
    #cur.execute(inv_wiki_insert_sql+rws[+","+");")




