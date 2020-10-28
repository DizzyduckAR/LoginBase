Login Base

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
any connaction to the DB is by Firebase Cloud Function (provided with this git {JS10})

RulesIMG

LognBase connaction is splitted into 3 oporations.

1) Google auth hold user emails - passwords - uid  (Admin do not have acccess to passwords. only reset email can reset pass).
2) Firebase Function "On user create" will open up a uid with data on every auth registration.
3) Client use the uid to talk with the main database with cloud functions requests.

CloudFunc IMG

No data is saved or running on the local client.
User can only access his own uid data.
All the importent data is prossecced on the cloud functions. user cant access or change the data. local modding of the data will not help since its running on the pre defined firebase bucket.

Db IMG

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



Install:

Req
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
