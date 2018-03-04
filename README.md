create table class(cid int primary key auto_increment,
                   caption varchar(50) not null unique
);

insert into class(caption) values("三年二班"),("一年三班"),("三年一班");




create table student(sid int primary key auto_increment,
                     sname varchar(20) not null unique,
                     gender enum("男", "女"),
                     class_id int not null,
                     foreign key (class_id) references class(cid)
)engine=innodb;


insert into student(sname, gender, class_id) values("铁蛋", "女"，1)，
("铁锤", "女"，1),("山炮", "男"，2);


create table teacher(tid int primary key auto_increment,
                     tname varchar(50) not null unique
);

insert into teacher(tname) values("波多"),("苍空"),("饭岛");

create table course(cid int primary key auto_increment,
                    cname varchar(20) not null unique,
                    teacher_id int not null ,
                    foreign key(teacher_id) references teacher(tid)
);

insert into course(cname, teacher_id) values("生物", 1),("体育", 1),("物理", 2);

create table score(sid int primary key auto_increment,
                    student_id int not null,
                    course_id int not null,
                    number int not null default 0,
                    unique(student_id, course_id),
                    foreign key(student_id) references student(sid),
                    foreign key(course_id) references course(cid)

);


insert into score(student_id, course_id, number) values(1,1,60),(1,2,59),(2,2,100);