# Back-End-Capstone

## Description of the project

This is the final project for Back-End Developer Capstone course (Meta Back-End Developer Professional Certificate) to build an API for the Little Lemon restaurant.

Main tasks for the project:

- Connect the Little Lemon restaurant back-end to MySQL
- Set up a Little Lemon restaurant booking API
- Insert booking data in the database via the booking API

---

## API URL

Localhost base URL is http://127.0.0.1:8000

---

## Getting Started

### Installation and Database Setup

#### Virtual Environment

It is recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [venv docs](https://docs.python.org/3/library/venv.html).

Create the virtual environment for the project directory

```bash
python3 -m venv <name>
```

Activate the virtual environment:

```bash
source <name>/bin/activate
```

Deactivate the virtual environment:

```bash
deactivate
```

Delete the virtual environment:

```bash
rm -r <name>
```

#### Installing Python Dependencies

Once the virtual environment is setup and running, install the required dependencies by navigating to the project directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages in the `requirements.txt` file.

---

## Database Setup

The project uses **MySQL** database.

Change settings (USER and PASSWORD) in littlelemon/settings.py, you should use your credentials.

DATABASES = {
"default": {
...
"USER" : "admindjango",
"PASSWORD" : "employee@123!",
...
}

Generate database tables from the models:

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

## Running the Server

Switch to the project directory and ensure that the virtual environment is running.

```bash
python3 manage.py runserver
```

---

## Testing

Run tests:

```bash
python3 manage.py test
```

In `notes.txt` you can find credentials for admin and customer.

You can use [Insomnia](https://insomnia.rest/) to test endpoints. In order for them to work properly, update the Bearer Tokens in each collection with tokens generated from the website. See the `notes.txt`.

---

## API

In order to use the API, users need to be authenticated. JWT tokens can be generated by logging in with the provided credentials (username and password) on the hosted site.

POST http://127.0.0.1:8000/auth/token/login/

### Endpoints

- Note: any `curl` commands used must include an authorization header as all endpoints require authorization to use:  
  `curl -H "Authorization: Bearer <JWT_ACCESS_TOKEN>"`
- For post and patch you need you need also add Content-Type:
  `curl -H "Authorization: Bearer <JWT_ACCESS_TOKEN>" -H "Content-Type: application/json" -d "{data}"`

#### User registration and token generation endpoints

| Endpoint                   | Role                                      | Method     | Purpose                                                                     |
| -------------------------- | ----------------------------------------- | ---------- | --------------------------------------------------------------------------- |
| /restaurant/users          | Admin                                     | GET        | Returns all users                                                           |
| /restaurant/users          | Admin                                     | POST       | Creates a new user                                                          |
| /restaurant/users/{userId} | Admin                                     | DELETE     | Delete user                                                                 |
| /restaurant/users/{userId} | Admin                                     | PUT, PATCH | Update the user                                                             |
| /auth/users                | No role required                          | POST       | Creates a new user with name, email and password                            |
| /auth/users/me/            | Anyone with a valid user token            | GET        | Displays the current user                                                   |
| /auth/users/me/            | Anyone with a valid user token            | PUT, PATCH | Update the current user                                                     |
| /auth/users/me/            | Anyone with a valid user token            | DELETE     | Delete the current user                                                     |
| /auth/token/login/         | Anyone with a valid username and password | POST       | Generates access tokens that can be used in other API calls in this project |
| /auth/token/logout/        | Anyone with a valid username and password | POST       | Logout the user (remove user authentication token)                          |

#### Menu-items endpoints

- Fetches a dictionary of dictionaries for each menu-items from the database.
- Request Arguments for GET and DELETE: None.
- Request Arguments for POST, UPDATE, PATCH: title, price, inventory.

| Endpoint                          | Role        | Method                   | Purpose                    |
| --------------------------------- | ----------- | ------------------------ | -------------------------- |
| /restaurant/menu                  | Not Manager | GET                      | Returns all menu-items     |
| /restaurant/menu-items            | Not Manager | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized |
| /restaurant/menu-items/{menuItem} | Not Manager | GET                      | Returns the menu-item      |
| /restaurant/menu-items/{menuItem} | Not Manager | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized |
| /restaurant/menu-items            | Manager     | GET                      | Returns all menu-items     |
| /restaurant/menu-items            | Manager     | POST                     | Creates a new menu-item    |
| /restaurant/menu-items/{menuItem} | Manager     | GET                      | Returns the menu-item item |
| /restaurant/menu-items/{menuItem} | Manager     | PUT, PATCH               | Updates the menu-item item |
| /restaurant/menu-items/{menuItem} | Manager     | DELETE                   | Deletes the menu-item item |

#### Bookings endpoints

- Fetches a dictionary of dictionaries for each booking from the database.
- Request Arguments for GET and DELETE: None.
- Request Arguments for POST, UPDATE, PATCH: name, no_of_guests, booking_date.

| Endpoint                         | Role        | Method     | Purpose                     |
| -------------------------------- | ----------- | ---------- | --------------------------- |
| /restaurant/bookings             | Not Manager | GET        | Returns all bookings user   |
| /restaurant/bookings             | Not Manager | POST       | Creates a new booking       |
| /restaurant/bookings/{bookingId} | Not Manager | GET        | Returns the current booking |
| /restaurant/bookings/{bookingId} | Not Manager | PUT, PATCH | Returns 403 - Unauthorized  |
| /restaurant/bookings/{bookingId} | Not Manager | DELETE     | Returns 403 - Unauthorized  |
| /restaurant/bookings             | Manager     | GET        | Returns all bookings        |
| /restaurant/bookings             | Manager     | POST       | Creates a new booking       |
| /restaurant/bookings/{bookingId} | Manager     | PUT, PATCH | Updates the booking         |
| /restaurant/bookings/{bookingId} | Manager     | DELETE     | Deletes the booking         |

#### Home endpoints

http://127.0.0.1:8000/restaurant/home/

