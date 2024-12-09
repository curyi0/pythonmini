create table g_univ(	
	idx number primary key, 
	sigun varchar2(20) not null, 
	faclt varchar2(100) not null, 
	addr varchar2(200) not null, 
	latitude number(20,10) not null, 
	longitude number(20,10) not null
); 

create sequence myboard_seq
  increment by 1
  start with 1
  minvalue 1
  nomaxvalue
  nocycle
  nocache;  
--delete from g_univ;
commit;

create table Kdeliver(
    idx number primary key,
    SIGUN_NM VARCHAR2(20) NOT NULL, 
    SNAME VARCHAR2(100) NULL,
    ADDR VARCHAR2(120)  NULL,
    INDUTYPE VARCHAR2(50),
    LATITUDE number(20,10),
    LONGITUDE number(20,10)
);