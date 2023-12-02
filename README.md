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

1. Log in as a superuser and create ticket categories from the [Admin Panel](http://127.0.0.1:8000/admin)
2. Create Engineers

## Contributing
If you would like to contribute to the project, please follow the guidelines outlined in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License
This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.

## Acknowledgments
Special thanks to the Django community for providing a robust framework.

Feel free to reach out for any questions, issues, or feature requests!

Happy coding🚀