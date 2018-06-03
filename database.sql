create table courses
( id  integer primary key autoincrement,
  title text(50),
  duration int,
  fee  int
 );

insert into courses (title,duration,fee) values ('Angular',15,2000);
insert into courses (title,duration,fee) values ('Java EE',45,6000);

select * from courses
