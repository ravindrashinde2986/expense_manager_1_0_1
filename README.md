
# Expense Manager 1.0.0

Expenses Manager is a user-friendly, expense management app which allows you to keep track of your expenses.
User can add, modify and delete their expense entries.
Dashboard will provide annual month wise expenses along with categorized expense summary with help of graphs and charts.



## Getting Started
## Running Locally




### Part 1 : Clone the project and create virtual environment

* Clone the Project using following link

    ```bash
    git clone https://link-to-project
    ```

* Go to the project directory

    ```bash
    cd expense_manager_1_0_0
    ```

* You need to install poetry on your machine if it not there already, refer https://python-poetry.org/docs/#installation

* Once poetry is up and running in our machine, we have to create a virtual environment:

    ```shell
    poetry shell
    ```

* then install the dependencies:

    ```shell
    poetry install
    ```

* Set the following environment variables in the same terminal
  _Windows_ :
    ~~~
    set FLASK_APP=src
    set FLASK_DEBUG=1 
    ~~~
  _linux/mac_:
    ~~~
    export FLASK_APP=src
    export FLASK_DEBUG=1
    ~~~
## Part 2 : Install PostgreSql & Create Database

* You need to install PostgreSql server on your machine if it is not there already. Here is the download link https://www.postgresql.org/download/.

* Once PostgreSql is installed on your machine, connect it with any Database management tool like pgAdmin or DBeavar or any other tool of your choice which can connect to PostgreSql server with default user/password. I personally use DBeavar.
* Create Database using
    ~~~
    CREATE DATABASE expense_mgr_db;
    ~~~
* Go to **_src_/\__init\__.py** and search for **app.config['SQLALCHEMY_DATABASE_URI']** and changes it's values to "postgresql://**<your db user>**:**<password>**@localhost:**<db_port_number>**/expense_mgr_db"

## Part 3 : Run Migration (Create db schema)

* Inside poetry shell run following commands
    ~~~ 
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
    ~~~
    This will generate schema/table in database
    
## Part 4: Run the application
* At the end of this process, you can start the application by running
    ```bash
    flask run
    ```
* You should see following when it run successfully.

    ```bash
      * Serving Flask app 'src'
      * Debug mode: on         
      * Running on http://127.0.0.1:5000                                                                                                                                                                                    
      * Debugger is active!      
      * Debugger PIN: 233-559-797
    ```


## Roadmap

- Deployment on production server with Gunicorn and NGINX 
- Login with Google/Facebook account
- Containerization with docker
- Publicly exposed APIs for 3rd party integrations
- More Charts/Tables
- Additional browser support