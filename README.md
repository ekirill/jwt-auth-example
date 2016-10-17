# jwt-auth-example

This project is simple implementation of limiting users with
permissions per particular resources. It is based on auth with
JWT (https://en.wikipedia.org/wiki/JSON_Web_Token), stored in cookies.

Permissions are stored in JWT.
All resources are numerated and have an id. 
If user has access to the resource, its id is in the list of permissions.
To use less bytes for storing permissions I use bit mask.
For example, if user has access to resource 1 and 3, then
his permissions are represented as int('1010', 2).
To store permissions, which id is more than max bits in an int
I use an array of integers and split bits among them.

This access system is used in my simple flask application.
Flask is used for simple routing only.
Login and logout methods are provided. These methods store and delete
auth cookies. Two api url with different permissions are created for
showcase. See **tests/test_app.py** as usage examples.
