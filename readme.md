# Simple REST API for Managing Persons

This repository contains a simple REST API for managing person records. You can create, read, update, and delete person records. 

Live link - https://hngx-ii.onrender.com/api

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) for creating isolated Python environments.
- [Django](https://www.djangoproject.com/) installed.
- [Django REST framework](https://www.django-rest-framework.org/) installed.

### Installation

Clone the repository:

    git clone https://github.com/iConnell/hngX-ii.git


Create a virtual environment:

    virtualenv venv
    source venv/bin/activate
    
Install the project dependencies:

    pip install -r requirements.txt

## Starting development server

To run the API locally, follow these steps:

Migrate the database:

    python manage.py migrate

Start the development server:

    python manage.py runserver

Test the API:

    python manage.py test

###### E-R Diagram 
![alt image showing the E-R diagram](https://github.com/iConnell/hngX-ii/blob/master/E-R_diagram.png?raw=true)



# Using the APIs
The API provides the following endpoints

| Method  |  Endpoint  |  Description      |
|---------|------------|-------------------|
|POST     |/api        |Create a new person|
|GET      |/api        |List all persons   |
|GET      |/api/user_id|Retrieve a person  |
|PATCH    |/api/user_id|Update a person    |
|DELETE   |/api/user_id|Delete a person    |

- #### Create a Person:
    - POST `/api`
    - status code 201
    ### Parameters
    |Parameter| Required|
    |---------|---------|
    |```name```|required|
    |```organisation```|Optional - Defaults to ```HNGX```|
    |```role```|Optional - Defaults to ```intern```|

    Example request:

        {
            "name": "John Doe",
            "organisation": "Zuri"
            "role": "intern"
        }

    Example response:

        {
            "id": 1,
            "name": "John Doe"
            "organisation": "Zuri",
            "role": "intern"
        }
    
- ### List Persons
    - GET ```/api```
    - status code 200

    Example response:

        [
            {
                "id": 1,
                "name": "John Doe"
                "organisation": "Zuri",
                "role": "intern"
            },
            {
                "id": 2,
                "name": "Mark Essien"
                "organisation": "HNGX",
                "role": "chief_mentor"
            }
        ]

- ### Retrieve Person
    - GET ```/api/user_id```
    - status code 200

    Example response:

        {
            "id": 1,
            "name": "John Doe"
            "organisation": "Zuri",
            "role": "intern"
        },
        
- ### Update Person
    - PATCH ```/api/user_id```
    - status code 200

    ### Parameters
    |Parameter| Required|
    |---------|---------|
    |```name```|Optional|
    |```organisation```|Optional|
    |```role```|Optional|

    Example request:

        {
            "name": "Updated Name",
            "organisation": "Andela"
            "role": "intern"
        }

    Example response:

        {
            "id": 1,
            "name": "Updated Name"
            "organisation": "Andela",
            "role": "intern"
        },

- ### Update Person
    - DELETE ```/api/user_id```
    - status code 204