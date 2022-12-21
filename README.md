# Photos-Hub

This project is a microservice that will let you view / edit / add Champions for League Of Legends !

The project consists of 3 parts, front-end, back-end, and MySQL database.

The Architecture of this project is described below :

![_Flow](https://user-images.githubusercontent.com/71922912/208976356-8707bff7-91e2-4414-89f6-8763ff420065.png)

## How to run the application ?

Prerequisites :
- Docker
- Git

1. First clone the repository to your local system :

``` git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/Photos-Hub.git```

2. Move into the directory of the project with the command : 

``` cd Photos-Hub ```

3. Then to start the application simply write the command : 

``` docker-compose up ```

this will create 3 containers for frontend, backend and database.

3. To enter the Backend FastAPI UI - open your browser and enter the URL : 
   ``` localhost:90/docs ```

4. To enter the Frontend UI - open your browser and enter the URL : 
   ``` localhost:8501 ```
