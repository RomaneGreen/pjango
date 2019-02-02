


Renmo:
A web application using Python & Django.A test of my basic understanding with the framework and language.
Project Overview:
Small payment processing app. Think of apps like Venmo, Cash App, and PayPal. This application must be built in Python/Django and have the following features ->
Email/Password Authentication:
A user can register a new profile or log in with name/email and password combination
Google Oauth:
User has the option to login in via Google Oauth, or via Github an alternative (in addition to conventional login)
Profile to update personal info:
A logged in user can access "My profile" link to update their Firstname,Lastname and Email adress
Stripe for payment processing:
The App uses token based system via stripe for payment processing since handling tokens directly on a server is risky,which then allows users to purchase tokens and use them as currency.
Database to track the transactions between users:
The Sqlite database is used to track tranaction between users.A MySql or Postgres database was considered but seemed overengineering for a small app,especially with Django admins capabilities.
A note attached to each transaction:
Notes are a mandatory field attached to each transaction.A user cannot send tokens without a note attached.A timestamp is also added to each transaction,something I feel is necessary for applications in which transactions are recorded
A newsfeed to see all the current users transactions:
A logged in user with have access to a newsfeed on the homepage,in which he or she can view recent transactions.
Tests:
The home,add token,send tokens pages are all unit tested,as well as two mock database tests for the UserProfile model and TokenTransfer model.
Misc
The App is deployed via pythonAnywhere http://romane71193.pythonanywhere.com/ . Light styling using Bluma css and bootstrap.
