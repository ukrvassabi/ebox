### Info

Application allows to login with google account. After login user will see his/her last 100 emails (if there are 100 emails in inbox)

#### How to run?

* You should have preinstalled Docker and [Docker compose](https://docs.docker.com/compose/install/)

* Pull sources and in the project folder create .env file with next content:
	```
	SECRET_KEY=<random>
	DEBUG=<True|False>
	DB_NAME=<db_name>
	DB_USER=<db_user>
	DB_HOST=db
	DB_PORT=5432
	GOOGLE_KEY=<your google client id>
	GOOGLE_SECRET=<your google secret>
	```

* Run folowing commands:
	`sudo docker-compose build`
	`sudo docker-compose run web python manage.py migrate`
	`sudo docker-compose up`

* Open `http://localhost:8000`
* Login with your Google credentials.