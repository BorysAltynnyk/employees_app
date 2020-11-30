
The web application should allow:

- display a list of departments and the average salary (calculated automatically) for these departments
- display a list of employees in the departments with an indication of the salary for each employee and a search field to search for employees born on a certain date or in the period between dates
- change (add / edit / delete) the above data


Employee
- id - Primary Key
- name 
- salary
- birth_date
- depratment_id - FK 


Department
- id -PR
- name

One Department has many Employee


API: 
GET /departments/42
GET    /deparments
POST /departments
PATCH /departments/42
DELETE /departments/42

GET
POST
PUT
PATCH

search field to search for employees born on a certain date or in the period between dates

GET /employees?birth_date=22.01.21
GET /employees?start=11.11.11&end=12.12.12


```
docker run -d --name mysql -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=db-password \
  -v /tmp:/var/lib/mysql mysql
```






