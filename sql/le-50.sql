-- 1661. Average Time of Process per Machine


Create table If Not Exists Activity (machine_id int, process_id int, activity_type varchar, timestamp float);

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '0.712');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'end', '1.52');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '3.14');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '4.12');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '0.55');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '1.55');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'start', '0.43');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '1.42');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'start', '4.1');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'end', '4.512');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'start', '2.5');
insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'end', '5');

delete from Activity;


with r as (
	with machine_activities_start as (
		select machine_id
	         , process_id
	         , timestamp
		  from Activity
	     where activity_type = 'start'
	), machine_activities_end as (
		select machine_id
	         , process_id
	         , timestamp
		  from Activity
	     where activity_type = 'end'
	)
	select s.machine_id
	     , s.process_id
	     , MAX(e.timestamp - s.timestamp) as diff
	  from machine_activities_start s
	     , machine_activities_end e
	 where 1=1
	   and s.machine_id = e.machine_id
	   and s.process_id = e.process_id
	group by s.machine_id
	       , s.process_id
)
select r.machine_id
     , ROUND(AVG(r.diff)::numeric, 3) as processing_time
  from r
 where 1=1
group by r.machine_id
 



   
select a.machine_id
     , ROUND(AVG(b.timestamp-a.timestamp)::numeric, 3) as processing_time
  from Activity a join Activity b on a.machine_id = b.machine_id and a.process_id = b.process_id and a.activity_type = 'start' and b.activity_type = 'end'
 where 1=1
group by 1
 


------------------------------------------------------------------------
-- 577. Employee Bonus


Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int);

insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', Null, 4000);
insert into Employee (empId, name, supervisor, salary) values ('1', 'John', 3, 1000);
insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', 3, 2000);
insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', 3, 4000);


Create table If Not Exists Bonus (empId int, bonus int);
insert into Bonus (empId, bonus) values ('2', '500');
insert into Bonus (empId, bonus) values ('4', '2000');



-- Write your PostgreSQL query statement below
SELECT e.name
     , b.bonus
  FROM Employee e LEFT OUTER JOIN Bonus b ON e.empId = b.empId
 WHERE 1=1
   and (b.bonus < 1000 or b.bonus is NULL)
   
   
   
   
------------------------------------------------------------------------
-- 1280. Students and Examinations
  
Create table If Not Exists Students (student_id int, student_name varchar(20));
Create table If Not Exists Subjects (subject_name varchar(20));
Create table If Not Exists Examinations (student_id int, subject_name varchar(20));

insert into Students (student_id, student_name) values ('1', 'Alice');
insert into Students (student_id, student_name) values ('2', 'Bob');
insert into Students (student_id, student_name) values ('13', 'John');
insert into Students (student_id, student_name) values ('6', 'Alex');

insert into Subjects (subject_name) values ('Math');
insert into Subjects (subject_name) values ('Physics');
insert into Subjects (subject_name) values ('Programming');

insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Programming');
insert into Examinations (student_id, subject_name) values ('2', 'Programming');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Programming');
insert into Examinations (student_id, subject_name) values ('13', 'Physics');
insert into Examinations (student_id, subject_name) values ('2', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Math');

delete from Examinations 

select s.student_id
     , s.student_name
     , e.subject_name
     , count(e.subject_name) as attended_exams
  from Students s join Examinations e on s.student_id = e.student_id
group by 1, 2, 3 
order by 1,2;

select s.student_id
     , s.student_name
     , e.subject_name
--     , count(e.subject_name) as attended_exams
     , sub.subject_name
  from Students s
       join Examinations e on s.student_id = e.student_id
       left outer join Subjects sub on sub.subject_name = e.subject_name
--group by 1, 2, 3 
order by 1, 2


select * 
  from Subjects sub left join Examinations e on sub.subject_name = e.subject_name
       

with st as (  
	select s.student_id
	     , s.student_name
	     , sub.subject_name
	  from Students s
	     , Subjects sub
    order by 1
     )
select st.student_id
     , st.student_name
     , st.subject_name
     , count(e.student_id)
  from st left outer join Examinations e on st.student_id = e.student_id and st.subject_name = e.subject_name
 where 1=1
group by 1,2,3
order by 1, 3


------------------------------------------------------------------------
-- 570. Managers with at Least 5 Direct Reports


Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);

insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', Null);
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');

insert into Employee (id, name, department, managerId) values ('110', 'John', 'B', null);
insert into Employee (id, name, department, managerId) values ('111', '2', 'B', '110');
insert into Employee (id, name, department, managerId) values ('112', '3', 'B', '110');
insert into Employee (id, name, department, managerId) values ('113', '4', 'B', '110');
insert into Employee (id, name, department, managerId) values ('114', '5', 'B', '110');
insert into Employee (id, name, department, managerId) values ('115', '6', 'B', '110');

delete from Employee 

select * from Employee 

with emps as (
	  select e1.id
	    from Employee e1 join Employee e2 on e1.id = e2.managerId
	group by 1
	  having count(e1.id) > 4
)
select e.name
  from emps em join Employee e on em.id = e.id
  
  
  
  
  
  
  
  
  
  
  
  
  
  
------------------------------------------------------------------------
-- 1934. Confirmation Rate

Create table If Not Exists Signups (user_id int, time_stamp timestamp);
Create table If Not Exists Confirmations (user_id int, time_stamp timestamp, action varchar);

insert into Signups (user_id, time_stamp) values ('3', '2020-03-21 10:16:13');
insert into Signups (user_id, time_stamp) values ('7', '2020-01-04 13:57:59');
insert into Signups (user_id, time_stamp) values ('2', '2020-07-29 23:09:44');
insert into Signups (user_id, time_stamp) values ('6', '2020-12-09 10:39:37');

insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-01-06 03:30:46', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-07-14 14:00:00', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-12 11:57:29', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-13 12:58:28', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-14 13:59:27', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-01-22 00:00:00', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-02-28 23:59:59', 'timeout');

delete from Signups;
delete from Confirmations;



with a as (
	with timeout as (
		select c.user_id
		     , count(c.user_id) as num
		  from Confirmations c 
		 where c.action = 'timeout'
		group by 1
	), confirmed as (
		select c.user_id
		     , count(c.user_id) as num
		  from Confirmations c 
		 where c.action = 'confirmed'
		group by 1
	)
	select CASE WHEN c.user_id is not null THEN c.user_id
	            ELSE t.user_id
	       end as user_id
	     , CASE WHEN c.num is not null and t.num is not null THEN ROUND(c.num/(t.num + c.num)::numeric, 2)
	            WHEN c.num is not null and t.num is null THEN 1
	            ELSE 0
	       end as confirmation_rate
	     , t.num
	     , c.num
	     , t.num + c.num
	     , c.num/(t.num + c.num)
	  from timeout t full join confirmed c on t.user_id = c.user_id 
  ) 
select s.user_id
     , CASE WHEN a.confirmation_rate is not null then a.confirmation_rate
	        ELSE 0
	       end as confirmation_rate
  from Signups s left join a on s.user_id = a.user_id
  
  
  
select * from Signups s 















------------------------------------------------------------------------
-- 1251. Average Selling Price


Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);

insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
insert into Prices (product_id, start_date, end_date, price) values ('3', '2019-02-21', '2019-03-31', '30');

insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');

insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');


insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-26', '100');

select t.product_id
     , case when SUM(t.total_sum) is null then 0
           else ROUND(SUM(t.total_sum)/SUM(t.count_of_purchases)::numeric, 2)
       end as average_price
  from (
	  select p.product_id
	       , p.start_date
	       , p.end_date
	       , p.price
	       , SUM(us.units) as count_of_purchases
	       , SUM(us.units) * p.price as total_sum
	    from Prices p left join UnitsSold us on p.product_id = us.product_id and us.purchase_date between p.start_date and p.end_date
	group by 1,2,3, p.price
) as t
group by 1
order by 1


------------------------------------------------------------------------
-- 1075. Project Employees I

delete Project;
delete Employee;

Create table If Not Exists Project (project_id int, employee_id int);
Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);

insert into Project (project_id, employee_id) values ('1', '1');
insert into Project (project_id, employee_id) values ('1', '2');
insert into Project (project_id, employee_id) values ('1', '3');
insert into Project (project_id, employee_id) values ('2', '1');
insert into Project (project_id, employee_id) values ('2', '4');

insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3');
insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2');
insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1');
insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2');



select p.project_id  
     , ROUND(AVG(experience_years)::numeric, 2) as average_years
  from Employee e join Project p on e.employee_id = p.employee_id
group by 1



Create table If Not Exists Users (user_id int, user_name varchar(20));
Create table If Not Exists Register (contest_id int, user_id int);

insert into Users (user_id, user_name) values ('6', 'Alice');
insert into Users (user_id, user_name) values ('2', 'Bob');
insert into Users (user_id, user_name) values ('7', 'Alex');

insert into Register (contest_id, user_id) values ('215', '6');
insert into Register (contest_id, user_id) values ('209', '2');
insert into Register (contest_id, user_id) values ('208', '2');
insert into Register (contest_id, user_id) values ('210', '6');
insert into Register (contest_id, user_id) values ('208', '6');
insert into Register (contest_id, user_id) values ('209', '7');
insert into Register (contest_id, user_id) values ('209', '6');
insert into Register (contest_id, user_id) values ('215', '7');
insert into Register (contest_id, user_id) values ('208', '7');
insert into Register (contest_id, user_id) values ('210', '2');
insert into Register (contest_id, user_id) values ('207', '2');
insert into Register (contest_id, user_id) values ('210', '7');



with uc as (
	select COUNT(u.user_id) as num
	  from Users u 
)
select r.contest_id
     , round((COUNT(r.user_id) / uc.num::numeric)*100::numeric, 2) as percentage
  from Register r, uc
group by 1, uc.num
order by 2 desc, 1 asc




------------------------------------------------------------------------
-- 1211. Queries Quality and Percentage

Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int);

delete from Queries

insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', '1', '5');
insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', '2', '5');
insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', '200', '1');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', '5', '2');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', '3', '3');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', '7', '4');


| query_name | result           | position | rating |
| ---------- | ---------------- | -------- | ------ |
| null       | Golden Retriever | 1        | 5      |
| null       | German Shepherd  | 2        | 5      |
| null       | Mule             | 200      | 1      |

| Cat        | Shirazi          | 5        | 2      |
| Cat        | Siamese          | 3        | 3      |
| Cat        | Sphynx           | 7        | 4      |


insert into Queries (query_name, result, position, rating) values (null, 'Golden Retriever', '1', '5');
insert into Queries (query_name, result, position, rating) values (null, 'German Shepherd', '2', '5');
insert into Queries (query_name, result, position, rating) values (null, 'Mule', '200', '1');

select count(*)
  from Queries q
group by q.query_name



  
  
select q.query_name
     , round(sum(q.rating::numeric / q.position::numeric) / count(*), 2) as quality
     , round((sum(case when q.rating<3 then 1 else 0 end)::numeric / count(*))*100::numeric, 2)::numeric as poor_query_percentage
  from Queries q
 where 1=1
   and q.query_name is not null
group by 1






------------------------------------------------------------------------
-- 1193. Monthly Transactions I

Create table If Not Exists Transactions (id int, country varchar(4), state varchar, amount int, trans_date date);
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', '2019-01-07');

select to_char(t.trans_date, 'YYYY-MM') as month
     , t.country
     , count(*) as trans_count
     , sum(case when t.state = 'approved' then 1 else 0 end) as approved_count
     , sum(t.amount) as trans_total_amount
     , sum(case when t.state = 'approved' then t.amount else 0 end) as approved_total_amount
  from Transactions t
group by 1, 2




------------------------------------------------------------------------
-- 1174. Immediate Food Delivery II

Create table If Not Exists Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date);
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('1', '1', '2019-08-01', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('2', '2', '2019-08-02', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('3', '1', '2019-08-11', '2019-08-12');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('4', '3', '2019-08-24', '2019-08-24');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('5', '3', '2019-08-21', '2019-08-22');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('6', '2', '2019-08-11', '2019-08-13');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('7', '4', '2019-08-09', '2019-08-09');

with s as (
	select d.delivery_id
	     , d.customer_id
	     , d.order_date
	     , d.customer_pref_delivery_date
	     , case when d.order_date = d.customer_pref_delivery_date then 'immediate' else 'scheduled' end as order_type
	     , ROW_NUMBER() OVER(PARTITION BY d.customer_id ORDER BY order_date) as num
	  from Delivery d 
) 
select ROUND(sum(case when s.order_type = 'immediate' then 1 else 0 end)::numeric / count(*)::numeric * 100, 2) as immediate_percentage
  from s 
 where 1=1
   and s.num = 1
   
   
   
------------------------------------------------------------------------
-- 550. Game Play Analysis IV
   

drop table Activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);

insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

with s1 as (
	select count(distinct a.player_id)::numeric as players_num
	  from Activity a
	 where 1=1
), s2 as (
	select a1.player_id
	     , MIN(event_date) as event_date
	  from Activity a1
  GROUP BY player_id
)
select round((count(a1.*)/s1.players_num), 2) as fraction
--     , count(a1.*)
--     , s1.players_num
  from s2 a1 join Activity a2 on a1.player_id = a2.player_id 
       and a2.event_date != a1.event_date
       and a2.event_date = a1.event_date+1
       right join s1 on 1=1
group by s1.players_num
     


select * 
  from (
	select a1.*
	     , ROW_NUMBER() OVER(PARTITION BY a1.player_id ORDER BY event_date) as num
	  from Activity a1
) as t
 where t.num = 1
  
  
 
------------------------------------------------------------------------
-- 550. Game Play Analysis IV
   
drop table Employees;

Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int);

insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', null, '43');
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41');
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36');
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', null, '37');

with t as (
	select e.employee_id  as manager_id
	     , e.name as manager_name
	  from Employees e
	 where 1=1
)
select t.manager_id as employee_id
     , t.manager_name as name
     , count(e.employee_id) as reports_count
     , round(avg(e.age)) as average_age
  from Employees e join t on e.reports_to = t.manager_id
group by t.manager_name
       , t.manager_id
order by t.manager_id


------------------------------------------------------------------------
-- 1070. Product Sales Analysis III
drop table Sales;
drop table Product;
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar(10));

insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');

insert into Product (product_id, product_name) values ('100', 'Nokia');
insert into Product (product_id, product_name) values ('200', 'Apple');
insert into Product (product_id, product_name) values ('300', 'Samsung');



with t as (
	select s.product_id
	     , min(s.year) as year
	  from Sales s
	group by s.product_id
)
select s.product_id
     , s.year as first_year
     , s.quantity
     , s.price
  from t join Sales s on s.product_id = t.product_id and s.year = t.year




------------------------------------------------------------------------
-- 1045. Customers Who Bought All Products  

drop table Customer;
drop table Product;
  
Create table If Not Exists Customer (customer_id int, product_key int);
Create table Product (product_key int);

insert into Customer (customer_id, product_key) values ('1', '5');
insert into Customer (customer_id, product_key) values ('2', '6');
insert into Customer (customer_id, product_key) values ('3', '5');
insert into Customer (customer_id, product_key) values ('3', '6');
insert into Customer (customer_id, product_key) values ('1', '6');

insert into Product (product_key) values ('5');
insert into Product (product_key) values ('6');


with t as (
	select count(*) as num
	  from Product
)


select c.customer_id
  from Customer c
 where 1=1
group by c.customer_id
having count(distinct c.product_key) = (
	select count(*) as num
	  from Product
)


------------------------------------------------------------------------
-- 1789. Primary Department for Each Employee

drop table Employee;
Create table If Not Exists Employee (employee_id int, department_id int, primary_flag varchar);

insert into Employee (employee_id, department_id, primary_flag) values ('1', '1', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('2', '1', 'Y');
insert into Employee (employee_id, department_id, primary_flag) values ('2', '2', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('3', '3', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '2', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '3', 'Y');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '4', 'N');
  
  
with t2 as (
	select e.employee_id
	     , e.department_id
	  from Employee e
  group by e.employee_id
    having count(distinct e.department_id) = 1	 
)
select e.employee_id
     , e.department_id
  from Employee e join t2 on e.employee_id = t2.employee_id
  
union 
select e.employee_id
     , e.department_id
  from Employee e
 where e.primary_flag = 'Y'




     
 
------------------------------------------------------------------------
-- 610. Triangle Judgement
 
Create table If Not Exists Triangle (x int, y int, z int);

insert into Triangle (x, y, z) values ('13', '15', '30');
insert into Triangle (x, y, z) values ('10', '20', '15');



select t.*
     , case when t.x + t.y > t.z and t.z + t.y > t.x and t.z + t.x > t.y then 'Yes'
       else 'No'
       end as triangle
  from Triangle t

  
  
  
------------------------------------------------------------------------
-- 180. Consecutive Numbers
drop table Logs;
Create table If Not Exists Logs (id int, num int);

insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');

--insert into Logs (id, num) values ('1', '1');
--insert into Logs (id, num) values ('2', '1');
--insert into Logs (id, num) values ('3', '2');
--insert into Logs (id, num) values ('4', '2');
--insert into Logs (id, num) values ('5', '1');
--insert into Logs (id, num) values ('6', '2');
--insert into Logs (id, num) values ('7', '2');

select distinct l.num as "ConsecutiveNums"
  from Logs l join Logs l1 on l.id = l1.id+1 and l.num = l1.num join Logs l2 on l1.id = l2.id+1 and l1.num = l2.num
order by l.id
  

with t as (
	select count(l.id) as ConsecutiveNums
	  from Logs l join Logs l1 on l.id = l1.id+1 and l.num = l1.num join Logs l2 on l1.id = l2.id+1 and l1.num = l2.num
)
select t.ConsecutiveNums as "ConsecutiveNums" from t where ConsecutiveNums > 0



select distinct t.num as "ConsecutiveNums"
  from (
	select l.id
	     , l.num
	     , lag(l.num, 1) over (order by l.id) as before
	     , lead(l.num, 1) over (order by l.id) as middle
	     , lead(l.num, 2) over (order by l.id) as after
	  from Logs l
) as t
where t.num = t.middle and t.num = t.after





------------------------------------------------------------------------
-- 1164. Product Price at a Given Date

drop table Products;

Create table If Not Exists Products (product_id int, new_price int, change_date date);

insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');


with t1 as (
	select distinct p.product_id
	     , 10 as price
	     , to_date('2019-08-16', 'YYYY-MM-DD') as change_date
	  from Products p
), t2 as (
	select coalesce(p.product_id, t1.product_id) as product_id
	     , coalesce(p.new_price, t1.price) as new_price
	     , coalesce(p.change_date, t1.change_date) as change_date
	  from t1 left outer join Products p on t1.product_id = p.product_id and p.change_date <= to_date('2019-08-16', 'YYYY-MM-DD')
), t3 as (
	select t2.product_id
	     , t2.new_price
	     , ROW_NUMBER() OVER(PARTITION BY t2.product_id ORDER BY t2.change_date desc) as num
	  from t2
)
select t3.product_id
     , t3.new_price as "price"
  from t3
 where t3.num = 1
 

 
------------------------------------------------------------------------
--  1204. Last Person to Fit in the Bus
 
Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int);

insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1');
insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5');
insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2');
insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3');
insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6');
insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4');

with t1 as (
	select q.*
	     , sum(q.weight) over(order by q.turn) as cummulative_sum
	     , row_number() over(order by q.turn) as row_num
	  from Queue q
)
select t1.person_name
  from t1 
 where t1.cummulative_sum <= 1000
order by t1.turn desc
limit 1
 

------------------------------------------------------------------------
-- 1907. Count Salary Categories

Create table If Not Exists Accounts (account_id int, income int);

insert into Accounts (account_id, income) values ('3', '108939');
insert into Accounts (account_id, income) values ('2', '12747');
insert into Accounts (account_id, income) values ('8', '87709');
insert into Accounts (account_id, income) values ('6', '91796');

select category
     , accounts_count
  from (
	select 1
	     , 'Low Salary' as category
	     , count(*) as accounts_count
	  from Accounts a
	 where a.income < 20000
	union
	select 2
	     , 'Average Salary'
	     , count(*)
	  from Accounts a
	 where a.income between 20000 and 50000
	union
	select 3
	     , 'High Salary'
	     , count(*)
	  from Accounts a
	 where a.income > 50000
	order by 1
)


------------------------------------------------------------------------
-- 1978. Employees Whose Manager Left the Company

drop table Employees;
Create table If Not Exists Employees (employee_id int, name varchar(20), manager_id int, salary int);

insert into Employees (employee_id, name, manager_id, salary) values ('3', 'Mila', '9', '60301');
insert into Employees (employee_id, name, manager_id, salary) values ('12', 'Antonella', null, '31000');
insert into Employees (employee_id, name, manager_id, salary) values ('13', 'Emery', null, '67084');
insert into Employees (employee_id, name, manager_id, salary) values ('1', 'Kalel', '11', '21241');
insert into Employees (employee_id, name, manager_id, salary) values ('9', 'Mikaela', null, '50937');
insert into Employees (employee_id, name, manager_id, salary) values ('11', 'Joziah', '6', '28485');



------------------------------------------------------------------------
-- 626. Exchange Seats

Create table If Not Exists Seat (id int, student varchar(255));

insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');


--lag(s.student, 1) over (order by s.id) as before

select lead(s.student, 1) over (order by s.id) as after
  from Seat s
 where 1=1
 
select s.id
	 , s.student
     , case when mod(s.id, 2) = 1 then 1 else 0 end as num
     , lead(s.student, 1) over (order by s.id) as after
  from Seat s
 where 1=1
order by s.id


select s.id
	 , s.student
	 , s1.id
	 , s1.student
	 , s2.id
	 , s2.student
  from Seat s left join Seat s1 on s.id+1 = s1.id left join Seat s2 on s.id-1 = s2.id
 where 1=1
order by s.id






------------------------------------------------------------------------
-- 1341. Movie Rating

Create table If Not Exists Movies (movie_id int, title varchar(30));
Create table If Not Exists Users (user_id int, name varchar(30));
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);

insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');

insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'James');

insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');

delete from Movies;
delete from Users;
delete from MovieRating;

insert into Movies (movie_id, title) values ('1', 'Rebecca');
insert into Users (user_id, name) values ('1', 'Rebecca');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '5', '2020-02-12');


select name as results
  from (
	select mr.user_id
	     , u.name
	     , count(*)
	  from MovieRating mr join Users u on mr.user_id = u.user_id 
	 where 1=1
	 group by 1,2
	 order by 3 desc, u.name asc
	 limit 1
 )
union all
select name
  from (
 	select mr.movie_id
 	     , m.title as name
 	     , round(avg(mr.rating), 1)::numeric
	  from MovieRating mr join Movies m on mr.movie_id = m.movie_id
     where to_char(mr.created_at, 'YYYY-MM') = '2020-02'
	 group by mr.movie_id
	        , m.title
	 order by 3 desc, m.title asc
	 limit 1
 )
 
 
 
 
 
------------------------------------------------------------------------
-- 1321. Restaurant Growth
 
drop table Customer;
Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int);

insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100');
insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120');
insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140');
insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150');
insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80');
insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150');


with a as (
	select min(c.visited_on)+6 as start_date
	  from Customer c
), t as (
	select distinct c.visited_on
	  from Customer c
	     , a
	 where c.visited_on >= a.start_date
)
select t.visited_on
     , round(sum(c.amount), 2) as amount
     , round(sum(c.amount)/7::numeric, 2) as average_amount
  from t
     , Customer c
 where 1=1
   and c.visited_on between t.visited_on-6 and t.visited_on
  group by t.visited_on
  order by t.visited_on
  

  
  
------------------------------------------------------------------------
-- 602. Friend Requests II: Who Has the Most Friends
  
Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null);

insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09');



select id
     , sum(num) as num
  from (
	select ra1.requester_id as id 
	     , count(ra1.accepter_id) as num
	  from RequestAccepted ra1  
	group by ra1.requester_id
	union all
	select ra1.accepter_id
	     , count(ra1.requester_id)
	  from RequestAccepted ra1  
	group by ra1.accepter_id
)
group by 1
order by 2 desc
limit 1


------------------------------------------------------------------------
-- 585. Investments in 2016

Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float);

insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40');


select sum(i1.tiv_2016)
  from Insurance i1 join Insurance i2 on i1.tiv_2015 = i1.tiv_2016 and i1.lat <> i2.lat and i1.lon <> i2.lon 
 where 1=1
   and i1.tiv_2015 
   
   
   
   
------------------------------------------------------------------------
-- 1667. Fix Names in a Table
   
drop table Users;
Create table If Not Exists Users (user_id int, name varchar(40));

insert into Users (user_id, name) values ('1', 'aLice');
insert into Users (user_id, name) values ('2', 'bOB');


select u.user_id
     , upper(substring(u.name from 1 for 1)) || lower(substring(u.name from 2 for length(u.name))) as name
  from Users u
order by user_id
  
  
