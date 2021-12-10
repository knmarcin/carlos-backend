# carlos-backend

### Purpose

The main purposes of this project are, allowing user to:
- create a 'CAR'
- add 'Repair log' to a 'CAR', with data like: 
    - time stamp
    - information about a service
    - which 'Employee' did a service
- retrieve data, with an option to filter, search, order_by:
- get useful collection of information for front-end plots     

### Endpoints

```/history``` ```GET``` ```POST``` Params: ```search, filter, order_by```


```/history/{id}``` ```GET``` ```PUT``` ```DELTE``` 

```/closest-services``` ```GET``` 

```/workers``` ```GET```

```/cars``` ```GET``` ```POST``` Params: ```search, filter, order_by```  

```/dashboard``` ```GET```

### Security

App is using rest_framework_simplejwt.authentication.JWTAuthentication
