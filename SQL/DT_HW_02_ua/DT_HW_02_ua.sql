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
Name nvarchar(100) not null check(Name != '') unique,
)

create table Teachers
(
id int identity(1,1) not null primary key,
EmploymentDate date not null check(EmploymentDate >= '01.01.1990'),
Name nvarchar(max) not null check(Name != ''),
Premium money not null check(Premium >= 0) default(0),
Salary money not null check(Salary > 0),
Surname nvarchar(max) not null check(Surname != ''),
)