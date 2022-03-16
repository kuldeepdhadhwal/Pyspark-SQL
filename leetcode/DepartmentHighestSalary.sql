#https://leetcode.com/problems/department-highest-salary/
Select Department, Employee, Salary from (Select d1.name as Department, e1.name as Employee, e1.salary as Salary, dense_rank() over(partition by d1.name order by e1.salary desc) 'dense_rank'  from Employee e1 inner join Department d1 on e1.departmentId = d1.id) e where e.dense_rank=1;
