Login Base

LoginBase is a "Serverless" User Login system with Online Database (Google FireBase)
The Local client is Written in pure py and using PyQT for GUI.

ALL Database Rules Are Locked. both Read and Write.
any connaction to the DB is by Firebase Cloud Function (provided with this git {JS10})

LognBase connaction is splitted into 3 oporations.
1) Google auth hold user emails - passwords - uid  (Admin do not have acccess to passwords. only reset email can reset pass).
2) Firebase Function "On user create" will open up a uid with data on every auth registration.
3) Client use the uid to talk with the main database with cloud functions requests.

No data is saved or running on the local client.
User can only access his own uid data.
All the importent data is prossecced on the cloud functions. user cant access or change the data. local modding of the data will not help since its running on the pre defined firebase bucket.


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
Must!!
(
  Firebase account - https://firebase.google.com
  Pc with python installed so we can build local env
  App / Data you wanna lock with login system
)
