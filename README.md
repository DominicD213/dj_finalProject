# dj_finalProject
Sure! Here’s the complete README.md script for your project, written in Markdown format:

markdown
Copy code
# Weather App

A Django-based weather application that allows users to search for current weather data of cities worldwide. It provides the temperature, humidity, and other weather-related data fetched from an external weather API. The application features user authentication and management, as well as an admin interface for managing the weather data and user details.

---

## Features

- **User Authentication**: Custom user model for registration, login, and profile management.
- **Weather Forecast**: Displays weather details such as temperature, humidity, and weather conditions for a city.
- **Admin Panel**: Customizable Django admin panel to manage weather data, users, and settings.
- **Background Tasks**: Uses Celery to perform asynchronous background tasks (e.g., updating weather data).
- **Responsive Design**: Mobile-friendly design using Bootstrap.

---

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [Technologies](#technologies)
- [License](#license)

---

## Installation

### 1. Clone the repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/DominicD213/dj_finalProject.git
cd dj_finalProject
2. Create and activate a virtual environment
For macOS/Linux:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
For Windows:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
Install all the required packages listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Set up the database
Run migrations to set up the database:

bash
Copy code
python manage.py migrate
5. Create a superuser
Create a superuser to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser.

6. Run the development server
Start the server to run the application locally:

bash
Copy code
python manage.py runserver
The app will be available at http://127.0.0.1:8000/.