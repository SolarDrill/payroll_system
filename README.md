<!-- ABOUT THE PROJECT -->
## Django Payroll System

This is an application built using Python/Django from scratch using the default startproject.

### Installation

1. Clone the repo, get into the project folder and change to "ramon_gomez" branch
   ```sh
   git clone https://github.com/anthomme06/backend-django-interview-test.git
   ```
2. Install pipenv for the environment
   ```sh
   pip install pipenv
   ```
3. Install the packages
   ```sh
   pipenv install
   ```
4. Run the virtual environment
   ```sh
   pipenv shell
   ```
5. Apply the migrations
   ```sh
   python manage.py migrate
   ```
6. Create a superuser
   ```sh
    python manage.py createsuperuser
   ```
7. Run the Development Server
   ```sh
   python manage.py runserver
   ```
### Description
   I added a model aside from the requirements called "OpenPosition" where we can register available jobs, the institution that is in need of it and the department of the solicited job.
      *I allowed non-authenticated users to view open positions since it's information that should be public to get people to apply.   

   Url for the API documentation: http://127.0.0.1:8000/api/v1/docs/
   
### How to run Unit Tests
   The tests are located inside payroll_app in a folder called tests. That's the command to run the endpoints tests, there's one for models only, but while testing endpoints it's already generating data for the models.
   ```sh
   python manage.py test payroll_app.tests.test_endpoints
   ```
   
## ANY QUESTION FEEL FREE TO CONTACT ME



