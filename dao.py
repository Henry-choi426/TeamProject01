import cx_Oracle
from dto import UserDTO
import json
import collections


class userDAO:

    def ordermenu(menu_id):
        data = "{"
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                print(menu_id)
                # (1,2,3) -> str
                for i in menu_id:
                    i = int(i)
                    cur.execute("select menu_name, menu_price from menu where menu_id in :m", m=i)
                    row = cur.fetchone()  
                    data += str(i)+':{"name":"' + row[0] + '", "price":' + str(row[1]) + '},'
                data = data[0:-1]+"}"
                # print(data)
                # data =json.dumps(data, ensure_ascii=False)   
                # print(data)
            except Exception as e:
                print(e) 
        finally:
            cur.close() 
            conn.close()
        return data

    def order_insert(menu):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("insert into order_t values (seq_order_01.nextval, :user_id, :menu_id, :order_count)", user_id=menu[0][0], menu_id=int(menu[0][1]), order_count=int(menu[0][2]))
                cnt = 1
                for i in range(1,len(menu)):
                    cur.execute("insert into order_t values (seq_order_01.currval, :user_id, :menu_id, :order_count)", user_id=menu[i][0], menu_id=int(menu[i][1]), order_count=int(menu[i][2]))
                conn.commit()
                cur.close()
                conn.close()
                return "성공"
            except Exception as e:
                cur.close()
                conn.close()
                print("실패")
                return ""
        except Exception as e:
            cur.close()
            conn.close()
            print("실패")
            return ""


    # 회원가입 로직
    def userinsert(dto1):
        try:
            conn=cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur=conn.cursor()
            try:
                cur.execute("insert into user_t values (:user_id, :user_pw, :user_name, :user_email)",
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
    def userone(self, user_id):
        data=""
        try:
            conn=cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur=conn.cursor()

            try:
                cur.execute("select * from user_t where user_id=:v", v=user_id)
                row=cur.fetchone()
                data='{"id":"' + row[0] + '", "pw":' + str(row[1]) + '}'
            except Exception as e:
                print(e)
        finally:
            cur.close()
            conn.close()

        return data

    def userSearch(self, userid):
        try:
            conn=cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur=conn.cursor()
            try:
                cur.execute(
                    "select userid, username, useremail from user where userid=:userid", userid=userid)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        return '{userid":' + str(cur.fetchone()[1]) + ', "username":' + str(cur.fetchone()[2]) + ', "useremail":' + str(cur.fetchone()[3]) + '}'

    def userUpdate(self, dto):
            try:
                conn=cx_Oracle.connect(
                    user="SCOTT", password="TIGER", dsn="xe")
                cur=conn.cursor()
                try:
                    cur.execute("update user set userid=:userid, username=:username, useremail=:useremail, userpassword=:userpassword", userid=dto.getUserid(
                    ), username=dto.getUsername(), useremail=dto.getUseremail(), userpassword=dto.getUserpassword())
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
                conn=cx_Oracle.connect(
                    user="SCOTT", password="TIGER", dsn="xe")
                cur=conn.cursor()
                try:
                    cur.execute(
                        "delete from user where userid=:userid", userid=userid)
                    conn.commit()
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
            finally:
                cur.close()
                conn.close()

if __name__ == '__main__':
    # userDAO.ordermenu({"1", "2", "3"})
    userDAO.order_insert([['test', '3', '3'], ['test', '4', '2']])