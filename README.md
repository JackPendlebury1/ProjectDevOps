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

## Database ERD

![ERD]()

## Project Management
for this trello was what i used for this. This allowed me to follow a clear plan to streamline the development process in an agile way throught the project, moving tickets 
to the relevent position in the development stage

![Trello]()

## CI
for the CI server i used Jenkins this is what the pipline that i have setup looks like

![CI]()

## Testing
For testing I used pytest to provide me test coverage of the flask application when conducting unit testing, 
for intergration testing i will be using selenium.
getting as close to 100% is ideal, showing all functions have been tested before being deployed.

![Pytest]()

## Risk Assessment

## Future Improvements

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