# ProjectDevOps

## Trello
Link to Trello Board: [Trello](https://trello.com/b/A1Rkz7Qx/devops-project1)

## Breif
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

this project should include:

- Project Management
- Python
- Python Testing
- Git
- Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

## Approach to the project
- Create a user
    - Username
    - Password
    - Email
    - First name
    - Last name

- Login User
    - Compare hashed password to text password

- Add Song for user
    - song name
    - length
    - artist
    - release date

- add/delete/update Song
    - delete songs from the user
    - update any song for the user

- Delete user
    - allow the user to delete their user

- Update user
    - update password
    - update email address
    - update username

- allow the user to view their details

- allow the user to view their songs

## method

**how i choose to go about this project was a simple approach i would get the very basics working, so displaying templates, i would then build on that and then move into functionality for that template. With my login page as an example what i did was first built the most simple route i could think of which would just display the login template, from this i then build a simple form which allowed the user to enter their details, i then gave the form to the template, and then added the extra functionality to the login route.**

## Database ERD

![ERD](https://i.imgur.com/LN7SZ02.png)

## Project Management
for this trello was what i used for this. This allowed me to follow a clear plan to streamline the development process in an agile way throught the project, moving tickets 
to the relevent position in the development stage

![Trello](https://i.imgur.com/bwyNVOB.png)

## CI
for cd i wanted to go beyond the spec, i know this isnt good pratice but i was very interested in jenkins and i didn't like leaving it unfinished. I have 2 jenkins jobs one that firsts tests the application with pytest, takes the coverage file and creates that into an artifact. This is all done continiously with a webhook to jenkins from github. the second job is to dockerize my application and run it within a container. I thought this step was needed because the job wouldn't finish there for not showing the true progress of the application.
for the CI server i used Jenkins this is what the pipline that i have setup looks like

![CI](https://i.imgur.com/hlwRERz.png)

## Testing
For testing I used pytest to provide me test coverage of the flask application when conducting unit testing, 
for intergration testing i will be using selenium.
getting as close to 100% is ideal, showing all functions have been tested before being deployed.
automated testing whenever pushed from github is useful and allows the version to fail if the testing also fails which would stop the next job, deploying the website to also stop.

![Pytest](https://i.imgur.com/odf5QYM.png)

## Risk Assessment

![Risk Assessment](https://i.imgur.com/QfTim7r.png)

## Future Improvements
- uploading images
- UI changes
- css and javascript to improve UX
- to split the application up further for readablity and maintainablity 

## Author
**Jack Pendlebury**

## how to install

```sh
$ git clone https://github.com/JackPendlebury1/ProjectDevOps.git
```

```sh
$ cd ProjectDevOps
```

```sh
$ pip3 install virtualenv
```

```sh
$ virtualenv venv
```

```sh
$ source venv/bin/activate
```

```sh
$ pip3 install -r requirements.txt
```