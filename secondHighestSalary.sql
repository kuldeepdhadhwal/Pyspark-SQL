Select max(salary) from employee where salary <> (Select max(salary) from employee);
