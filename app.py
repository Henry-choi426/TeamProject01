from flask import *
from flask_jwt_extended import *
from dao import userDAO
from dto import *
from ast import literal_eval

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
@app.route('/selectcheckpage', methods=['get'])
def selectcheck_page():
    return render_template('04.selectCheck.html')

# 회원가입 비동기
@app.route('/signup', methods=['post'])
def new_user():
    # 하단 코드는 양식에 맞춰 수정 예정
    # 추가 할 로직 : 회원 가입 전 id 중복 여부 확인
    user1 = UserDTO(request.form.get("id"),request.form.get("pw"),request.form.get("name"),request.form.get("email"))
    msg = userDAO.userinsert(user1)
    if msg:
        return jsonify(result= request.form.get("id") +"회원가입 완료")
    else:
        return jsonify(result= request.form.get("id") +"회원가입 실패")

# 로그인 비동기
@app.route("/login", methods=['POST'])
def login_proc():
    user_id = str(request.form.get("id"))
    user_pw = str(request.form.get("pw"))
    dao = userDAO()
    ruser= literal_eval(dao.userone(user_id))
    ruser["pw"] = str(ruser["pw"])
    if user_id == ruser.get('id') and user_pw == ruser.get('pw'):
        # global bucket = OrderDTO(user_id,1,0) 장바구니 DTO 생성
        return jsonify(
            access_token=create_access_token(identity=user_id,fresh=True)
        ), 200
    else:
        return ""


# 메뉴 데이터 select
@app.route('/menu_select', methods=["post"])
def menuselect():
    menu = list()
    menu = list(request.form.keys())

    # dao 에서 가져와야 하는 것 ->  select menu_name, menu_price from menu where menu_id = :v, v = menu_id


@app.route('/user_only', methods=["post"])
@jwt_required()
def user_only():
    # print("==================")
    cur_user = get_jwt_identity()
    # print(cur_user)
    if cur_user is None:
        return ""
    else:
        return jsonify(cur_user)


if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port="5000",
            debug=True)
