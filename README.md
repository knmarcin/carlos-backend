# carlos-backend

###Purpose

The main purposes of this project are, allowing user to:
- create a 'CAR'
- add 'Repair log' to a 'CAR', with data like: 
    - time stamp
    - information about a service
    - which employee did a service
- retrieve data, with features like:
    - filters:
        - filter by car, employee, date and any other useful queries
    
###Models

So at this moment we have 3 models, which are:
- Employee
- Car
- History

### Endpoints

```/history``` ```GET``` ```POST``` 
- returns a list with all entries, this view will allow user to filter data

```/history/{id}``` ```GET``` ```PUT``` ```DELTE``` 
- self-explanatory

```/closest-services``` ```GET``` 
- list of closest services for cars

### Security

App is using default django/django-rest-framework auth

