# KartPool

![coverage](readme_img/cover.png)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

KartPool is a community-driven delivery app and platform for connecting residents with local businesses. It aims to address the challenges posed by the COVID-19 pandemic by providing a safe and efficient way for people to shop for essentials and support local businesses.

![Screenshot](readme_img/screenshot1.gif)
![Screenshot](readme_img/screenshot2.gif)



## Installation

clone the repo:
```sh
$ git clone https://github.com/Ahmed3atef/Kartpool.git
```

- Install PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib
```
This will install PostgreSQL and some additional utilities.
-    Install PostGIS
```bash
sudo apt install postgis postgresql-<version>-postgis-<version>
```
Replace <version> with the version of PostgreSQL you have installed. For example, if you’re using PostgreSQL 14, you would use postgresql-14-postgis-3.
-   Verify Installation
```bash
psql --version
```
#### Create a New Database and Enable PostGIS
-   Switch to the PostgreSQL User:
```bash
sudo -i -u postgres
```
-   Start the PostgreSQL Interactive Terminal:
```bash
psql
```
-   Create a New Database (replace your_database_name with your desired name):
```sql
CREATE DATABASE your_database_name;
```
-   Connect to the Database:
```sql
\c your_database_name
```
-   Enable PostGIS Extension:
```sql
CREATE EXTENSION postgis;
```
-   You can also enable additional extensions if needed:
```sql
CREATE EXTENSION postgis_topology;
```

On macOS and Linux:

```sh
$ sudo ./reset_kartpool_db.sh
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
```
## Execution / Usage

To run KartPool, fire up a terminal window and run the following command:

eddit this lines in kartpool/settings.py
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # making django work with PostGIS
        'NAME': 'kartpool',
        'USER': 'change me',
        'PASSWORD': 'change me',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =  587
EMAIL_HOST_USER = "your user"
EMAIL_HOST_PASSWORD = "your password"
EMAIL_USE_TLS = True
```

```sh
$ source env/bin/activate
$ python manage.py runserver
```

## Technologies

KartPool uses the following technologies and tools:

-   **Python 3**: Programming language.
-   **Django**: Web framework for developing the application.
-   **GeoDjango**: Django module for geographic web applications.
-   **PostgreSQL**: Database for data storage.
-   **PostGIS**: Extension for PostgreSQL to handle spatial data
## Features

KartPool currently has the following set of features:

1. **Store Locator**: Users can view stores in their vicinity and check their inventory.
2. **Wishlist Creation**: Users can create wishlists of essential items they need to purchase.
3. **Community Delivery**: Other users (wishmasters) can accept requests and deliver items to requestors.
4. **Karma Points**: A recognition system to appreciate helpful community members.

## Why KartPool?

- Promotes community engagement and mutual support
- Reduces exposure risk by minimizing trips to stores
- Supports local businesses during challenging times
- Provides a digital infrastructure for businesses lacking online presence

## Contributing

To contribute to the development of KartPool, follow the steps below:

1. Fork KartPool from <https://github.com/Ahmed3atef/Kartpool.git>
2. Create your feature branch (`git checkout -b feature-new`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some new feature'`)
5. Push to the branch (`git push origin feature-new`)
6. Create a new pull request

## License

KartPool is distributed under the MIT license. See [`LICENSE`](LICENSE.md) for more details.
