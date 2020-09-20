from db import db
import users

def get_list():
    sql = "SELECT phrase from phrases"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO phrases (phrase) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return True
