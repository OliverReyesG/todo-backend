# Installation

## Clone this repository by using the following command

```bash
git clone https://github.com/OliverReyesG/todo-backend.git
```

### Then cd into the "todo-backend" directory

```bash
cd ./todo-backend/
```

# Create a python virtual environment

## Use the following command to create the virtual environnment

```bash
python3 -m venv ./venv
```

## Activate the virtual environment

### [Mac OS / Linux]

```bash
source ./venv/bin/activate
```

### [Windows]

```
venv\Scripts\activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

# Add environment variables

## Create a file named ".env" in the root folder of the project

### Open the ".env" file in your text editor of choice and add the following environment variable to it: SECRET_KEY = " "

### You need to asign a [string] value to this variable which is going to be the secret key for your project

# Create migrations

## First run

```bash
python manage.py migrate
```

## Then run

```bash
python manage.py makemigrations
```

# Create superuser

```bash
python manage.py createsuperuser
```

# Run tests

```bash
python manage.py test
```

# Run development server

```bash
python manage.py runserver
```
