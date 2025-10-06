# Write your MySQL query statement below
select Product.product_name,Sales.year,Sales. price 
from Product -- table 2:
right join Sales -- table 1:
on Sales.product_id=Product.product_id ;

