Information Security Project 2021

-Rene Zorzi
-Samuel Sanna
-Axel Mezini

Not-Secure-Branch
Here is the insecure version of the web application. On the web app you can register, login and search for posts. 
You can also create, comment and delete a post on the home page. There is an about page and an account page with the posts that that user created.
This version of the application is vulnerale to differente attacks.

Secure-Branch
This version has the same functionalities as the insecure version plus you can delete your account. This version is not vulnerable to the same attacks as before.

Libraries needed to run both versions are:
pip install Flask
pip install Flask-SQLAlchemy
pip instal WTForms
pip install Flask-Login
pip install Flask-Bcrypt


## 02/06 Edit
- Small fix of versions structure and order
- Delete is possible in both versions but only for posts without answers (or with all precedent answers deleted) and for users that have not created any post (or all posts deleted). This feature is not fully implemented and may raise a server error in different cases.

- Videos uploaded
  - Standard Scenario = https://www.youtube.com/watch?v=bFAOHIJ1qPo
  - SQL Injection and XSS Insecure Version = https://www.youtube.com/watch?v=R8swmwUyypE
  - SQL Injection and XSS Secure Version = https://www.youtube.com/watch?v=wCKjdDNhgys


