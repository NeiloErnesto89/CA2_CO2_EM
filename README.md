<h1 align="center"">CSD - CA2 - Group 4

<h2 align="center">CO2 emissions for Aviation Industry </h2>


### **Here is the link to the groups Github repo:** **[CSD CA2 CO2 Emissions Project](https://github.com/NeiloErnesto89/CA2_CO2_EM)** 


# **Table of Content**

- [**Team Principles**](#team-principles)
- [**Project Introduction**](#project-introduction)
- [**Project Scope**](#project-scope) 
- [**UX**](#ux)


## **Team Principles**

A list of core principles guiding the project and the teams workload:

> 1.	Respect for one another: Basically respect each others time, private lives, deadlines etc. If we cannot attend meetings etc., just try and communicate that. 
> 2.	Communicate: Everyone is here to learn, ask questions, please avoid judgement and try help one another
> 3.    Etc. etc.


## **Project Introduction** 

"Our team has beem hired by a climate change NGO to develop an application to track, analyse and provide insights regarding CO2 emissions by the aviation industry"


## **Project Scope**

Built in Python using the Flask/Django framework etc.


> 1.	Django:  Django project backend by a relational database to create a website that allows users to track, calculate and analyse data records CO2 emissions by the aviation industry.
> 2.	Backend: Python
> 3.    Frontend: HTML

## **UX** 

Here's how are App looks ..


## Deployment
1. In your virtual environment, install all requirements:
    ~~~bash
    pip install -r requirements.txt
    ~~~
2. Migrate the database
    ~~~bash
    python manage.py migrate
    ~~~
3. Create a Super User
    ~~~bash
    python manage.py createsuperuser
    ~~~


### Debug Run
```bash
python manage.py runserver
```

### Settings

- Admin Portal Credentials
    ```
    user: admin
    pass: CA2123!
    ```

#### Django-Pytest

~~~bash
    pip install django-pytest
~~~

Added ```pytest.ini``` config file with following details to facilitate a smooth testing suite

```
# -- FILE: pytest.ini (or tox.ini)
[pytest]
DJANGO_SETTINGS_MODULE = App.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```

test files in core dir, we run the ```pytest``` command in the terminal (or ```pytest -x``` for stop on failure)

~~~

(.venv) PS C:\Users\XXXX\Desktop\Personal\Donegal_ATU\Contemporary_SW\XXXX\> pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
django: settings: App.settings (from ini)
rootdir: C:\Users\XXXX\Desktop\Personal\Donegal_ATU\Contemporary_SW\XXXX\, configfile: pytest.ini
plugins: django-4.5.2
collected 2 items

core\tests.py .F                                                                                                                                             [100%]

============================================================================ FAILURES ============================================================================= 
________________________________________________________________________ test_example_fail ________________________________________________________________________ 

    def test_example_fail():
>       assert 2 == 1
E       assert 2 == 1

core\tests.py:10: AssertionError
===================================================================== short test summary info ===================================================================== 
FAILED core/tests.py::test_example_fail - assert 2 == 1
=================================================================== 1 failed, 1 passed in 0.89s =================================================================== 

~~~