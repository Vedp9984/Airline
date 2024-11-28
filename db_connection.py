import pymysql

def connect_to_db(username, password):
    try:
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db='AIRLINE',
                              cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        return con, cur
    except Exception as e:
        print(e)
        return None, None
