-- 1. 필요 테이블
--     user
--         user_id varchar2(15) primary key
--         user_pw varchar2(15) not null
--         user_name varchar2(10) not null,
--         user_email varchar2(20) not null -> id 생성 시 정규표현식 사용 여부
drop table user_t;
create table user_t(
    user_id varchar2(15) primary key,
    user_pw varchar2(15) not null,
    user_name varchar2(10) not null
    user_email varchar2(20) not null
);
insert into menu values('id','pw','이름','email'); -- 데  
insert into user_t values('11','11','나야','lee@gmail.com');    
insert into user_t values('22','11','가야','lee@gmail.com');    
insert into user_t values('33','11','다야','lee@gmail.com');    
insert into user_t values('44','11','라야','lee@gmail.com');    
insert into user_t values('55','11','마야','lee@gmail.com');    
--     menu
--         mid number(4) 시퀀스 primary key
--         mname   varchar2(20)    not null
--         mprice  number(8) not null
drop sequence seq_menu_01;
create sequence seq_menu_01;
drop table menu;
create table menu(
    menu_id number(4) primary key,
    menu_name varchar2(20) not null,
    menu_price number(8) not null
);
insert into menu values(seq_menu_01.nextval,'Cafe_De_Olla', 8000); 
insert into menu values(seq_menu_01.nextval,'Café_Toba_Mist', 7000); 
insert into menu values(seq_menu_01.nextval,'Coffee_in_Venice', 5000 ); 
insert into menu values(seq_menu_01.nextval,'Sidamo_Mountain_Coffee',6000); 


--     order
--         order_id number(4) 시퀀스 primary key
--         user_id varchar2(15) foreign key
--         menu_id number(4) foreign key
--         order_count number(2) not null
drop sequence seq_order_01;
create sequence seq_order_01;
drop table order_t;
create table order_t(
    order_id number(4),
    user_id varchar2(20) constraint fk_order_user_id references user_t(user_id),
    menu_id number(4) constraint fk_order_menu_id references menu(menu_id),
    order_count number(2) not null,
    primary key(order_id,menu_id)
);
insert into order_t values(seq_order_01.nextval,11,1,3);
insert into order_t values(seq_order_01.nextval,22,1,6);
insert into order_t values(seq_order_01.nextval,33,2,4);
insert into order_t values(seq_order_01.nextval,44,3,2);
insert into order_t values(seq_order_01.nextval,55,3,2);
insert into order_t values(seq_order_01.nextval,55,1,2);
insert into order_t values(seq_order_01.nextval,55,2,2);
insert into order_t values(1,55,2,2);
insert into order_t values(1,55,3,2);
-- 2. 필요 view
--     order_view - inner join menu order
--         oid
--         uid

-- drop view order_com;
-- create view order_com
-- as select o.order_id, o.user_id, menu_price*order_count as total_price
-- from order_t o, menu m
-- where o.menu_id= m.menu_id;


drop view order_com;
create view order_com
as select order_id, user_id, sum(menu_price*order_count) as total_price
from order_t o, menu m
where o.menu_id= m.menu_id
group by order_id, user_id 
order by order_id;




-- create view order_com 
-- as select o.user_id, sum(menu_price*order_count)
-- from order_t o, menu m
-- where o.menu_id= m.menu_id
-- group by user_id;


-- Select order_id, sum(total_price) 
-- from order_com
-- group by order_id;


-- Select  user_id, sum(total_price) 
-- from order_com
-- group by user_id;