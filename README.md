# Slate

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-wiki">Project Wiki</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#sample-features">Sample Features</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![slate](https://user-images.githubusercontent.com/105696861/200223816-6747bd49-24f9-4dd9-a563-e13a102ff674.png)


[Slate](https://slate-canva.herokuapp.com/) is a web application inspired by Canva, allowing users to have an easy way to create designs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Project Wiki
* [User Stories](https://github.com/amanduhkv/slate/wiki/User-Stories)
* [Database Schema and Backend Routes](https://github.com/amanduhkv/slate/wiki/Database-Schema-and-Backend-Routes)
* [Features List](https://github.com/amanduhkv/slate/wiki/Features-List)
* [Redux State Shape](https://github.com/amanduhkv/slate/wiki/Redux-Store-State)
* [Wireframes](https://github.com/amanduhkv/slate/wiki/Wireframes)



### Built With
#### Frameworks, Platforms, & Libraries:
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)

#### Database:
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

#### Database:
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SAMPLE FEATURES -->
## Sample Features
### Log in or sign up
![login](https://user-images.githubusercontent.com/105696861/200228063-cd57e7cc-f7e2-432d-a82a-4fd50fbf9ce4.png)
### Design Page
![despage](https://user-images.githubusercontent.com/105696861/200228161-cafef450-e27b-422f-8c99-be6b0c280c19.png)
### Create a Design
![create-des](https://user-images.githubusercontent.com/105696861/200228206-307825f0-5325-460f-9db3-384fcb9fac46.png)
### Brand Page
![brand-page](https://user-images.githubusercontent.com/105696861/200228242-f548c96c-d363-410f-abcc-ebdbf3228a00.png)




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

1. Clone the repo:

    SSH version:
    ```sh
    git clone git@github.com:amanduhkv/slate.git
    ```
    or

    HTTPS version:
    ```sh
    git clone https://github.com/amanduhkv/slate.git
    ```

2. Install packages
    ```sh
    pipenv install
    cd react-app
    npm install
    ```
3. Create a .env file and set the environment variables for SECRET_KEY and DATABASE_URL to your choosing.

4. Migrate and seed the files.
    ```sh
    flask run db init
    flask run migrate
    flask seed all
    ```
5. Run the server and start the react app
    ```sh
    pipenv run flask run
    cd react-app
    npm start
    ```

<!-- ROADMAP -->
## Roadmap

- [x] Designs
    - [x] Create a design
    - [x] Load all designs
    - [x] Load current user's designs
    - [x] Update a current user's design
    - [x] Delete a current user's design
- [x] Brands
    - [x] Create a brand
    - [x] Load all brands
    - [x] Load all user's brands
    - [x] Update a current user's brand
    - [x] Delete a current user's brand
    
- [ ] Images / Shapes
    - [ ] Create a design image or shape
    - [ ] Edit a design image or shape
    - [ ] Delete a design image or shape
   
- [ ] Search / Filter
    - [ ] Create a search filter
    - [ ] See the result of a search filter
    - [ ] Update a search filter
    - [ ] Remove a search filter


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->

Amanda Vien:
<br>
[![linked in][linkedin-icon]][linkedin-url-amanda]
[![linked in][github-icon]][github-url-amanda]
<br>


Project Link: [https://github.com/amanduhkv/slate](https://github.com/amanduhkv/slate)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-icon]: https://skillicons.dev/icons?i=linkedin
[github-icon]: https://skillicons.dev/icons?i=github
[linkedin-url-amanda]: https://www.linkedin.com/in/amandakvien/
[github-url-amanda]: https://github.com/amanduhkv
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
