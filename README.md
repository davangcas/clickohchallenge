# Ecommerce challenge for ClickOH

## Runtime version of python

python 3.8

## Deploy localy this project:

Need postgresql installed and config in settings database credentials

- Create python enviroment

```python3 -m venv venv```

- Export enviroment vars to run the project

```

    #!/bin/bash

    source venv/bin/activate

    export DEBUG=True


```

- Install requiremets

```pip install -r requirements.txt```


- Run the project

```python manage.py runserver```


### Notes

To create a new order you need access to order-details/ url
