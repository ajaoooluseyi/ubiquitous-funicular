# ubiquitous-funicular

## Description
It is a issue management API built on a PostgreSQL database. It accepts issue data and asssigns an agent and a mechanic 
to the issue based on availability. 

### Dependencies

* Django
* Django Rest Framework
* Python version 3.11 


### Executing program

On the terminal execute the below command to create the projects' working directory and move into that directory.

 
```python
$ mkdir app
cd app
```

In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

 
```python
$ py -m venv venv
```

To activate the virtual environment, execute the below command.

```python
$ source venv/Scripts/activate
```
Clone this repository in the projects' working directory by executing the command below.

```python
$ git clone https://github.com/ajaoooluseyi/ubiquitous-funicula.git
$ cd ubiquitous-funicula

```

To install all the required dependencies execute the below command.

```python
$ pip install -r requirements.txt
```

To run the app, navigate to the app folder in your virtual environment and execute the command below
```python
$ python manage.py migrate

$ python manage.py runserver
```

