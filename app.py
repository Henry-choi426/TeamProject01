from ast import literal_eval
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from dao import user_dao
from dto import UserDTO

app = Flask(import_name=__name__)

app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY="Teamse7en"
)

app.config['JSON_AS_ASCII'] = False

jwt = JWTManager(app)

# 첫 화면
@app.route('/', methods=['get'])
def get():
    return render_template('00.index.html')

# 회원가입 페이지
@app.route('/signuppage', methods=['get'])
def signup_page():
    return render_template('01.signUp.html')

# 로그인 페이지
@app.route('/signinpage', methods=['get'])
def signin_page():
    return render_template('02.signIn.html')

# 메뉴선택 페이지
@app.route('/menupage', methods=['get'])
def menu_page():
    return render_template('03.menuSelect.html')

# 선택 체크 페이지
@app.route('/ordercheckpage', methods=['get'])
def ordertcheck_page():
    return render_template('04.orderCheck.html')

# 회원가입 비동기
@app.route('/signup', methods=['post'])
def new_user():

    # html에서 비동기로 받은 회원가입 정보를 DB에 저장.

    user1 = UserDTO(request.form.get("id"),request.form.get("pw"),\
            request.form.get("name"),request.form.get("email"))
    msg = user_dao.user_insert(user1)
    if msg:
        return jsonify(result= "id :" +request.form.get("id") 
        +"회원가입 완료. 로그인 페이지로 이동합니다.")
    else:
        return ""

# 로그인 비동기
@app.route("/login", methods=['POST'])
def login_proc():
    user_id = str(request.form.get("id"))
    user_pw = str(request.form.get("pw"))
    dao = user_dao()
    ruser= literal_eval(dao.userone(user_id))
    ruser["pw"] = str(ruser["pw"])
    if user_id == ruser.get('id') and user_pw == ruser.get('pw'):
        return jsonify(
            access_token=create_access_token(identity=user_id,fresh=True)
        ), 200
    else:
        return ""

@app.route('/menu_select', methods=["post"])
def menuselect():
    menu = list()
    menu = list(request.form.keys())
    cnt = list()
    for i in menu:
        cnt.append(request.form.get(i))
    dic = { a:b for a, b in zip(menu, cnt) }
    data = literal_eval(user_dao.order_menu(menu))
    for key,value in dic.items():
        data[int(key)]['count'] = int(value)
    return jsonify(data)

@app.route('/order',methods=['post'])
def order_complete():
    menu = list(request.form.keys())
    cnt = list()
    for i in menu:
        cnt.append(request.form.get(i)[1:-1].split(","))
    if user_dao.order_insert(cnt):
        return "성공"
    else:
        return ""

@app.route('/user_only', methods=["post"])
@jwt_required()
def user_only():
    cur_user = get_jwt_identity()
    if cur_user is None:
        return ""
    else:
        return jsonify(cur_user)

if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port="5000",
            debug=True)
