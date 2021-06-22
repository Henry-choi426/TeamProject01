import cx_Oracle
from dto import UserDTO
import json, collections

class userDAO:

    # 회원가입 로직
    def userinsert(dto1):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("insert into usert values (:user_id, :user_pw, :user_name, :user_email)",
                            user_id=dto1.getuser_id(), user_pw=dto1.getuser_pw(), user_name=dto1.getuser_name(), user_email=dto1.getuser_email())
                print("---------------")
                conn.commit()
                cur.close()  
                conn.close()
                return "회원가입 완료"
            except Exception as e:  
                cur.close()  
                conn.close()
                return ""
        except Exception as e:  
            cur.close()  
            conn.close()
            return ""

    # 로그인 로직
    def userone(self,user_id):
        data = ""
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from usert where user_id=:v", v=user_id)
                row = cur.fetchone()  
                data = '{"id":"' + row[0] + '", "pw":' + str(row[1]) + '}'
            except Exception as e: 
                print(e) 
        finally:
            cur.close()  
            conn.close()

        return data

    def userSearch(self, userid):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select userid, username, useremail from user where userid=:userid", userid=userid)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        return '{userid":' + str(cur.fetchone()[1]) + ', "username":' + str(cur.fetchone()[2]) +', "useremail":' + str(cur.fetchone()[3]) +'}'

    def userUpdate(self, dto):
            try:
                conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
                cur = conn.cursor()
                try:
                    cur.execute("update user set userid=:userid, username=:username, useremail=:useremail, userpassword=:userpassword", userid=dto.getUserid(), username=dto.getUsername(), useremail=dto.getUseremail(), userpassword=dto.getUserpassword())
                    conn.commit()
                except Exception as e:
                    print(e) 
            except Exception as e:
                print(e)
            finally:
                cur.close() 
                conn.close()

    def userDelete(self, userid):
            try:
                conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
                cur = conn.cursor()
                try:
                    cur.execute("delete from user where userid=:userid", userid=userid)
                    conn.commit()
                except Exception as e:
                    print(e) 
            except Exception as e:
                print(e)
            finally:
                cur.close()
                conn.close()

if __name__ == '__main__':
    print(userDAO.userone('test'))