#https://leetcode.com/problems/customers-who-never-order/
Select c1.name as Customers from Customers c1 left join Orders o1 on c1.id = o1.customerId where o1.customerId is null
