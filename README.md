### About
This project is an online complaints portal where students can register complaints related to hostel environment and workers solve the registered complaints. This portal is built using Django.

Common problems faced by students in hostels of NIT Rourkela include: fan not working, tubelight not working, broken window panes, water cooler not working, LAN not working, etc. The students always need to go to __Chief Warden Office__ or __Data Center__ to register their complaints. Then the students need to wait for several days and the respective worker comes to the room/corridor and solves the problem. This is quite inefficient as there is no visibility in tracking the status of the problem as to when the worker sees the problem and arrives at the scene to solve the task. Our project aims to solve this issue by building an online portal to keep track of the problem status. We have also added a discussion system that allows users to discuss about when the worker needs to arrive to match the availability of student.

### Build steps

1. Create a virtual environment in python (3.8.1).
2. Download this repo and `cd` into it.
3. Inside the virtual environment type: `pip install -r requirements.txt`
4. Setup the database migrations script: `python manage.py makemigrations`
5. Execute the migrations script: `python manage.py migrate`
6. Run the server by the typing the command: `python manage.py runserver`
7. The server should be live at: http://127.0.0.1:8000/

**Note:** After downloading this repo one needs to create .env file that stores the secret key of the Django application and sendgrid api key for email backend.

**Example .env file:**

`
SECRET_KEY=XXXXXXXXXXXX
`

`
SENDGRID_API_KEY=XXXXXXXXXXXX
`
### Apps

There are 4 major apps in the project as follows:

- **accounts**
	- This handles all the registration of the user. There are two categories of user: __student__ and __worker__. This is identified by user type when a user registers on the portal. __student__ can only create, update and delete complaints. __worker__ can only update the status of the complaints. Registration was handled by **django-registration-redux** application. Email backend for verification and password reset was handled using **sendgrid**.

- **student**
	- This handles the content available for use by a __student__ type user. The actions available to perform are create, update and delete complaints.

- **worker**
	- This handles the content available for use by a __worker__ type user. The actions available to perform are update status of complaints. A __worker__ can update those complaints having complaint type as of the __worker__. For example if the __worker__ is an electrician, then he/she can update statuses of complaints that are electrical in type. Similarly, a plumber can update statuses of complaints that are marked as plumbing type.

- **comments**
	- This handles the comments made by a user. User can comment on any complaint. They can see the comments made by them on any complaints and update or delete them if necessary.