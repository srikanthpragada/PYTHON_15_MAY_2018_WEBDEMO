create table courses
( id  integer primary key autoincrement,
  title text(50),
  duration int,
  fee  int
 );

create table topics
( id  integer primary key autoincrement,
  courseid integer references courses(id) on delete cascade,
  topic text(50),
  duration int
 );


insert into courses (title,duration,fee) values ('Angular',15,2000);
insert into courses (title,duration,fee) values ('Java EE',45,6000);

insert into topics(courseid, topic, duration)  values(1,'TypeScript',4);
insert into topics(courseid, topic, duration)  values(1,'DataBinding',6)

insert into topics(courseid, topic, duration)  values(2,'JDBC',5);
insert into topics(courseid, topic, duration)  values(2,'Servlets',5)



select * from courses
