use Academy

create table Departments
(
id int identity(1,1) not null primary key,
Financing money not null check(Financing >= 0) default(0),
Name nvarchar(100) not null check(Name != '') unique,
FacultyId int not null foreign key (FacultyId) references Faculties(Id),
)

create table Faculties
(
id int identity(1,1) not null primary key,
Name nvarchar(100) not null check(Name != '') unique,
)

create table Groups
(
id int identity(1,1) not null primary key,
Name nvarchar(10) not null check(Name != '') unique,
Year int not null check(Year between 1 and 5),
DepartmentId int not null foreign key (DepartmentId) references Departments(Id),
)

create table GroupsLectures
(
Id int identity(1,1) not null primary key,
GroupId int NOT NULL foreign key references Groups(Id),
LectureId int NOT NULL foreign key (LectureId) references Lectures(Id),
)

create table Lectures
(
Id int identity(1,1) not null primary key,
DayOfWeek int not null check(DayOfWeek between 1 and 7),
LectureRoom nvarchar(max) not null check(LectureRoom != ''),
SubjectId int not null foreign key (SubjectId) references Subjects(Id),
TeacherId int not null foreign key (TeacherId) references Teachers(Id),
)

create table Subjects
(
Id int identity(1,1) not null primary key,
Name nvarchar(100) not null check(Name != '') unique,
)

create table Teachers
(
id int identity(1,1) not null primary key,
Name nvarchar(max) not null check(Name != ''),
Salary money not null check(Salary > 0),
Surname nvarchar(max) not null check(Surname != ''),
)

select * from Departments
select * from Faculties
select * from Groups
select * from GroupsLectures
select * from Lectures
select * from Subjects
select * from Teachers



/*1.Вивести кількість викладачів кафедри «Software Development».*/ 

select count(*) as Teachers_count
from Teachers
where Id in (
    select TeacherId
    from Lectures
    where SubjectId in (
        select Id
        from Subjects
        where Name = 'Software Development'
    )
);

/*2 Вивести кількість лекцій, які читає викладач “Dave McQueen”.*/ 

select count(*) as Lectures_count
from Lectures
where TeacherId = (
    select Id
    from Teachers
    where Name = 'Dave' and Surname = 'McQueen'
);

/*3.Вивести кількість занять, які проводяться в аудиторії “D201”.*/

select count(*) as Lectures_count
from Lectures
where LectureRoom = 'D201';

/*4.Вивести назви аудиторій та кількість лекцій, що проводяться в них.*/

select LectureRoom, count(*) as Lectures_count
from Lectures
group by LectureRoom;

/*5.Вивести кількість студентів, які відвідують лекції викладача “Jack Underhill”.*/

select count(distinct gl.GroupId) as StudentCount
from GroupsLectures gl
inner join Lectures l on gl.LectureId = l.Id
inner join Teachers t on l.TeacherId = t.Id
where t.Name = 'Jack Underhill';

/*6.Вивести середню ставку викладачів факультету Computer Science.*/

select avg(Salary) as Average_Salary
from Teachers
where Id in (
    select Id
    from Departments
    where FacultyId in (
        select Id
        from Faculties
        where Name = 'Computer Science'
    )
);

/*7.Вивести мінімальну та максимальну кількість студентів серед усіх груп.*/

select min(StudentCount) as MinStudents, max(StudentCount) as MaxStudents
from (
    select gl.GroupId, count(*) as StudentCount
    from GroupsLectures gl
    inner join Groups g on gl.GroupId = g.Id
    group by gl.GroupId
) as StudentCounts;

/*8.Вивести середній фонд фінансування кафедр.*/

select avg(Financing) as Average_Financing
from Departments;

/*9.Вивести повні імена викладачів та кількість читаних ними дисциплін.*/

select Teachers.Name as Teacher_Name, Teachers.Surname as Teacher_Surname, count(*) as Disciplines_count
from Teachers
join Lectures on Teachers.Id = Lectures.TeacherId
group by Teachers.Name, Teachers.Surname;

/*10.Вивести кількість лекцій щодня протягом тижня.*/

select DayOfWeek, count(*) as Lectures_count
from Lectures
group by DayOfWeek
order by DayOfWeek;

/*11.Вивести номери аудиторій та кількість кафедр, чиї лекції в них читаються.*/

select l.LectureRoom as Auditorium, count(distinct d.Id) as DepartmentCount
from Lectures l
inner join Departments d on l.TeacherId = d.Id
group by l.LectureRoom;

/*12.Вивести назви факультетів та кількість дисциплін, які на них читаються.*/

select f.Name as FacultyName, count(distinct l.SubjectId) as DisciplineCount
from Lectures l
inner join Departments d on l.TeacherId = d.Id
inner join Faculties f on d.FacultyId = f.Id
group by f.Name;

/*13.Вивести кількість лекцій для кожної пари викладач-аудиторія.*/

select Teachers.Name as Teacher_Name, Lectures.LectureRoom as Lecture_Room, count(*) as Lectures_count
from Lectures
join Teachers on Lectures.TeacherId = Teachers.Id
group by Teachers.Name, Lectures.LectureRoom;
