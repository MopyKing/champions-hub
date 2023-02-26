# Champions-Hub


https://user-images.githubusercontent.com/71922912/214917768-a180aee3-b84f-4a6a-9bb2-0ab7834a2110.mp4


This project is a microservice that will let you view & edit Champions and Weapons of "League Of Legends" !

The project consists of 3 parts, front-end, back-end, and MySQL database.

The Architecture of this project is described below :

![_Flow](https://user-images.githubusercontent.com/71922912/208976356-8707bff7-91e2-4414-89f6-8763ff420065.png)

## How to run the application ?

Prerequisites :
- Docker
- Git
- ```.env.mysql``` file

1. First clone the repository to your local system :

``` git clone https://github.com/MopyKing/champions-hub.git```

2. Move into the directory of the project with the command : 

``` cd champions-hub ```

3. Create a file named ```.env.mysql``` and paste this content : 

```
MYSQL_DATABASE=eass
MYSQL_ROOT_HOST=%
MYSQL_ROOT_PASSWORD=123456
```

4. Then to start the application simply write the command : 

``` docker-compose up ```

this will create 3 containers for frontend, backend and database.

- To enter the Backend FastAPI UI - open your browser and enter the URL : 
   ``` localhost:90/docs ```

- To enter the Frontend UI - open your browser and enter the URL : 
   ``` localhost:8501 ```
