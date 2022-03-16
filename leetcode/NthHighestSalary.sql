#https://leetcode.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select sub.salary from (select salary, dense_rank() over(order by salary desc) 'rank'
                          from Employee where salary is not null) sub where sub.rank = N
                           limit 1
      
  );
END
