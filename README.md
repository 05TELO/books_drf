# books_drf

---

### Installation instructions

---
Dependencies:
* Python v.3.10.6
* Poetry


after cloning this repository

  
    >  poetry install
     
  
    > poetry run python manage.py migrate
     
  
    > poetry run python manage.py runserver
  
---

## Tests


[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/25434486-e7aa663d-75da-4d44-a940-2ccdf55d4079?action=collection%2Ffork&collection-url=entityId%3D25434486-e7aa663d-75da-4d44-a940-2ccdf55d4079%26entityType%3Dcollection%26workspaceId%3D25bf1c5c-460a-46d5-8573-be88f8617905)


### POST



* Add new author

  > http://localhost:8000/api/authors/
  >
  >>{"first_name": "<first_name>","last_name": "<last_name>", "email": "<email>"}

* Add new book

  > http://localhost:8000/api/books/
  > 
  >> {
  >>  "title": "<title>",
  >>  "authors": [id author, ...]
  >>   }


### GET


* Author list

  > http://localhost:8000/api/authors/


* Author

  > http://localhost:8000/api/authors/[slug]

* Book list

  > http://localhost:8000/api/books/

* Book

  > http://localhost:8000/api/books/[slug]

___

### Languages:

* Python

### Frameworks:

* Django REST

### Database:

* SQLite3



