# GoIT Database Management Project

The educational project implements a database schema designed to model a simplistic management system. It includes tables for groups, students, teachers, disciplines (courses), and grades. The project aims to practice database design, data insertion, and query execution to perform various data retrieval tasks.

## Database Schema Overview

The schema is structured into the following tables to accurately represent the educational model:

- **Groups Table:** Lists the available student groups.
- **Students Table:** Details student identities with first and last names.
- **Teachers Table:** Stores details of teachers.
- **Disciplines Table:** Lists disciplines along with the respective teacher for each discipline.
- **Grades Table:** Records the grades students receive in various disciplines, noting the award date.

## Data Generation Requirement

This project uses the `Faker` library to fill the database with fictitious but realistic-looking data. While the names and last names of students and teachers are randomly generated to add variety, the names of the groups and the disciplines are already set within the program and don't change. The setup includes 50 students spread out over 3 fixed groups, with 5 teachers, 8 predefined disciplines, and each student getting up to 20 grades across all these disciplines.

## Queries

Scripts are provided for executing various queries to retrieve information, such as:

- Identifying the top 5 students by average grade across all disciplines.
- Finding the student with the highest average grade in a specific discipline.
- Calculating average grades within groups for a specific discipline.
- Determining the overall average grade across all grades recorded.
- Listing disciplines taught by a specific teacher.
- Retrieving a list of students within a particular group.
- Finding grades of students in a specific group for a particular discipline.
- Calculating the average grade awarded by a specific teacher.
- Listing disciplines a student is enrolled in.
- Identifying disciplines taught to a specific student by a specific teacher.
- Calculating the average grade a teacher awards to a specific student.
- Finding grades awarded in the last class for a discipline within a specific group.

## Installation

    # Clone the repository
    git clone https://github.com/alex-nuclearboy/goit-python-web-hw6.git
    # Navigate to the cloned repository directory
    cd goit-python-web-hw6
    # Install the required Python packages
    pip install -r requirements.txt
    # Initialize and populate the Database:
    python main.py

## Usage

### Execute Queries from the Terminal

Use `run_sql_scripts.py` to automatically process and analyze the database, simplifying direct interaction and output assessment:

    python run_sql_scripts.py

### Compatibility with SQL Management Tools

The database and query scripts are compatible with various SQL management tools, such as DBeaver, allowing for easy import and execution of SQL scripts for analysis or practice.
