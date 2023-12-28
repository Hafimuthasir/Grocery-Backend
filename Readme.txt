This README provides instructions on how to set up and run the project locally.

## Table of Contents
1. [Requirements]
2. [Installation]
3. [Running the Project]
4. [Message]


## Requirements

- Python 3.x
- Django==5.0
- django-cors-headers==4.3.1
- djangorestframework==3.14.0

## Installation

1. Clone the repository: `git clone [repository_url]`
2. Navigate to the project directory: `cd [project_directory]`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`


## Running the Project

1. If the virtual environment is not already activated, activate it:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
2. Run migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`

The project will be accessible at [http://localhost:8000/] 


## Message

Created endpoints as per the specifications. Despite having some custom solutions for robust authentication system and CRUD operations , it hasn't been included in this due to it is not being explicitly mentioned for the implementation. Furthermore, integrated pagination and a basic caching mechanism based on pagination. If there are any concerns or issues with the code, please feel free to reach out. There might be reasons behind certain choices, and I'm open to addressing any questions you may have.


