# flask_mysql_autocomplete_docker
This project is a simple web app that automatically suggests search locations from approximately 15,5000 prepopulated records in the database.

## Getting Started

***Step 1:*** Make sure git is installed on your os. I will be using windows 10 for the project.


***Step 2:*** Clone the project into your local machine using below command.

git clone https://github.com/Asif-Rumee/flask_mysql_autocomplete_docker.git

### Prerequisites

#### 1. Docker

Make sure you have Docker installed. Please follow the below link for official documentation from Docker to install latest version of docker on your os. For this project I am using Docker CE (18.09).

https://docs.docker.com/docker-for-windows/install/

### Installing

***Step 1:*** Change to the directory where the project was cloned in previous step. 

**cd flask_mysql_autocomplete_docker**

***Step 2:*** Make sure Docker is up and running. You can start the docker engine from start menu on windows.

***Step 3:*** Run

**docker-compose up**

***Step 4:*** Change directory to app/ **cd flask_mysql_docker/app**

run python script **cmd python application.py** 

***Step 5:*** Open up the browser and paste the below url
**http://localhost:5000/**



***Step 6:*** Verify DB is up and running and tables are created

Use any of the database clients like MySQL workbench or SQLDeveloper. In my case, I am using the MySQL workbench.

Connect to MySQL database using the properties specified in docker-compose.yml file with host as localhost.

**Note:**

Use the MYSQL_ROOT_PASSWORD and MYSQL_DATABASE in the DB URI.
Use 3360 as port to connect the MySQL server as it's the port which is exposed by the docker container bearing the MySQL image.
The port to be used is 5000 which is the port on which app will be running on localhost.



### Built With

* [Docker](https://www.docker.com/) - Deployment model
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework
* [Python](https://www.python.org/) - programming language
* [pip](https://pip.pypa.io/en/stable/) - Package and dependency manager
* [MySQL](https://www.mysql.com/) - Database
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python sql toolkit and ORM
* [jQuery](https://jquery.com/) - JavaScript library to manipulate html  
