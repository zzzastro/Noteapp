# Noteapp

A modern, feature-rich note-taking application built with Django and Tailwind CSS.

## Features

- **Note Management**
  - Create, edit, and delete notes  
  - Rich text content support  
  - Automatic timestamps for creation and updates  
  - Quick copy functionality

- **Category System**
  - Organize notes by categories  
  - Create and manage custom categories  
  - Filter notes by category

- **Search Functionality**
  - Full-text search across notes  
  - Search by title and content  
  - Real-time filtering

- **User Interface**
  - Clean, modern design with Tailwind CSS  
  - Responsive layout for all devices  
  - Toast notifications for user actions  
  - Intuitive navigation

## Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/zzzastro/noteapp.git](https://github.com/zzzastro/noteapp.git)
    cd noteapp
    ```

2.  **Create and activate virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Node.js dependencies and build CSS**
    ```bash
    cd theme/static_src
    npm install
    npm run build
    ```

5.  **Run migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Start the development server**
    ```bash
    python manage.py runserver
    ```


## Technologies Used

- Django 5.1.3
- Tailwind CSS 3.4.0
- Python 3.12
- SQLite3
