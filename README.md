# My Book Tracking Application 📚

This repository contains the codebase for a Django-based web application I developed to facilitate the management and tracking of personal book collections. The application offers a range of functionalities designed to enhance the user's interaction with their reading habits.

## Core Functionalities ✨

* **User Authentication:** The system incorporates secure user registration, login, and logout mechanisms, allowing individuals to manage their personal book data privately. 🚪
* **Book Record Management:** Authenticated users can perform comprehensive operations on their book records, including:
    * **Viewing:** Displaying a complete list of all recorded books. 👀
    * **Creation:** Adding new book entries with details such as title, author, rating, total page count, current page number, and assigned category. ✍️
    * **Modification:** Editing existing book records to update any of the aforementioned details. ✏️
    * **Deletion:** Removing unwanted book records from their collection. 🗑️
* **Reading Progress Indication:** The application automatically determines and displays the completion status of a book based on the comparison between the current page and the total page count. 💯
* **Search Capability:** Users can efficiently search their book inventory by either the title of the book or the name of the author. 🔍
* **Categorization and Filtering:** Books can be categorized by the user, enabling the filtering and display of books belonging to specific genres or classifications. 
* **Personalized User Profile:** Each user has a dedicated profile page providing an overview of their entire book collection, including separate listings for books currently being read and those that have been completed. 🤓
* **Account Modification:** Users possess the ability to update their account credentials, specifically their username and password, through the profile settings. 😉
* **Detailed Book Information:** A dedicated view is available for each book record, presenting a comprehensive overview of its attributes. 📖

## Technical Implementation 🛠️

* The application is built using the Django web framework (utilizing Python). 🐍
* Python serves as the primary programming language for the backend logic and application development. 😉

## Setup Procedure (General Outline) 🏃

While specific setup instructions are beyond the scope of the provided code snippet, a typical deployment of this Django application would involve:

1.  Ensuring the presence of a Python interpreter on the target system.
2.  Installing the Django framework using the pip package manager (`pip install Django`).
3.  Executing database migrations to establish the necessary database schema (`python manage.py migrate`).
4.  Creating an administrative user account for system management (`python manage.py createsuperuser`).
5.  Launching the Django development server to host the application (`python manage.py runserver`).

## Usage Guidelines 🚀

1.  Initiate the process by registering a new user account via the signup page.
2.  Access the application by logging in with the created credentials on the login page.
3.  Upon successful authentication, users can add new book records, view their existing collection, perform searches, modify book details, and remove entries as needed.
4.  The user profile section provides a summary of reading activity and allows for the editing of account information.
5.  Navigating through category links enables the filtering and display of books within selected categories.

## Codebase Structure (View Functions) ⚙️

The application's view logic is organized into the following functions:

* `sign_up`: Manages the user registration process.
* `login_view`: Handles user authentication and login.
* `logout_view`: Facilitates user logout. 👋
* `all_books`: Displays the user's book collection and processes search queries.
* `add_book`: Implements the functionality for adding new book records.
* `edit_book`: Enables the modification of existing book records.
* `delete_book`: Provides the ability to remove book records.
* `category_search`: Filters and displays books based on their assigned category.
* `user_profile`: Presents the user's profile information and reading statistics.
* `edit_profile`: Handles the modification of user account details.
* `book_details`: Displays detailed information for a specific book record.
