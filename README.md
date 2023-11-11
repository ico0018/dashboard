## How to Run

To get the My Dashboard project up and running, follow these steps:

### Install Virtualenv

First, install `virtualenv` on your machine.

To install `virtualenv`, run:

```
pip install virtualenv
```

Create and Activate a Virtual Environment
Create a virtual environment in your project directory:

```
virtualenv venv
```

Then, activate the virtual environment. On Windows, use:

```
venv\Scripts\activate
```

On Unix or MacOS, use:

```
source venv/bin/activate
```

### Install Project Dependencies

Install the necessary project dependencies using pip:

```
pip install -r requirements.txt
```

### Set Up Flask Application

Before running the server, set the Flask application environment variable. This can be done with the following command:

```
export FLASK_APP=run.py
```

For Windows users, use:

```
set FLASK_APP=run.py
```

### Run the Flask Server

With everything in place, start the Flask server:

```
flask run --debug
```
The --debug flag launches Flask in debug mode, which is useful during development as it automatically reloads the app on code changes and provides debug information.

Access the application at http://localhost:5000 in your browser.

## Admin Interface
To manage the database, navigate to http://localhost:5000/admin. This admin interface allows for direct manipulation and management of the database entries.

## Database Configuration
In the file: apps/config.py file

```
class ProductionConfig(Config):
    # ... other config settings ...
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
    # ... other config settings ...

class DebugConfig(Config):
    # ... other config settings ...
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
    # ... other config settings ...
```
