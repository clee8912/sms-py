# School Management System

## Requirements:
This is basic School Management System where students can register courses and view courses assigned to them
1. Only students with correct credentials can login, else it will display "Wrong Credentials"
2. Students with valid credentials will be able to see the courses they registered, saved to a csv.
3. Students will be able to register any course listed in the csv file for courses.

## Databases:
### CSV Files will be used to store the following information:
### 1. students.csv: 

| Name          | Description                    |
| ------------- |:------------------------------:|
| email         | Student's current school email |
| name          | The full name of the student   |
| pass          | Student's password             |

### 2. courses.csv: 

| Name          | Description                    |
| ------------- |:------------------------------:|
| course_id     | Unique Course identifier       |
| name          | The name of the Course         |
| instructor    | The name of the instructor     |

### 3. attending.csv: 

| Name          | Description                    |
| ------------- |:------------------------------:|
| course_id     | Unique Course identifier       |
| email         | Student's current school email |




