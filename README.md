# GLIM

## Project goals
This project provides a Django Rest Framework API for the [GLIM React web app](https://glim-9f608ab3b04d.herokuapp.com/).

Glim is designed to be a ticket booking web site for a small (family type) cinema theatre, it should:

1. Provide an easy way to check what are the movies currently in theatre, read other users reviews and post your own review check popularity of each movie and book your ticket.
2. Deliver a simple and intuitive user experience, suitable for everyone.
3. Offer a minimal set of impactful features chosen in order to deliver a useful app within an achievable development timeframe, while laying a solid foundation for additional features in the future.

## Table of contents
- [GLIM](#GLIM)
  * [Project goals](#project-goals)
  * [Table of contents](#table-of-contents)
  * [Planning](#planning)
    + [Data models](#data-models)
      - [**Profile**](#profile)
      - [**Movies**](#movies)
      - [**Likes**](#likes)
      - [**Comments**](#comments)
      -  [**Tickets**](#tickets)
  * [Frameworks, libraries and dependencies](#frameworks-libraries-and-dependencies)
    + [django-cloudinary-storage](#django-cloudinary-storage)
    + [dj-allauth](#dj-allauth)
    + [dj-rest-auth](#dj-rest-auth)
    + [djangorestframework-simplejwt](#djangorestframework-simplejwt)
    + [dj-database-url](#dj-database-url)
    + [psychopg2](#psychopg2)
    + [django-filter](#django-filter)
    + [django-cors-headers](#django-cors-headers)
  * [Testing](#testing)
    + [Manual testing](#manual-testing)
    + [Python validation](#python-validation)
    + [Resolved bugs](#resolved-bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)

## Planning
Planning started by creating epics and user stories for the frontend application, based on the project goals. The user stories were used to inform wireframes mapping out the intended functionality and 'flow' through the app. See the [GLIM React web app repository ](https://github.com/AhmadAlmasriDev/glim) for more details.

The user stories requiring implementation to achieve a minimum viable product (MVP) were then mapped to API endpoints required to support the desired functionality.

<details close>
  <summary>API endpoints</summary >

  ![API endpoints](documentation/API_end_points.jpg)

</details>
<br>

### Data models
Data model schema were planned in parallel with the API endpoints, using an entity relationship diagram.

<details close>
  <summary>Data diagram</summary >

  ![Data diagram](documentation/data_diagram.jpg)

</details>
<br>

Custom models implemented for GLIM are:

#### **Profile**
Represents the user profile, using a one-to-one relationship to the user model. A Profile instance is automatically created on user registration. The Profile model includes an `is_admin` Boolean field, which is used to determine whether a given user has admin privileges. Note that initial user registration creates a profile with user rights (regular user). The admin can give the staff rights (manager) through the admin panel.

Users can edit their own `name`, `email` and `avatar` fields.

The model can be checked here: [Profiles](https://github.com/AhmadAlmasriDev/glim-api/tree/main/profiles)

#### **Movies**
The movies model represents the movie, it has a lot of fields, mostly are information about each movie, there are some additional fields that where added in the serializer to add more functionality to the model, like the `is_admin`, `like_id`, `likes_count`, and `comments_count` fields. And a separate serializer that returns service data like the `ratings` or other information that can be added later to the model.

Managers can add, edit or delete a `movie` and is given by the permissions IsAdminUser and ReadOnly

The model can be checked here: [Movies](https://github.com/AhmadAlmasriDev/glim-api/tree/main/movies)

#### **Likes**
The Likes model represents the user's like, it has the `movie` (foreign Key) which relates to the movie id, and `owner` (foreign Key) which relates to the user id.

The model can be checked here: [Likes](https://github.com/AhmadAlmasriDev/glim-api/tree/main/likes)

#### **Comments**
The Comments model represents the comment, it has a `movie` (foreign key) that relates to the commented movie's id, `owner` (foreign key) that relates to the comment owner's id, `owner_name` serves as a slug field used to keep the comment after the owner of the comment was deleted, `comment_body` is for the comment body, and `approved` field that is used to create drafts and approve later. a couple of fields are added by the serializer like, the `profile_id and the `profile_avatar`.

The model can be checked here: [Comments](https://github.com/AhmadAlmasriDev/glim-api/tree/main/comments)

#### **Tickets**
The Tickets model represents tickets. And is the one that most important to the website functionalities. It has a `movie` (foreign key) that relates to the commented movie's id, `owner` (foreign key) that relates to the comment owner's id, `seat` that holds the seat number, and validated to be 1-84, `show_date` that hold the show date for the movie, `reserve` a Boolean for temporary booking the seat when the user clicks on it, and a `purchased` field, a Boolean for permanently booking the seat, when the user clicks the reserve button. A couple of fields were added by the serializer like, `is_owner`, `price` taken from the movie, and the `expired` field, which is by default is false till three minutes have passed since the initial reserve (clicking on the seat) after that it returns true. This field combined with the custom permission `IsOwnerOrReadOnlyOrExpired` give the application the functionality to delete expired tickets.

The model can be checked here: [Tickets](https://github.com/AhmadAlmasriDev/glim-api/tree/main/tickets)


## Frameworks, libraries and dependencies
The GLIM API is implemented in Python using [Django](https://www.djangoproject.com) and [Django Rest Framework](https://django-filter.readthedocs.io/en/stable/).

The following additional utilities, apps and modules were also used.

### django-cloudinary-storage
https://pypi.org/project/django-cloudinary-storage/

Enables cloudinary integration for storing user profile images in cloudinary.

### dj-allauth
https://django-allauth.readthedocs.io/en/latest/

Used for user authentication. While not currently utilised, this package enables registration and authentication using a range of social media accounts. This may be implemented in a future update.

### dj-rest-auth
https://dj-rest-auth.readthedocs.io/en/latest/introduction.html

Provides REST API endpoints for login and logout. The user registration endpoints provided by dj-rest-auth are not utilised by the Tribehub frontend, as custom functionality was required and implemented by the Tribehub API.

### djangorestframework-simplejwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

Provides JSON web token authentication.

### dj-database-url
https://pypi.org/project/dj-database-url/

Creates an environment variable to configure the connection to the database.

### psychopg2
https://pypi.org/project/psycopg2/

Database adapater to enable interaction between Python and the PostgreSQL database.

### django-filter
https://django-filter.readthedocs.io/en/stable/

django-filter is used to implement ISO datetime filtering functionality for the `events` GET endpoint. The client is able to request dates within a range using the `from_date` and `to_date` URL parameters. The API performs an additional check after filtering to 'catch' any repeat events within the requested range, where the original event stored in the database occurred beforehand.

### django-cors-headers
https://pypi.org/project/django-cors-headers/

This Django app adds Cross-Origin-Resource Sharing (CORS) headers to responses, to enable the API to respond to requests from origins other than its own host.
GLIM is configured to allow requests from all origins, to facilitate future development of a native movile app using this API.

## Testing

### Manual testing

A series of manual tests were carried out for each end point using the Django Rest Framework HTML interface running on the local server and using the deployed database.

| Operation | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **/profiles/** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns profiles list  | GET request | Endpoint returned profiles list | Pass|
| GET | Authorized user Get request to endpoint returns profiles list  | GET request | Endpoint returned profiles list | Pass|
| **/profiles/id** |  |  |  |  |
|  |  |  |  |  |
| GET | Authorized user (not owner) Get request to endpoint returns profile details  | GET request | Endpoint returned profile details | Pass|
| GET | Authorized user (owner) Get request to endpoint returns profile details  | GET request | Endpoint returned profile details | Pass|
| PUT | Authorized user (owner) PUT request to endpoint updates profile details  | PUT request (all data) | profile details updated | Pass|
| PUT | Authorized user (owner) PUT request to endpoint returns 400 error  | PUT request (name field empty) | returned 400 error | Pass|
| **/movies/** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns profiles list  | GET request | Endpoint returned profiles list | Pass|
| POST | Admin user POST request to endpoint creates a movie  | POST request (all data) | Movie was created | Pass|
| POST | Admin user POST request to endpoint returns 400 error  | POST request (empty title or price or poster field) | Returned 400 error | Pass|
| **/movies/id** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns movie details  | GET request | Endpoint returned movie details | Pass|
| PUT | Admin user PUT request to endpoint updates movie details  | PUT request (all data) | movie details updated | Pass|
| PUT | Admin user PUT request to endpoint returns 400 error  | PUT request (empty title or price field) | returned 400 error | Pass|
| DELETE | Admin user DELETE request to deletes the movie | DELETE request  | The movie was deleted | Pass|
| **/movies/service** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns service details  | GET request | Endpoint returned service details | Pass|
| **/likes/** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns likes list  | GET request | Endpoint returned likes list | Pass|
| POST | Authorized user POST request to endpoint creates a like  | POST (all data) | Like was created | Pass|
| **/likes/id** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns like details  | GET request | Endpoint returned like details | Pass|
| DELETE | Authorized (owner) user DELETE request to endpoint deletes the like | DELETE request | Like is deleted | Pass|
| **/tickets/** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns tickets list  | GET request | Endpoint returned tickets list | Pass|
| POST | Authorized user POST request to endpoint creates a ticket  | POST request (all data) | ticket was created | Pass|
| POST | Authorized user POST request to endpoint returns 400 error  | POST request (empty seat and date field) | returned 400 error | Pass|
| **/tickets/id** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns ticket details  | GET request | Endpoint returned ticket details | Pass|
| PUT| Authorized user (owner and ticket not expired) PUT request to endpoint updates ticket details  | PUT request (all data)| Ticket details updated | Pass|
| PUT| Authorized user (owner and ticket not expired) PUT request to endpoint returns 400 error  | PUT request (empty seat or date field)| Returned 400 error | Pass|
| DELETE | Authorized user (owner and ticket not expired) DELETE request to endpoint deletes the ticket  | DELETE request | The ticket was deleted | Pass|
| DELETE | Unauthorized user (ticket expired) DELETE request to endpoint deletes the ticket  | DELETE request | The ticket was deleted | Pass|
| **/comments/** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns comments list  | GET request | Endpoint returned comments list | Pass|
| POST | Authorized user POST request to endpoint creates a comment  | POST (all data) | Comment was created | Pass|
| POST | Authorized user POST request to endpoint returns 400 error  | POST request (empty comment body field) | returned 400 error | Pass|
| **/comments/id** |  |  |  |  |
|  |  |  |  |  |
| GET | Unauthorized user Get request to endpoint returns comment detail | GET request | Endpoint returned comment detail | Pass|
| DELETE | Authorized user (owner) DELETE request to endpoint deletes the comment | DELETE request | The tcomment was deleted | Pass|
<br>

Testing on the frontend revealed a number of bugs which had not been detected while testing the API in isolation, and led to the implementation of several additional features for consumption by the React app. The bugs are detailed in the bugs section below, and the following additional features were added as a result of front-end testing:

- Sign-up was throwing a 400 error, it was due to syntax error, an extra slash in the url.  
- Movie rating was sent as an integer, to work around this issue a serializer for service date was created and it will send an array with the ratings that are used.
- One of the most difficult tasks was deleting expired tickets. For this reason the `reserved` and `purchased` Boolean fields were added, and since the user can't delete other users tickets a special permission was created to give any user the right to delete any ticket if expired.  
- The user avatar was not displayed because the field name on the backend was different instead of `user_avatar` it was `user_image`.
- There was an unwanted PUT operation in the comments views and in the likes view, although it is not giving any errors but in case there is a PUT operation it eill give an error.

### Python validation

Code errors and style issues were detected using black linter in GitPod, and immediately fixed throughout development.
All files containing custom Python code were then validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/):

- Glim

    <details close>
    <summary>Permissions</summary >

    ![Permissions](documentation/ips_glim_api_permissions.jpg)

    </details>
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_glim_api_serializers.jpg)

    </details>
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_glim_api-urls.jpg)

    </details>
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_glim_api-views.jpg)

    </details>
    <details close>
    <summary>Settings</summary >

    ![Settings](documentation/ips_glim_api_settings.jpg)

    </details>
    <details close>
    <summary>Pagination</summary >

    ![Pagination](documentation/ips_glim_api-pagination.jpg)

    </details>
    <br>
- Comments

    <details close>
    <summary>Models</summary >

    ![Models](documentation/ips_comments_models.jpg)

    </details>
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_comments_serializers.jpg)

    </details>
    
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_comments_urls.jpg)

    </details>
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_comments_views.jpg)

    </details>
    <br>
- Likes

    <details close>
    <summary>Models</summary >

    ![Models](documentation/ips_likes_models.jpg)

    </details>
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_likes_serializers.jpg)

    </details>
    
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_likes_urls.jpg)

    </details>
    
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_likes_views.jpg)

    </details>
    <br>
- Movies

    <details close>
    <summary>Models</summary >

    ![Models](documentation/ips_movies_models.jpg)

    </details>
    
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_movies_serializers.jpg)

    </details>
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_movies_urls.jpg)

    </details>
    
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_movies_views.jpg)

    </details>
    <br>
- Profiles
    
    <details close>
    <summary>Models</summary >

    ![Models](documentation/ips_profiles_models.jpg)

    </details>
    
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_profiles_serializers.jpg)

    </details>
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_profiles_urls.jpg)

    </details>
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_profiles_views.jpg)

    </details>
    <br>
- Tickets

    <details close>
    <summary>Models</summary >

    ![Models](documentation/ips_tickets_models.jpg)

    </details>
    <details close>
    <summary>Serializes</summary >

    ![Serializes](documentation/ips_tickets_serializers.jpg)

    </details>
    <details close>
    <summary>Urls</summary >

    ![Urls](documentation/ips_tickets_urls.jpg)

    </details>
    <details close>
    <summary>Views</summary >

    ![Views](documentation/ips_tickets_views.jpg)

    </details>
    

### Resolved bugs


- When a user is deleted by the admin, all tickets and comments are deleted. The comments of deleted user should not be deleted unlike the tickets which are directly related to the deleted user only, but comments are viewed by other users. So in in order to leave the comments a service account was created and all the deleted users comments become related to this account only the name of the original user stays. 
- in the Moments walkthrough the dates were formatted, and I used this same pattern in this project, but after working with the frontend a couple of issues  resurfaced. In the project some of the functionality was depending heavily on comparing date and was difficult to achieve. So I used a library called moment-react to compare the date on the front end.      
- when the user tries to access a comment detail the API returns an error. One of the fields source was the same as the field name it self (owner) and it was changed to (owner.id).

## Deployment
The GLIM API is deployed to Heroku, using an ElephantSQL Postgres database.
To duplicate deployment to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user profile images.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Login to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Name the 'plan' and select the 'Tiny Turtle (free)' plan.
- Select 'select region'.
- Choose the nearest data centre to your location.
- Click 'Review'.
- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
- Copy the ElephantSQL database URL to your clipboard (this starts with `postgres://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your ElephantSQL postgres database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
    - `ALLOWED_HOST`: *the url of your Heroku app (but without the `https://` prefix)*
- Select the 'Deploy' tab at the top.
- Select 'GitHub' from the deployment options and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed API to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your API will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits
- The technique resize the image on demand was adapted from this article [Cloudinary](https://cloudinary.com/guides/image-effects/how-to-resize-an-image-with-react).

- How to create a custom permission was adapted from Rest Framework documentation [Rest Framwork](https://www.django-rest-framework.org/)

- A lot of information was adapted from these tutorials:
  - [Django Rest Framework](https://www.youtube.com/watch?v=soxd_xdHR0o&list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw&ab_channel=VeryAcademy)
  - [Build an API from Scratch](https://www.youtube.com/watch?v=i5JykvxUk_A&ab_channel=CalebCurry) 

- Most of the solution to various problems were taken from [Stackoverflow](https://stackoverflow.com) and the [django documentation](https://docs.djangoproject.com/en/5.0/)

In addition, the following documentation was extensively referenced throughout development:

- [Django documentation](https://www.djangoproject.com)
- [Django Rest Framework documentation](https://www.django-rest-framework.org)
- [django-filter documentation](https://django-filter.readthedocs.io/en/stable/)

