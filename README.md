# Django Messenger Bot Template

A project starter template for Django 1.11 that is production ready for creating a Facebook Messenger bot deployed to Heroku. Created by Bytesize.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Base application for developing a Facebook Messenger bot with all the helpful utilities.
- Uses Python 2.7.

## How to Use

To use this project, follow these steps:

### Seting up your Environment

Install Django:

    $ pip install django

### Creating your Project

Using this template to create a new Django app is easy:

    $ django-admin.py startproject --template=https://github.com/rohitahuja/hcs-bot-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

### Setting up the Project

Enter your project folder:

    $ cd helloworld

Create your virtual environment and activate it:

    $ virtualenv venv
    $ source ./venv/bin/activate

Install dependencies:
    
    $ pip install -r requirements.txt

### Deployment to Heroku

Initialize version control for the project:

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

Create a Heroku project:

    $ heroku create
    $ git push heroku master

### Connecting to a Messenger Bot

Create your messenger bot on https://developers.facebook.com/ 

Add the products Messenger and Webhooks. On the Webhooks tab, create a New Subscription with the Callback URL as `http://<your-heroku-subdomain>.herokuapp.com/webhook/` and the Verify Token as ``johnharvard``. For Fields, check ONLY ``message``.

On the Messenger tab, under "Webhooks", subscribe the webhook we just created to the page you want to connect your bot to. Also, under "Token Generation", generate a token for the page we're connecting to and replace the variable ``page_access_token`` at the top of ``message.py`` with it.
