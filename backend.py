import sqlite3
class Market :
    def __init__(self , db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS marketing (id INTEGER PRIMARY KEY , item text , buy text , sale text , number text)")
        self.con.commit()

    def insert(self , item , buy , sale , number):
        self.cur.execute("INSERT INTO marketing VALUES(NULL , ? ,?,?,?)",(item , buy , sale , number))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM marketing ")
        rows=self.cur.fetchall()
        return rows
    
    def delete(self , id):
        self.cur.execute("DELETE FROM marketing WHERE id=?" , (id,) )
        self.con.commit()
    
    def edit(self , id , item , buy , sale , number):
        self.cur.execute("UPDATE marketing SET item=? , buy=? , sale=? , number = ? WHERE id=?",(item , buy , sale, number , id))
        self.con.commit()

    def search(self , item , buy , sale , number):
        self.cur.execute("SELECT * FROM marketing WHERE item=? or buy=? or sale=? or number = ? ",(item , buy , sale, number))
        rows=self.cur.fetchall()
        return rows