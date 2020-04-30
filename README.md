## Project # 3: Plantery```React```  & ```Flask```

##### About:
This is a flask file for plants api and currently this api is in use for this [React](https://github.com/Paresh10/plantery-react-full-crud) project here. To get the api and run it for your project see the Instruction below on how to run.


#### ```Model-User```

| User           | Type        | ID           |
| -------------  |:-----------:| :-----------:|
| Name           | CharFeild() | Primary_key  |
| Email          | CharFeild() | Primary_key  |
| Username       | CharFeild() | Primary_key  |
| Password       | CharFeild() | Primary_key  |


#### ```Model-Plant```  
| Plant          | Type        | ID              |
| -------------  |:-----------:| :--------------:|
| Name           | CharFeild() |  Primary_key    |
| posted_on      | datetime()  |  Primary_key    |
| Region         | CharFeild() |  Primary_key    |
| Description    | CharFeild() |  Primary_key    |
| Relation       | Foreign_key |  user.id        |


```
REST–ROUTES-PlANT
| URL                | HTTP VERB  | ACTION  | Description       |
| ::-------------    |::---------:| -----:: | ----------------::|
|/plants             | GET        |  Index  | Show all plants   |
|/plants             | POST       |  New    | Add new Plant     |
|/plants/:id         | PUT        |  Update | Plant to update   |
|/plants/:id/        | DELETE     |  Delete | Plant to delete   |

REST–ROUTES-USER  
| URL                | HTTP VERB  | ACTION  | Description                 |
| ::-------------    |::---------:| -----:: | --------------------------::|
|/users/signup       | POST       |  Sign up form   | Sign up new user    |
|/users/login        | POST       |  Log in form    | Log in user         |
|/users/:id/plants   | GET        |  User's plants  | Show user's plants  |  
|/users/:id          | DELETE     |  Delete         | Delete user profile |
```

#### Technologies used:
**React** – Amazing JavaScript library that provides developers super powers of building complex websites easily! Front-end has been developed using ```REACT``` and designed with ```semantic-ui-react```

__Python-Flask__ – Very powerful python flask is the back bone of this website. Beck-end is built by using flask and ample flask's library.

**Sqlite** – Sqlite is structured query language database. All the data during the development phase will be saved in the Sqlite database.

**CORS** – Which stands for cross origin resource sharing, provides the ability to share data and routes from origins. Origin can be host, server and/or browser. CORS makes it possible to cross function the resources.

__Postgress sql__ – Data base is also structured query language database. All the data during and after deployement of this website will be stored in the psql database

#### Forthcoming features:
1. Give users ability to like the plants.
2. Give users ability to add comments on the post
3. Give users ability to see other user's plants

#### Instruction on how to run the app:
1. Assuming you have python3. Clone this repository and in your terminal (open separate terminal) navigate to the desired directory where you want clone this repository and run this command ```virtualenv .env -p python3```. Which will create a virtual environment for your file to be run and installed in the .env. To activate it run ```source .env/bin/activate```. This will run virtual environment in your source directory. All the installation should be done in virtual environment. When you see .env at the beginning, before your cursor in the terminal then you can run this command ```pip3 install -r requirement.txt``` for ```python3```. Which will install all the dependencies from the requirement.txt file. Don't forget to freeze all the installed dependencies by running this command ```pip3 freeze > requirement.txt```.

2. Start the server at the python terminal by running ```python3 app.py```and violla!.
