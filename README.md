# **Task Monkey**

**Developer: Mark Daniel**

💻 [Live link](https://md82-p5-api-93955a9ca799.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the Task Monkey front-end application

## Table of Contents

- [**Task Monkey**](#task-monkey)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
    - [Code Structure](#code-structure)
      - [Project Apps](#project-apps)
      - [Other django apps](#other-django-apps)
  - [User Stories](#user-stories)
  - [Technologies Used](#technologies-used)
    - [Languages \& Frameworks](#languages--frameworks)
    - [Libraries \& Tools](#libraries--tools)
    - [All libraries used for deployment in Heroku](#all-libraries-used-for-deployment-in-heroku)
  - [Agile design](#agile-design)
    - [About](#about)
    - [User Story Template](#user-story-template)
    - [Kanban Board](#kanban-board)
  - [Database Design](#database-design)
    - [Data Models](#data-models)
      - [User Model](#user-model)
      - [Profile model](#profile-model)
      - [Tasks model](#tasks-model)
      - [Comment model](#comment-model)
  - [Features](#features)
    - [Home Page](#home-page)
    - [Profile List Page](#profile-list-page)
    - [Profile Detail Page](#profile-detail-page)
    - [Task List Page](#task-list-page)
    - [Task Detail Page](#task-detail-page)
    - [Comment List Page](#comment-list-page)
    - [Comment Detail Page](#comment-detail-page)
  - [Validation](#validation)
    - [Python](#python)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Creating Database using ElephantSQL](#creating-database-using-elephantsql)
    - [Deploying the website in Heroko](#deploying-the-website-in-heroko)
      - [Login or create an account at Heroku](#login-or-create-an-account-at-heroku)
      - [Creating an app](#creating-an-app)
      - [Open settings Tab](#open-settings-tab)
        - [Click on config var](#click-on-config-var)
        - [Add Buildpacks](#add-buildpacks)
      - [Open Deploy Tab](#open-deploy-tab)
        - [Choose deployment method](#choose-deployment-method)
        - [Connect to Github](#connect-to-github)
        - [Automatic and Manual deploy](#automatic-and-manual-deploy)
        - [Deployment](#deployment-1)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning the repository in GitHub](#cloning-the-repository-in-github)
  - [Credits](#credits)
    - [Code](#code)
  - [Thank Yous](#thank-yous)

## Project Structure

The overall structure of the project was made with the help of Code Institute walkthrough project [drf-api](https://github.com/Code-Institute-Solutions/drf-api) including models, views and serializers.

### Code Structure

Project code structure is organized and divided into various application folders and constructed using Django Rest Framework

#### Project Apps

- **profile app**: This app contains model, views, serializers, tests and urls for profile
- **tasks app**: This app contains model, views, serializers, tests and urls for tasks
- **comments app**: This app contains model, views, serializers, tests and urls for comments

#### Other django apps

- **settings.py**: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- **Procfile**: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- **requirements.txt**: This file lists the dependencies required for the Django project to run.
- **env.py**: This file is used to store environment variables for a Django project or application, such as database connection details or API keys.

## User Stories

User Story: Add privacy option to tasks when adding them - as a site user i can choose whether my tasks are private or publicly visible

User Story: Archive old tasks - as a site user i can archive old or completed tasks to keep my view clean on the site

User Story: task category - as a site user i can assign a category to my tasks

User Story: task status - as a site user i can set a completed status for my tasks

User Story: set priority and deadline for tasks - as a site user i can set a priority and deadline for my tasks

User Story: add a task - as a site user i can create a task

User Story: edit profile - as a site user i can edit my personal profile

User Story: Create profile - As a site user i can register for the site/create a profile

## Technologies Used

### Languages & Frameworks

- Python 3.10.2
- Django
- Django Rest Framework

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) to store images for profile and tasks
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files.
- [Lucidcharts](https://lucid.app/) has been used in project to design and document data model architecture.
- [CodeAnyWhere](https://app.codeanywhere.com/) was IDE used for writing code and to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku](https://heroku.com) - Cloud platform. Justification: I used this was used to deploy the project into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) - API toolkit. Justification: I used this to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) - API Module. Justification: I used this for user authentication
- [Psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adaptor. Justification: This was used as a PostgreSQL database adapter for Python
- [ElephantSQL](https://www.elephantsql.com/) - Database hosting service – Justification: This was used as the deployed project on Heroku uses an ElephantSQL database

### All libraries used for deployment in Heroku

- All libraries used are stored in requirements.txt for deployment in heroku

## Agile design

### About

- Agile development is the most effective way to development of any website
- The project is broken down into individual elements that are then tackled one at a time

### User Story Template

- Using Github issues first I created the template for a user story that was later used to create user stories. I used labels to differentiate between the types of user stories and bugs. The labels used are: User story, could have, should have, must have and bug

### Kanban Board

- As a visual representation of the project's status, showing what tasks are to be done, in progress and completed.Each task is represented as a card on the board, and the cards can be moved from one column to another to show progress.

[Link to project Kanban board.](https://github.com/users/markdaniel1982/projects/5)

## Database Design

- This sample ERD diagram was made using [Lucid Charts](https://www.lucidchart.com)
- For this Django app I have used PostgreSQL relational database management system.
- model showed on the diagram visually represents the structure of a PostgreSQL database, including tables, columns, relationships, and constraints, that is stored in the database itself.

![API Chart ]()

### Data Models

#### User Model

- User model as part of the Django Rest Framework dj-rest-auth library contains basic information about authenticated user and contains folowing fields:
  Username, Password, Email

#### Profile model

- Profile model is created for user to add their details and image for better interaction with the website

| NAME| DATABASE KEY | FIELD TYPE | VALIDATION |
|:---:|:---:|:---:|:---:|
| name        | owner | OneToOneField | User, on_delete=models.CASCADE|
| profile_image    | profile_image    | ImageField    | upload_to='images/', default='../profileplaceholder_niir6l'' |
| bio | bio | TextField     | max_length=255 blank=True|
| created_on | created_on | DateTimeField | auto_now_add=True|

#### Tasks model

- Tasks model is created for the user to add a new task

owner = models.ForeignKey()
    created_on = models.()
    updated_on = models.()
    title = models.()
    content = models.()
    priority = models.()
    due_date = models.DateField()
    privacy = models.IntegerField()
    status = models.IntegerField(

| DATABASE KEY | FIELD TYPE | VALIDATION |
|:---:|:---:|:---:|
| owner | ForeignKey | User, on_delete=models.CASCADE
| created_on | DateTimeField |  auto_now_add=True
| updated_on | DateTimeField |  auto_now=True
| title | CharField |  max_length=255
| content | TextField |  blank=True
| priority | IntegerField |  choices=priority_choices, default=2
| due_date | DateField |  null=True, blank=True
| privacy | IntegerField | choices=privacy_choices, default=1
| status | IntegerField | choices=status_choices, default=1

The choices available for the above model are:

priority_choices = [
        (1, 'URGENT'),
        (2, 'Normal'),
        (3, 'Low'),
    ]
    status_choices = [
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Complete'),
        (4, 'On hold'),
    ]
    privacy_choices = [
        (1, "Private"),
        (2, "Public"),
    ]

#### Comment model

- Comment model was created for user to comment on an task

| Name       | Database Key | Field Type    | Validation                      |
| ---------- | ------------ | ------------- | ------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE  |
| task     | task        | ForeignKey    | Task, on_delete=models.CASCADE |
| created_on | created_on   | DateTimeField | auto_now_add=True               |
| updated_on | updated_on   | DateTimeField | auto_now_add=True               |
| content    | content      | TextField     | blank=False                     |

## Features

### Home Page

- This is the welcoming page for all users
- When the user opens the API site, the welcome page appears in front of them.

### Profile List Page

- This page consists of profile list of all users

### Profile Detail Page

- This page consists of profile detail page
- If user is owner he can edit and delete his profile

### Task List Page

- This page consists of a list of all tasks which have been posted
- This page also consist a task create form for logged in user

### Task Detail Page

- This page consists of the task details
- If user is the task owner he can edit and delete his task that he has created

### Comment List Page

- This page consists of comment list of all comments posted on the tasks
- This page also consist a comment create form for logged in users

### Comment Detail Page

- This page consists of comment detail
- If user is owner he can edit and delete his comments what he has posted

## Validation

### Python

- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files.
- NOTE: The validation was done to all custom python files written by me. Settings.py and env.py was excluded because it contains important data which is longer than 79 lines and cannot be changed.

## Testing

- Testing of the website can be [seen here](/TESTING.md)

## Deployment

### Creating Database using ElephantSQL

1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance.

- After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.

### Deploying the website in Heroko

- Before deploying in Heroku following files were created:
  1. env.py : stores confidential data eg. API keys, passwords etc.

2. Procfile : Very important for deployment and must be added with capital P

3. Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project

- The website was deployed to Heroko using following steps:

#### Login or create an account at Heroku

- Make an account in Heroko and login

#### Creating an app

- Create new app in the top right of the screen and add an app name.
- Select region
- Then click "create app".

#### Open settings Tab

##### Click on config var

- Store CLOUDINARY_URL file from in key and add the values
- Store DATABASE_URL file from in key and add the values
- Store SECRET_KEY file from in key and add the values
- Store ALLOWED_HOST in key and add the value
- Store DISABLE_COLLECTSTATIC in key and add the value

##### Add Buildpacks

- Add python buildpack first
- Add Nodejs buildpack after that

#### Open Deploy Tab

##### Choose deployment method

- Connect GITHUB
- Login if prompted

##### Connect to Github

- Choose repositories you want to connect
- Click "Connect"

##### Automatic and Manual deploy

- Choose a method to deploy
- After Deploy is clicked it will install various file

##### Deployment

- Project was deployed in Heroku

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
4. [GitHub Repository](https://github.com/Sinha5714/pp5-api-ref)

### Cloning the repository in GitHub

1. Visit the GitHub page of the website's repository
2. Click the “Clone” button on top of the page
3. Click on “HTTPS”
4. Click on the copy button next to the link to copy it
5. Open your IDE
6. Type `git clone <copied URL>` into the terminal

## Credits

The code for the API is based heavily on the drf-api from the Code Institute course.

### Code

- The code was written with the help of Code Institute walkthrough project [drf-api](https://github.com/Code-Institute-Solutions/drf-api)

## Thank Yous

- My mentor Jubril Akolade for the export guidance and the patience to explain things in a way that i understood
- Sarah on the CI tutor support for help with the CHOICES and front end field validation
