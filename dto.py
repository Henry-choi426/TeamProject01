# 사원 정보를 보유하게 되는 구조의 클래스 
# 객체(복합 데이터)

class UserDTO:
    def __init__(self, newuser_id, newuser_pw, newuser_name,newuser_email):
        self.user_id = newuser_id
        self.user_pw = newuser_pw
        self.user_name = newuser_name
        self.user_email = newuser_email

    def getuser_id(self):
        return self.user_id
    
    def setuser_id(self, newuser_id):
        self.user_id = newuser_id

    def getuser_pw(self):
        return self.user_pw
    
    def setuser_pw(self, newuser_pw):
        self.user_pw = newuser_pw

    def getuser_name(self):
        return self.user_name
    
    def setuser_name(self, newuser_name):
        self.user_name = newuser_name

    def getuser_email(self):
        return self.user_email
    
    def setuser_email(self, newuser_email):
        self.user_email = newuser_email

    def __str__(self):
        return 'id : ' + self.user_id + '- pw : ' + self.user_pw + '- 이름 : ' + self.user_name + '- email : ' + self.user_email


class menuDTO:
    def __init__(self, menuid, menuname, menuprice):
        self.menuid = menuid
        self.menuname = menuname
        self.menuprice = menuprice

    def getMenuid(self):
        return self.menuid
    
    def setMenuid(self, newmenuid):
        self.menuid = newmenuid

    def getMenuname(self):
        return self.menuname

    def setMenuname(self, newmenuname):
        self.menuname = newmenuname

    def getMenuprice(self):
        return self.menuprice

    def setMenuprice(self, newmenuprice):
        self.menuprice = newmenuprice


class orderDTO:
    def __init__(self, orderid, userid, menuid, orderquantity):
        self.orderid = orderid
        self.userid = userid
        self.menuid = menuid
        self.orderquantity = orderquantity

    def getOrderid(self):
        return self.orderid

    def setOrderid(self, neworderid):
        self.orderid = neworderid

    def getUserid(self):
        return self.orderid

    def setUserid(self, newuserid):
        self.userid = newuserid

    def getMenuid(self):
        return self.menuid

    def setMenuid(self, newmenuid):
        self.menuid = newmenuid

    def getOrderquantity(self):
        return self.orderquantity

    def setOrderquantity(self, neworderquantity):
        self.orderquantity = neworderquantity
