# Django Ticketing System

Now your customers can get help in real time by opening support tickets and collaborating with support agents.  

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

A ticketing system improves your customers experiece while using your service or product. Not only your customers but internal users as well. With the ticketing system, one can attend to issues in real time, see tickets on queue, assign to different engineers and make your customers/internal users feel confident in your I.T operations and customer-centric system. This particular project was setup with easy-to-use features, which emulates the basics of a ticketing system - which is ease!

## Features

Here are what makes the project tick! Please go through the features to see why this project is awesome!

- Simple Dashboard
    - This is the landing page for all authenticated users. However, users would be directed to the login page when they are not authenticated.
    - You can add customizations to change the looks of the dashboard to suit your taste.
- Multiple User Types
    - Due to the nature of the project, it's only right that it carries a MUT, for better role, rights and privilege checks.
- Automatic Ticket Status Update
    - Updates on tickets' status are done automatically as the ticket moves through its lifecycle. Any user can see this happen in real time. 
- Superusers can assign ticket to any engineer
    - There's a ticket queue that can only be accessd by superusers. From this queue, tickets can be assigned to engineers (maybe based on priority or skillset. It's up to you to decide)

## Installation

Setting up and installing this project is quite straightforward and easy. Below are detailed step on how to get this web app up and running. 

1. Install a virtual environment. 
```bash
pip intall virtualenv

```

2. Create and activate a virtual environment 
```bash
virtualenv generic_name

cd generic_name && Scripts\activate
```

3. Clone the project's github repo and cd into project
```bash
git clone https://github.com/chideegit/django-ticketing-system.git

cd django-ticketing-system
```

4. Install all the dependencies contained in the [requirements.txt](./requirements.txt) file. 
```bash
pip install -r requirements.txt
```

5. Make migrations, migrate and  then run local server 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Create a superuser account
```bash
python manage.py createsuperuser

```

## Usage
Navigating through the app is as easy as it look. You can follow through the steps below to have an idea of the experience before diving in yourself.

1. Log in as a superuser and create 'ticket categories' from the [Admin Panel](http://127.0.0.1:8000/admin)
2. Create Engineers (from the admin panel), and make sure to check the 'is_engineer' box, so that the user can have all the roles and priviledges of an engineer. 
3. From the [Register Page](http://127.0.0.1:8000/register-customer), you can register a test customer and log in. 
4. Once logged in as a customer, you can create and manage your tickets. 
5. After a ticket has been created, view the experience from an engineer's scope by logging into the site as an engineer. 
6. While logged in as an engineer, you'd able to work on tickets and resolve them. 
7. Ticket status updates automatically at each point in its lifecycle. Any user can see this happen in real time. 
8. From the super admin scope, you would be able to see all unassigned and active ticket in the app. 

## Contributing
If you would like to contribute to the project, please follow the guidelines outlined in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License
This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.

## Acknowledgments
Special thanks to the Django community for providing a robust framework.

Feel free to reach out for any questions, issues, or feature requests!

Happy coding🚀