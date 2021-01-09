We strongly recommend avoid use google services.
above high fat random bills any other services will provide the same.

use django and backend kick google to the bin.


thank you google for blocking parler and showing all of the internet what an uncontrolled monster you become.

we gonna leave the data as is but again we strongly recommend you to AVOID USE ANY GOOGLE SERVICES.
you dont need them and it just gonna cost you money while they keep pushing politics into our internet.


**Login Base**

Home

![python3_WUWGB0Njce](https://user-images.githubusercontent.com/52171360/97435929-d69e8a80-1929-11eb-915f-f3cad30b0600.png)

Register

![python3_1fTHF1SRoa](https://user-images.githubusercontent.com/52171360/97435937-d8684e00-1929-11eb-9fc3-b76be183350b.png)

Recover

![python3_PRXT0v2MUB](https://user-images.githubusercontent.com/52171360/97435940-d900e480-1929-11eb-8a88-afe888f166f6.png)


LoginBase is a "Serverless" User Login system with Online Database (Google FireBase)
The Local client is Written in pure py and using PyQT for GUI.

![python (1)](https://user-images.githubusercontent.com/52171360/97438564-a3f69100-192d-11eb-824a-3f423b17199d.png) ![Qt](https://user-images.githubusercontent.com/52171360/97438892-1bc4bb80-192e-11eb-9937-c60cb9fd78db.png) ![Js](https://user-images.githubusercontent.com/52171360/97438891-1b2c2500-192e-11eb-8ea3-e9b1a45f2289.png) ![Fire](https://user-images.githubusercontent.com/52171360/97438342-57ab5100-192d-11eb-8422-48f5c5cfbbb5.png)

ALL Database Rules Are Locked. both Read and Write.
any connection to the DB is by Firebase Cloud Function (provided with this git {JS10})

![chrome_eptgEcXPyl](https://user-images.githubusercontent.com/52171360/97439095-6a725580-192e-11eb-9b17-cec1f1db765c.png)

LoginBase connection is splitted into 3 operations.

1) Google auth hold user emails - passwords - uid  (Admin do not have access to passwords. only reset email can reset pass).
2) Firebase Function "On user create" will open up a uid with data on every auth registration.
3) Client use the uid to talk with the main database with cloud functions requests.

JS10 Cloud Function and uploaded Function in firebase console:
![Code_JQbnMFjYpN](https://user-images.githubusercontent.com/52171360/97439210-8ece3200-192e-11eb-84d0-e59b01fddf12.png)
![chrome_WKTIRwKsco](https://user-images.githubusercontent.com/52171360/97439337-b7562c00-192e-11eb-9d88-195a477a4d55.png)

No data is saved or running on the local client.
User can only access his own uid data.
All the important data is processed on the cloud functions. user cant access or change the data. local modding of the data will not help since its running on the pre defined firebase bucket.

Auth user and realTime database data:
![chrome_8uqfNAJFho](https://user-images.githubusercontent.com/52171360/97439868-672b9980-192f-11eb-85c2-bdbc89f7f67e.png)
![chrome_PWwn1eW27g](https://user-images.githubusercontent.com/52171360/97439872-685cc680-192f-11eb-929c-afa2c280f32f.png)

The system Demo Full working User login system.
User Trails
User Groups
User Register
User Password Recover

You can Fully integrate the system with your very own firebase account For Free!!
Every part of what you see above is free open source or open services. (above register nothing is needed..)

Lock your app (any app) - Protect your data - Add Remote ability to any Client

Once setup is done Everything can be controlled from Firebase web Console.

Stuff Needed To start:

  *Firebase account - https://firebase.google.com

  *Pc with python installed so we can build local env

  *App / Data you wanna lock with login system
  
  * Microsoft VS Code https://code.visualstudio.com/  (we used free. not sure they got payment options)


Install:

Build environment 
Get liberty into the new venv.

***1)*** Open local text editor and save this lines with .bat
then run to grab everything into "venv" on the local folder you are running.
```
python3 -m venv venv
call venv/scripts/activate.bat
python -m pip install --upgrade pip
pip install PyQt5==5.9.2
pip install Pyrebase
pip install --upgrade PyUpdater[all]
pause
```
***2)*** after python have created the libs he need you can copy paste the Source Code into the folder root.

Folder Structure after Copy

-New folder to hold project

---Venv (folder)

---resources (folder)

---Gui (folder)

---main.py

--client_config.py


***3)***
Open Firebase Account
Watch video Firebase setup

***4)***
Set Local firebase CLI (with command prompt so we can push our stuff from local pc)
Copy the function JS to your new Firebase Function Folder.
Change / Mod / Edit
push when done
you can view and test your functions local before pushing (DB will be updated we emulate only the request)

***5)***
Intargte Firebase Public key each project got one. (This is not account service key or secret key!!!!!!!! WE DO NOT USE THOSE. Never ADD Secret Key or Service Account Key!!!!!!!!!)

Gif how to view and copy account public key

once you change the api to your public api you can run the app and everything will be hooked.
you can register.
login.
recover.


Add this
Copy this
Do this...


Integrate:
Copy public api key and replace "API HERE"
Push the Ready to go Cloud Functions (you can also change the data writing and push)
Lock your firebase RealTime Database with No Read and Write allowed.

Test:
Signup user
DB Write Gif 
