# simple program to commit brute-force attacks with parameter injection arrays on localhost
# - to verify the injection status on vscode split the terminal panel and then at every attack instance there is a new update request in the Flask Application
import requests

# add multiple parameter injection and pollution techniques for both client-side and server-side testing-- Examples are XSS, SQL injections via parameters, etc...

parameter_injection= ["account.html", "home.html"]

#may add multiple post request attacks, note that this post request in order to work, the URL needs to be sending the POST request, for in-form scripting attacks 
# use the website interface

POST_req_parameter= {'form': 'insert some xss scripting attack in here'}

SQL_DB_injection= []

req_header= requests.head('http://127.0.0.1:5000/')
print("ANALYZE THE TYPE OF WEBSITE IMPLEMENTATION: ")
print("Server: " + req_header.headers['server'])
# print("Last modified: " + req_header.headers['last-modified'])
print("Content type: " + req_header.headers['content-type'])


print("\nASSESSING FIRST THE GET REQUESTS ATTACKS")
for i in parameter_injection:
    
    req_session= requests.Session()
    
    # please not that request library contains a prameter variable to add to the url ( may switch to it, if you would like that approach better
    
    req= requests.get('http://127.0.0.1:5000//'+i)
    req_cookies= req_session.cookies
    cookie_list= req_cookies.get_dict()
    print("THE COOKIE USED BY THE WEBSITES ARE: \n")
    print(cookie_list)
    print("THE ENCODING OF THE RESPONSE IS: "+ req.encoding)
    print("WEBSITE REQUEST STATUS IS: " + str(req.status_code))
    print(req.text)

    if req.status_code == 200:
       
        print("The Program could detect a connection volnerability in parameter: "+ i + " \n Please optimize your security")
    else:
        print("The website has not been successful in terms of responses \n"+ "YOU MAY ADD OTHER PARAMETER IN THE LIST TO VERIFY OTHER POTENTIAL VULNERABILITIES FOR "+ i)

    # print(req.json()) 
print(" \n ASSESSING THE POST REQUESTS ATTACKS FOR THE WEBSITE")


# in here the verification of the vulnerability for the post requests
for j in POST_req_parameter:
    if req.status_code== 200:
        response_post= req.post("http://127.0.0.1:5000/", j)
        print(response_post.text)
    else:
        print("THERE COULD NOT BE ACHIEVED A SCUCCESSFUL ATTACK. ")
        
        
# loop to assess the mysql security for the website

for z in SQL_DB_injection:
  if req.status_code== 200:
      response_sql= req.get("http://127.0.0.1:5000/",z)
      print(response_sql.text)
  else:
    print("NO SQL INJECTION COULD HAVE BEEN COMMITTED SUCCESSFULLY")
