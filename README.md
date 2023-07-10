# multiple_user_auth
#### Fork Me if you happy with this ..... 😜

Intergrated roles - customer and staff. \
In JWT there are embeded values such as user_id , username and usertype\
with npm libraries like jwt-decode we can decode and use those values in react

if you need to change database change values in settings.py\
NAME , USER , PASSWORD - if you are using mysql
change whole default code part if you using other db refering necessery documentation.


```python
DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'test_db',  
        'USER': 'root',  
        'PASSWORD': 'root',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}
```
## sample POST JSON body for example
### 1.For customer

```JSON
{
        "username": "customer",
        "email": "customer@customer.com",
        "password": "customer" ,
        "fullname" : "customer shalinda",
        "address" : "polonnaruwa"
}
```

### 2.For staff

```JSON
{
        "username": "staff",
        "email": "staff@staff.com",
        "password": "staff" ,
        "branch" : "branch1",
        "tele" : "polonnaruwa",
        "usertype" : "staff"
}
```
