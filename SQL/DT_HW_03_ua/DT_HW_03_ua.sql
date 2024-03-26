use Academy

create table Groups
(
id int identity(1,1) not null primary key,
Name nvarchar(10) not null check(Name != '') unique,
Rating int not null check(Rating between 0 and 5),
Year int not null check(Year between 1 and 5),
)

create table Departments
(
id int identity(1,1) not null primary key,
Financing money not null check(Financing >= 0) default(0),
Name nvarchar(100) not null check(Name != '') unique,
)

create table Faculties
(
id int identity(1,1) not null primary key,
Dean nvarchar(max) not null check(Dean != ''),
Name nvarchar(100) not null check(Name != '') unique,
)

create table Teachers
(
id int identity(1,1) not null primary key,
EmploymentDate date not null check(EmploymentDate >= '01.01.1990'),
IsAssistant bit not null default(0),
IsProfessor bit not null default(0),
Name nvarchar(max) not null check(Name != ''),
Position nvarchar(max) not null check(Position != ''),
Premium money not null check(Premium >= 0) default(0),
Salary money not null check(Salary > 0),
Surname nvarchar(max) not null check(Surname != ''),
)

select * from Groups
select * from Departments
select * from Faculties
select * from Teachers

/*1*/select Name, Financing, Id from Departments order by Name desc
/*2*/select Name as 'Group Name', Rating as 'Group Rating' from Groups
/*3*/select Surname, cast(Salary/Premium*100 as int) as 'Rate/Premium (%)', convert(int, Salary/(Salary+Premium)*100) as 'Rate/Salary (%)' from Teachers 
/*4*/ select 'The dean of faculty ' + Name + ' is ' + dean + '. ' as 'Deans of faculties' from Faculties
/*5*/select Surname from Teachers where IsProfessor = 1 and Salary > 1050
/*6*/select Name from Departments where Financing between 11000 and 25000
/*7*/select Name from Faculties where Name != 'Computer Science'
/*8*/select Surname, Position from Teachers where IsProfessor = 0
/*9*/select Surname, Position, Salary, Premium from Teachers where IsAssistant = 1 and Premium between 160 and 550
/*10*/select Surname, Position from Teachers where IsAssistant = 1
/*11*/select Surname, Position from Teachers where year(EmploymentDate) <= 2020
/*12*/select Name as "Name of Department" from Departments where Name < 'Software Development'
order by Name
/*13*/select Surname from Teachers where IsAssistant = 1 and Salary+Premium <= 1200
/*14*/select Name from Groups where Year = 5 and Rating between 2 and 4
/*15*/select Surname from Teachers where IsAssistant = 1 and Salary between 200 and 550