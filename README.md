# MedXpert
A mobile and web-based application that will enable users to view, search, get recommendations on, make appointments with, notify, and set up automation to contact health facilities like hospitals, clinics, and ambulances when needing medical attention.

## Demo
[Video](https://www.youtube.com/watch?v=djY5PCIWqpk)
## About MedXpert
TL;DR [Video About Medxpert](https://www.youtube.com/watch?v=CdRrbXms5kg)

Getting fast medical attention when one needs is clearly very important, and things like emergency lines, ambulances, and denser health facilities have been used to that end, but while Ethiopia might have and be in the process of implementing those, there has been no exploitation of what ICT could give in closing the gap between those that need medical attention and the health facilities. The prevailing way of getting medical services is to go to a health facility one knows or is told of and make an appointment. And when one needs immediate medical attention one could call an ambulance which could be very far or not the best choice, assuming either the person in danger is conscious and can call, or there is someone else who can. This means that the medical attention given could be inefficient, slow, and, in places where the involved are new to the place, unreliable, and potentially requires outside help. To better this and combat its problems, we propose a digital system that makes appointments faster and efficient and addresses health emergency cases more reliably. The system will allow people to view health facilities, and make appointments. It will show the facilities with their relevant details, enabling people to choose one that has what they need and is also close. In cases of emergencies, it will allow people to launch an emergency sequence they have set up that will get them medical attention and/or some help. Furthermore, it will detect if a person's phone is falling – which could indicate that the person may have a heart attack, seizure, etc. – and if the user is unresponsive, it will launch an emergency sequence (of the likes described above). This would especially help those with health conditions predisposing them to such emergencies.

# Installation and Setup
### Setting up the Database
First, make sure you have the Postgres database with its Application Stack Builder installed.
1. Open the Application Stack Builder.
2. Select the postgress installation you have and click next.
3. Tick PostGIS Bundle for PostgresSQL under Spatial Extentions and select next. PostGIS will be installed.
4. Open and login to SQL Shell.
5. Creating a database and adding postgis extension to it.
```
$ CREATE DATABASE SOME_DATABASE_NAME;
$ \c SOME_DATABSE_NAME;
$ CREATE EXTENSION postgis;
```
### Running The Server
First, make sure you have Python version 3.8.10 installed.
1. Creating and Activating Virtual Environment
```
$ python -m venv virtual_environment_name
$ source virtual_environment_name/Scripts/activate
```
2. Installing Dependencies
```
$ pip install -r requirements.txt
```
3. Defining Environmental Variables
Add a file called .env in the root directory and define the following variables in the following format.
```
MEDXPERT_DB_NAME=THE_DB_NAME
MEDXPERT_DB_USER=THE_DB_USER_NAME
MEDXPERT_DB_PASSWORD=THE_DB_PASSWORD
RECOMMENDATION_SERVER_API_KEY=THE_RECOMMENDATION_SERVER_API_KEY
API_KEY=RANDOM_STRONG_API_KEY
```
4. Running the Server
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
### Accessing the Admin Portal
Go to http://localhost:8000/admin

## Frameworks and Technologies:
- Django
- Postgres
- Postgis
- GeoDjango
- Socketio

## To setup the backend 
[How to setup medxpert frontend](https://github.com/MedXpert/medxpert_frontend#readme)
# Team Members
| Team Member | Contact |
|--|-|
|Betemariam Moges|[Github](https://github.com/BgitBB)|
|Dawit Bezabih|[LinkedIn](https://www.linkedin.com/in/davenbezz/)|
|Liyu Mesfin|[LinkedIn](https://www.linkedin.com/in/liyumk/)|
|Michael Belete|[LinkedIn](https://www.linkedin.com/in/michael-belete-8600a3176/)|
|Naol Dame|[LinkedIn](https://www.linkedin.com/in/naol-dame-38783b213/)|
