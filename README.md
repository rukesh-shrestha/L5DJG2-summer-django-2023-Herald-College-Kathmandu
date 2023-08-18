# L5DJG1 - summer-django - 2023 - Herald College Kathmandu 
To download and use this project. Follow the below mention steps. 

## Clone the project
To clone the project using SSH. Choose the option 1 otherwise you can go with option 2. 
- If you choose option 1. You have to setup the SSH in your local machine and Github.
- Option 1
  
  ```
  git clone git@github.com:rukesh-shrestha/summer-django.git myproject
  ```
- Option 2

  ```
  git clone https://github.com/rukesh-shrestha/summer-django.git myproject
  ```

## Set the Environment
- Go to myproject
  
  ```
  cd myproject
  ```
- You can create the virtualenv for the isolated environment. If you don't want to create the env you can skip this step. Click [here](https://pypi.org/project/virtualenv/) to know more details to create the virtualenv.
- installing the dependency from requirement file
  
  ```
  pip install -r requirements.txt
  ```
  - create the env file in the root project then populate with below data.
  - DATABASE=YOUR-DATABASE-URI
  - SECRET_KEY=YOUR-SECRET-KEY
  - EMAIL_BACKEND=YOUR-EMAIL-BACKEND
  - EMAIL_HOST=YOUR-EMAIL-HOST
  - EMAIL_HOST_USER=YOUR-EMAIL-ADDRESS
  - EMAIL_HOST_PASSWORD=YOUR-EMAIL-PASSWORD
  - EMAIL_PORT=YOUR-EMAIL-PORT
  - EMAIL_USE_TLS=YOUR-BOOLEAN-VALUE
  - DEFAULT_FROM_EMAIL=YOUR-DEFAULT-VALUE


## Run the project
  - Migrate the database
    
    ```
    python manage.py migrate
    ```
  - Run server
    
    ```
    python manage.py runserver
    ```
  - Nagivate to the localhost and enjoy 


## Main Feature
- User Management System.
- Dynamic Email Sending.
- CRUD operation for the Blog.


## Want to Collaborate
- You can add new feature, push to the new branch and send the pull request. 
