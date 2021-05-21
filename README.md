<p align="center"><img alt= "logo" src="images/logo.png" width="200"></p>
<h1 align="center">Order Pizza API</h1>
<h3 align="center">A RESTful API as pizza restaurant ordering system.</h3>

<h3 align="center">
<a href="https://order-pizza-api-python3-7.herokuapp.com/api/ui">Documentation </a>
</br>
</br>

## Setup

1. `git clone https://github.com/NavGitGood/order-pizza-api.git`
2. `cd order-pizza-api`
3. `pip install -r requirements.txt` 
   _or place virtual environment and then install_
4. `python server.py`

## Usage

**Example Response**

```bash
curl -s https://order-pizza-api-python3-7.herokuapp.com/api/orders
```

```json
[
  {
    "Crust": "NORMAL",
    "Flavor": "VEGGI",
    "Order_ID": 1,
    "Size": "M",
    "Table_No": 1,
    "Timestamp": "2018-12-12T13:42:13.704148+00:00"
  },
  {
    "Crust": "THIN",
    "Flavor": "CHEESE",
    "Order_ID": 2,
    "Size": "S",
    "Table_No": 5,
    "Timestamp": "2018-12-12T13:42:13.704148+00:00"
  },
  {
    "Crust": "NORMAL",
    "Flavor": "CHICKEN-FAJITA",
    "Order_ID": 3,
    "Size": "L",
    "Table_No": 3,
    "Timestamp": "2018-12-12T13:42:13.720690+00:00"
  }
]
```

**Endpoints**


* POST : `/auth`    

```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username": "test", "password": "test"}'  https://order-pizza-api-python3-7i.herokuapp.com/api/auth
```

* POST : `/orders`  (_Access Token is required_)

```bash
curl 
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer <JWT>" 
  -X POST 
  -d  
 '{
    "Flavor": "ABC", 
    "Crust": "XYZ",
    "Size": "XL", 
    "Table_No": 9
  }' 
  https://order-pizza-api-python3-7.herokuapp.com/api/orders
  ```
`Do replace the <JWT> in the above request with the token you have acquired.`


* DELETE : `/orders/{Order_ID}`

```bash
curl -X DELETE https://order-pizza-api-python3-7.herokuapp.com/api/orders/1
```

## License
MIT

Make sure to add following files:

Procfile
runtime.txt - to mention the python version to be used (must be supported by heroku, check from list https://devcenter.heroku.com/articles/python-support#supported-runtimes
requirements.txt - package versions could sometime cause an issue (if not present in heroku, use a different version in that case)
After you code is pushed to github main, use following steps:

go to https://dashboard.heroku.com/apps and create a new app e.g. basicflaskapi
login to heroku cli in powershell / terminal using heroku login (for browser login) or heroku login -i (for login from powershell / terminal)
add you repo to heroku heroku git:remote -a {project_name} e.g. heroku git:remote -a basicflaskapi
push your code to heroku git push heroku main
if everything runs fine, a url would be generated for your app