Steps to install and run the application

1. Create the virtual envirmment. 
    If you are using Linux, 
        a. use "virtualenv virtualenv_name" command to create the virtual environment
        b. use "source virtualenv_name/bin/activate" to activate the environment
    If you are using windows,
        a. use "mkvirtualenv virtualenv_name" command to create the virtual environment
        b. use "workon virtualenv_name" to activate the environment
2. Clone the repository using:
    git clone https://github.com/katejasagar/Monsoon_To-do-List.git
3. Move to folder Monsoon_To-do-List
    cd Monsoon_To-do-List
4. Install all the requirements:
    pip install -r requirements.txt
5. Create database using:
    python manage.py makemigrations
    python manage.py migrate
6. To use default admin portal of Django
    python manage.py createsuperuser
    Enter the username, emailId and password
7. To run the applicaition
    python manage.py runserver

Now your application will be running on the local server. You will be able to access at 127.0.0.1:8000

Description:
Application contains the home page, where we can add the task in the todo list. It displays the task name and the created time and date. 
Each task contains the update and delete button. On update page we can change the status of the task and from delete page we can delete the task from our to-do list. 

