# RAKT-Innovations-P1-django-take-home-assignment

Run these commands in project root:
```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd api
python manage.py migrate
python manage.py populate
python manage.py runserver
```
After that, please [open this in the browser](http://127.0.0.1:8000/foodtrucks) and check for the partial listing of food trucks imported (`count` is 481). Add `?x=6007018` to the end of the URL and see the list has been reduced (now `count` is 5). That happened because the view *FoodTruckViewSet* (source code is located at *api/main/views.py*) filtered according to the column *x*, which values would be inside a interval centered at `6007018`. The main approach consisted of writing my own `get_queryset` method for the view.

### Remarks

- *food-truck-data.csv* is exactly the same CSV file provided by the challenge's author.
- Django Rest Framework (a.k.a. DRF) for the whole API Rest architecture
- Custom command *populate*: read data from CSV file and run *create* method from Django model *FoodTruck*. Source code is located at *api/main/management/commands/**populate.py***
- Since returning at least 5 food trucks was a requirement, I chose to insert the filtering query to a loop, where after every step the interval of search would increase "a little".

### Documentation

GET /foodtrucks - list of trucks

POST /foodtrucks - create truck

GET /foodtrucks/:id - retrieve details of a particular truck

PUT /foodtrucks/:id - update details of a particular truck

DELETE /foodtrucks/:id - remove truck