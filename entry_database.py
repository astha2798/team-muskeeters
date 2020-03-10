import pymysql
db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='demodb')
def entry_database(query1):
    cursor=db.cursor()
    cursor.execute(query1)
    db.commit()
sql=""" update attendance SET outcounter = outcounter+1 where id = "1" """
sql1=""" update attendance SET incounter = incounter+1 where id = "1" """
entry_database(sql)