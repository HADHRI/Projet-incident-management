# Projet-incident-management
* Read all the guidelines first then attempt any of the instruction.

Software Requirments.
1- Python 
	
2- Postman
	- for API testing

Python Installation guide: ( Every Step is crucial )

- Uninstall Anaconda or any other IDE or software that runs python. 
	
	* Run your notebook on kaggle or google colab for demonstration. 

- When running setup , don't forget to check "Add Python to PATH Variable" 
	


After Installation guid:

- open a command prompt and install the required packages:
	- write following commands one by one:
	- pip install django
	- pip install djangorestframework
	- pip install sklearn
	- pip install pandas

- go to the directory where project is stored (open the first folder only,  manage.py file is present)
Add bestmodelrandom.pkl ( the file generated ) in MLAPI directory otherwise it will not work ! 
- open a command prompt there 
	-write:	py manage.py runserver (if it doesn't run)
	- python manage.py runserver
	- if run is successful you should get a message on screen: 
		* Starting development server at http://127.0.0.1:8000/
		* the port no is important if not 8000 then replace it in with the given in further steps.

- Open postman software now
	-> create a request (there would be a button)
	-> select POST request
	-> on address bar write: http://localhost:8000/predict/
	-> click on body
		- radio button 'raw'
		- select JSON (default would be text)
	-> Write following in body:
{
    "reassignment_count": 0,
    "sys_mod_count": 0,
    "caller_id": 2254,
    "opened_by": 8,
    "location": 143,
    "category": 55,
    "subcategory": 170,
    "assignment_group": 56,
    "assigned_to": 0,
    "opened_at_day": 29,
    "opened_at_month": 2,
    "opened_at_minute": 16,
    "sys_updated_day": 25,
    "sys_updated_month": 2
}
	* you can change values according to you. 
	-> hit the send button
	-> that's it (you should have a response below that says "predicted duration is...." 

	