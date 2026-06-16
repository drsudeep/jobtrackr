# JobTrackr – Job Application Tracking System

A full-stack web application built with Django that helps users manage, organize, and track their job applications in one place. Users can register, log in, add applications, update application status, monitor progress through an analytics dashboard, and export records to CSV.

---

## Features

### User Authentication

- User Registration
- Secure Login & Logout
- Session-Based Authentication
- User-Specific Application Data
- Protected Routes Using Django Login Required

### Job Application Management

- Add New Applications
- Edit Existing Applications
- Delete Applications
- Track Application Progress
- Store Company, Role, Location, Date, Status, and Notes

### Application Tracking

- Applied
- Interview
- Offer
- Rejected

### Dashboard Analytics

- Total Applications Count
- Applied Applications Count
- Interview Applications Count
- Offer Applications Count
- Rejected Applications Count
- Recent Applications Overview

### Search & Filtering

- Search Applications by Company Name
- Filter Applications by Status
- Dynamic QuerySet Filtering

### CSV Export

- Export All Applications
- Download Records as CSV File
- Easy Reporting and Data Backup

---

# Application Screenshots

## 1️⃣ Homepage

Landing page introducing the JobTrackr platform.

![](https://github.com/drsudeep/jobtrackr/blob/main/Homepage.png?raw=true)

---

## 2️⃣ User Registration

New users can create an account.

![](https://github.com/drsudeep/jobtrackr/blob/main/register.png?raw=true)

---

## 3️⃣ User Login

Secure login interface for existing users.

![](https://github.com/drsudeep/jobtrackr/blob/main/login.png?raw=true)

---

## 4️⃣ Dashboard

Displays application statistics and recent applications.

![](https://github.com/drsudeep/jobtrackr/blob/main/dashboard.png?raw=true)

---

## 5️⃣ Applications Management

View, search, filter, edit, delete, and export applications.

![](https://github.com/drsudeep/jobtrackr/blob/main/applications.png?raw=true)

---

## 6️⃣ Add New Application

Add new job applications with complete details.

![](https://github.com/drsudeep/jobtrackr/blob/main/addapplication.png?raw=true)

---

# Tech Stack

## Backend

- Python
- Django
- Django ORM
- SQLite

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Tools

- Git
- GitHub
- VS Code

---

# Project Structure

```text
JobTrackr/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── jobs/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│   └── base.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

# How It Works

1. User registers an account.
2. User logs into the system.
3. User adds job applications.
4. Applications are stored in the database.
5. Users can edit or delete records.
6. Dashboard displays application statistics.
7. Search and filter help locate applications quickly.
8. Applications can be exported as CSV reports.

---

# Resume Highlights

- Developed a full-stack Job Application Tracking System using Django and Bootstrap.
- Implemented user authentication and session management.
- Built CRUD functionality for managing applications.
- Developed dashboard analytics for application tracking.
- Implemented search, filtering, and CSV export features.
- Designed responsive UI using Bootstrap 5.

---

# Future Enhancements

- Resume Upload Support
- Email Notifications
- Interview Scheduling
- Application Timeline Tracking
- Company-wise Analytics
- PostgreSQL Integration
- REST API Support
- Cloud Deployment

---

# Author

**Sudeep**

GitHub: https://github.com/drsudeep
