								 MVC_Project 2차.Mini Web Project/ 
								 프로젝트 기간 : 210621~210624/ 
								 주제 : 매장 배달주문 사이트 /
								 조원 : 최한승, 김영민, 이진의, 윤정화


# Take out KIOSK Project 
주문을 돕기 위한 KIOSK 프로그램을 만들어 보자  

## Purpose of the porject 
   *Required skills for this project : SQL/Flask/JavaScript/Ajax/JWT/HTML/CSS/Python*  
   
   습득한 기술을 바탕으로 페이지를 구성하여 Website를 만들 수 있다.

****
### Function of the KIOSK 
    ● 회원가입, 로그인, 주문확인, 결제 페이지를 볼 수 있다. 
	
### The components of the KIOSK sites
  

    ● Backend pages

        DAO - 작성된 SQL(DB)에 접촉하여 데이터를 삽입 혹은 추출 
        DTO - 데이터를 DAO로 혹은 APP으로 전달해주는 역할 
        APP - Controller 역할 URL를 바탕으로 각 메소드가 실행 될 수 있도록 하는 역할 

        SQL - 가장 기본적인 데이터를 저장 삽입 추출을 할 수 있도록 하는 저장소. 
                
                USER TABLE : 손님의 회원가입과 로그인을 관리 
                MENU TABLE : 메뉴이름과 가격을 저장 
                ORDER TABLE : 두 테이블과 주문 수량을 바탕으로 계산서 도출
                
    ● Front pages

        HTML - Backend 의 결과 값을 출력하여 보여주는 User interface pages           
            
****

### The website operation  

    1. Index Page

              Frontend : Home 기능으로 고객이 회원 가입 또는 로그인을 할 수 있는 페이지로 이동한다.

	      Backend :  고객의 응답을 받은 APP 페이지에서 회원가입 혹은 로그인 HTML 페이지로 동기이동 시켜준다. 

    2. Signup Page 

              Frontend: 고객이 회원으로 등록 할 수 있도록 하고 Signin page로 이동한다. 

              Backend : 고객이 입력시 비동기로 움직이며, 고객의 데이터는 DTO와 DAO를 통해 DB에 저장된다.


    3. Signin Page

              Frontend : 고객이 입력한 아이디와 비밀번호를 통해 로그인을 한다. 
	      		
			 실패시 Home 으로 성공시 Menu page로 이동 

              Backend : 로그인시 입력된 아이디와 비밀 번호는 저장된 DB와 비교하여 일치하는지 확인하고 
	      		
			일치시 JWT 를 통해 토큰을 발급한다.
                      
                        이 때 발급된 토큰은 Log-out 할 때 까지 Local storage에 저장된다. 
                      
         * 로그인시 발급된 토큰은 회원을 인증하는 역할로 토큰이 있는 경우만 메뉴 페이지에 넘어갈 수 있도록 한다.
	 

    4. MenuSelect Page 

              Frontend : 고객은 메뉴별 수량을 설정하고 주문한 것에 대한 가격을 확인 후 결제 할 수 있다.
	      		
			 결제 후 OrderCheck Page로 이동 

              Backend : Local storage에 저장된 토큰이 유효한지 비동기 방식으로 확인 후,
	      		
			메뉴 페이지에서 고객이 지정한 메뉴와 수량을  Session storage 에 저장한다.
	      		
			고객이 선택한 메뉴 데이터를 DAO를 통해 DB에서 가격 정보를 추출한다. 
                      
             		1) 장바구니 조회: 고객에게서 얻은 메뉴와 수량, DB 에서 추출한 가격 정보를 
			
			바탕으로 Total Price를 구해 HTML에 테이블 형식으로 출력한다. 
			 
			2) 결제 : 결제버튼은 클릭 시 저장된 토큰을 확인 한 후 주문내역을 DB에 저장한다. 
			
			이후 OrderCheck page로 동기 방식으로 이동한다.
			 


    5. OrderCheck Page 

              Fronted : 고객은 결제를 확인하고 다시 Login 페이지로 돌아간다.

              Backend : 로그아웃 버튼을 클릭하면 Local Storage에 저장된 토큰이 삭제 되고
	      	
			Login 페이지로 이동한다. 
*****
### The difficulites or limitations of the project

    - asdf;lasjd;
