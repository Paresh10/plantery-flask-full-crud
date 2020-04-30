## Project # 3: Plantery```React```  & ```Flask```

##### About:
Fully functional ```CRUD``` ```React``` & ```Flask``` app that provide thorough information about plants.

#### User Story:
1. User can can sign up and login.
2. User can create profile at the sign up page or update once logged in.
3. User have the ability to add new plant, edit/update or delete.
4. User can see all the plants posted including other people's post.
5. User can click on see info tab on the plant image and the modal box will open which contains all the information about that particular plant.
6. User can all see their postings in the see my plants tab which contains all the information about their added or updated plant.
7. User can delete their account which will delete all the information about them including all the postings.

#### ```Model-User```

| User           | Type        | ID     |
| -------------  |:-----------:| -----: |
| Name           | CharFeild() |  –
| Email          | CharFeild() |  –
| Username       | CharFeild() |  –
| Password       | CharFeild() |  –

#### ```Related User-Model```
| UserId        | User          | PlantId  |
| ------------- |:-------------:| -----:   |
| user.id       | user.username | plant.id |


#### ```Model-Plant```  
| Plant          | Type        | ID     |
| -------------  |:-----------:| -----: |
| Name           | CharFeild() |  –
| posted_on      | datetime()  |  –
| Region         | CharFeild() |  –
| Description    | CharFeild() |  –


#### ```Related Model```
| PlantId        | Plant       | UserId   |
|:: -----------  |::------------::| -----::  |
| plant.id       | plant.name  | user.id  |

```
#### ```REST–ROUTES-PlANT```  
| URL                | HTTP VERB  | ACTION  | Description       |
| ::-------------    |::---------:| -----:: | ----------------::|
|/plants             | GET        |  Index  | Show all plants   |
|/plants/new         | POST       |  New    | Add new plant     |
|/plants/:id/edit    | GET        |  Edit   | Plant for edit    |  
|/plants/:id         | PUT        |  Update | Plant to update   |
|/plants/:id/        | DELETE     |  Delete | Plant to delete   |

#### ```REST–ROUTES-USER```  
| URL                | HTTP VERB  | ACTION  | Description                 |
| ::-------------    |::---------:| -----:: | --------------------------::|
|/users/signup       | POST       |  Sign up form   | Sign up new user    |
|/users/login        | POST       |  Log in form    | Log in user         |
|/users/:id/plants   | GET        |  User's plants  | Show user's plants  |  
|/users/:id/plants   | PUT        |  Update         | Plant to update     |
|/users/plants/:id   | DELETE     |  Delete         | Plant to delete     |
|/users/:id          | DELETE     |  Delete         | Delete user profile |
```
#### Wireframes:
![alt text](https://i.imgur.com/cbD3bfX.jpg)
![alt text](https://i.imgur.com/2umptRu.jpg)
![alt text](https://i.imgur.com/iTNBWoj.jpg)

#### Technologies used:
**React** – Amazing JavaScript library that provides developers super powers of building complex websites easily! Front-end has been developed using ```REACT``` and designed with ```semantic-ui-react```

__Python-Flask__ – Very powerful python flask is the back bone of this website. Beck-end is built by using flask and ample flask's library.

**Sqlite** – Sqlite is structured query language database. All the data during the development phase will be saved in the Sqlite database.

**CORS** – Which stands for cross origin resource sharing, provides the ability to share data and routes from origins. Origin can be host, server and/or browser. CORS makes it possible to cross function the resources.

__Postgress sql__ – Data base is also structured query language database. All the data during and after deployement of this website will be stored in the psql database

#### Forthcoming features:
1. Give users ability to like the plants.
2. Give users ability to add comments on the post

#### Instruction on how to run the app:
1. This app is running with two different repositories. For the front-end is [React](https://github.com/Paresh10/plantery-react-full-crud) and for the beck-end is [Python Flask](https://github.com/Paresh10/plantery-flask-full-crud). For React clone this repo and run ```npm install``` in the terminal inside the cloned repo. This will install all the dependencies.

2. Assuming you have python3. Clone this repository and in your terminal (open separate terminal) navigate to the desired directory where you want clone this repository and run this command source .env/bin/activate. This will run virtual environment in your source directory. All the installation should be done in virtual environment. When you see .env at the beginning, before your cursor in the terminal then you can run this command ```pip3 install -r requirement.txt``` for ```python3```. Which will install all the dependencies from the requirement.txt file. Don't forget to freeze all the installed dependencies by running this command ```pip3 freeze > requirement.txt```.

3. Start the server at the python terminal by running ```python3 app.py```.

4. Start the react app by running ```npm start``` and violla!!
