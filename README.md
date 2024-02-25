# EDDIFY - A E-Learining Platform For Students

![logo.png](web_dynamic/static/images/Eddify-logos_transparent.png)

## 🚀 Welcome to EDDIFY: Your Gateway to Limitless Learning 🚀

Welcome to EDDIFY, where learning knows no bounds! As your premier e-learning platform, EDDIFY is crafted to unleash your intellectual potential and guide you on a journey of continuous education. Whether you're a seasoned professional, a student eager to explore new horizons, or someone embarking on a lifelong learning adventure, EDDIFY is your trusted companion.

# EDDIFY API LINKS - Courses and Categories

Explore the EDDIFY API for various functionalities related to courses and categories:

1. **Get All Categories**
    - **Endpoint:** `/category`
    - **Method:** `GET`
    - **Description:** Retrieve information about all course categories.
    - **Usage:** View a list of all available course categories.
    - **Link:** [Get All Categories API](#)

2. **Get Courses by Category**
    - **Endpoint:** `/category/<category_id>/courses`
    - **Method:** `GET`
    - **Description:** Retrieve a list of courses under a specific category.
    - **Usage:** View courses associated with a particular category.
    - **Link:** [Get Courses by Category API](#)

3. **Get Course by ID**
    - **Endpoint:** `/courses/<course_id>/`
    - **Method:** `GET`
    - **Description:** Retrieve details about a specific course by its ID.
    - **Usage:** Get information on a particular course.
    - **Link:** [Get Course by ID API](#)

4. **Get All Courses**
    - **Endpoint:** `/courses`
    - **Method:** `GET`
    - **Description:** Retrieve information about all available courses.
    - **Usage:** View a list of all courses on EDDIFY.
    - **Link:** [Get All Courses API](#)

5. **Get Enrolled Courses for a User**
    - **Endpoint:** `/profile/courses/<user_id>/enrolled-courses`
    - **Method:** `GET`
    - **Description:** Retrieve courses that a user is enrolled in.
    - **Usage:** View the courses in which a user is currently enrolled.
    - **Link:** [Get Enrolled Courses API](#)

6. **Delete Course by ID**
    - **Endpoint:** `/courses/<course_id>/`
    - **Method:** `DELETE`
    - **Description:** Delete a course based on its ID.
    - **Usage:** Remove a course from EDDIFY.
    - **Link:** [Delete Course by ID API](#)

7. **Create Course in a Category**
    - **Endpoint:** `/category/<category_id>/courses`
    - **Method:** `POST`
    - **Description:** Create a new course under a specific category.
    - **Usage:** Add a new course to a designated category.
    - **Link:** [Create Course in a Category API](#)

8. **Update Course by ID**
    - **Endpoint:** `/courses/<course_id>/`
    - **Method:** `PUT`
    - **Description:** Update details of a specific course.
    - **Usage:** Modify information about a particular course.
    - **Link:** [Update Course by ID API](#)

Feel free to explore and interact with these APIs to enhance your learning experience on EDDIFY.

# EDDIFY API LINKS - User Management

Explore the EDDIFY API for various user-related functionalities:

1. **Get All Users**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/users](http://0.0.0.0:5000/api/v1/users)
    - **Method:** `GET`
    - **Description:** Retrieve the list of all user objects or a specific user.
    - **Link:** [Get All Users API](http://0.0.0.0:5000/api/v1/users)

2. **Get User by ID**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/users/<user_id>](http://0.0.0.0:5000/api/v1/users/<user_id>)
    - **Method:** `GET`
    - **Description:** Retrieve details of a specific user.
    - **Link:** [Get User by ID API](http://0.0.0.0:5000/api/v1/users/<user_id>)

3. **Delete User**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/users/<user_id>](http://0.0.0.0:5000/api/v1/users/<user_id>)
    - **Method:** `DELETE`
    - **Description:** Delete a user object.
    - **Link:** [Delete User API](http://0.0.0.0:5000/api/v1/users/<user_id>)

4. **User Signup**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/signup](http://0.0.0.0:5000/api/v1/signup)
    - **Method:** `POST`
    - **Description:** Create a new user account.
    - **Link:** [User Signup API](http://0.0.0.0:5000/api/v1/signup)

5. **User Login**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/login](http://0.0.0.0:5000/api/v1/login)
    - **Method:** `POST`
    - **Description:** Authenticate and log in a user.
    - **Link:** [User Login API](http://0.0.0.0:5000/api/v1/login)

6. **User Authentication**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/auth](http://0.0.0.0:5000/api/v1/auth)
    - **Method:** `GET`
    - **Description:** Authenticate and retrieve user details.
    - **Link:** [User Authentication API](http://0.0.0.0:5000/api/v1/auth)

7. **Update User**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/users/<user_id>](http://0.0.0.0:5000/api/v1/users/<user_id>)
    - **Method:** `PUT`
    - **Description:** Update user information.
    - **Link:** [Update User API](http://0.0.0.0:5000/api/v1/users/<user_id>)

Feel free to explore these APIs to manage your user accounts on EDDIFY.

# EDDIFY API LINKS - User Enrollments

Explore the EDDIFY API for managing user enrollments:

1. **Get User Enrollments**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/user/<user_id>/enrollments](http://0.0.0.0:5000/api/v1/user/<user_id>/enrollments)
    - **Method:** `GET`
    - **Description:** Retrieve the list of all enrollments of a user, along with details of the enrolled courses.
    - **Link:** [Get User Enrollments API](http://0.0.0.0:5000/api/v1/user/<user_id>/enrollments)

2. **Get Enrollment by ID**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>](http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>)
    - **Method:** `GET`
    - **Description:** Retrieve details of a specific enrollment.
    - **Link:** [Get Enrollment by ID API](http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>)

3. **Delete Enrollment**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>](http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>)
    - **Method:** `DELETE`
    - **Description:** Delete an enrollment object.
    - **Link:** [Delete Enrollment API](http://0.0.0.0:5000/api/v1/enrollments/<enrollment_id>)

4. **Create Enrollment**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/course/<user_id>/enrollments](http://0.0.0.0:5000/api/v1/course/<user_id>/enrollments)
    - **Method:** `POST`
    - **Description:** Enroll a user in a course.
    - **Link:** [Create Enrollment API](http://0.0.0.0:5000/api/v1/course/<user_id>/enrollments)

5. **Update Enrollment**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/enrollment/<enrollment_id>](http://0.0.0.0:5000/api/v1/enrollment/<enrollment_id>)
    - **Method:** `PUT`
    - **Description:** Update enrollment information.
    - **Link:** [Update Enrollment API](http://0.0.0.0:5000/api/v1/enrollment/<enrollment_id>)

Feel free to use these APIs to manage user enrollments on EDDIFY.

# EDDIFY API LINKS - Course Lessons

Explore the EDDIFY API for managing course lessons:

1. **Get Lessons of a Course**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/course/<course_id>/lesson](http://0.0.0.0:5000/api/v1/course/<course_id>/lesson)
    - **Method:** `GET`
    - **Description:** Retrieve the list of all lessons associated with a course.
    - **Link:** [Get Lessons of a Course API](http://0.0.0.0:5000/api/v1/course/<course_id>/lesson)

2. **Get Lesson by ID**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/lesson/<lesson_id>](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)
    - **Method:** `GET`
    - **Description:** Retrieve details of a specific lesson.
    - **Link:** [Get Lesson by ID API](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)

3. **Delete Lesson**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/lesson/<lesson_id>](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)
    - **Method:** `DELETE`
    - **Description:** Delete a lesson object.
    - **Link:** [Delete Lesson API](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)

4. **Create Lesson**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/course/<course_id>/lesson](http://0.0.0.0:5000/api/v1/course/<course_id>/lesson)
    - **Method:** `POST`
    - **Description:** Create a new lesson associated with a course.
    - **Link:** [Create Lesson API](http://0.0.0.0:5000/api/v1/course/<course_id>/lesson)

5. **Update Lesson**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/lesson/<lesson_id>](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)
    - **Method:** `PUT`
    - **Description:** Update lesson information.
    - **Link:** [Update Lesson API](http://0.0.0.0:5000/api/v1/lesson/<lesson_id>)

Feel free to use these APIs to manage lessons associated with courses on EDDIFY.

# EDDIFY API LINKS - Course Reviews

Explore the EDDIFY API for managing course reviews:

1. **Get Reviews of a Course**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/course/<course_id>/reviews](http://0.0.0.0:5000/api/v1/course/<course_id>/reviews)
    - **Method:** `GET`
    - **Description:** Retrieve the list of all reviews associated with a course.
    - **Link:** [Get Reviews of a Course API](http://0.0.0.0:5000/api/v1/course/<course_id>/reviews)

2. **Get Review by ID**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/reviews/<review_id>](http://0.0.0.0:5000/api/v1/reviews/<review_id>)
    - **Method:** `GET`
    - **Description:** Retrieve details of a specific review.
    - **Link:** [Get Review by ID API](http://0.0.0.0:5000/api/v1/reviews/<review_id>)

3. **Delete Review**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/reviews/<review_id>](http://0.0.0.0:5000/api/v1/reviews/<review_id>)
    - **Method:** `DELETE`
    - **Description:** Delete a review object.
    - **Link:** [Delete Review API](http://0.0.0.0:5000/api/v1/reviews/<review_id>)

4. **Create Review**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/course/<course_id>/reviews](http://0.0.0.0:5000/api/v1/course/<course_id>/reviews)
    - **Method:** `POST`
    - **Description:** Create a new review associated with a course.
    - **Link:** [Create Review API](http://0.0.0.0:5000/api/v1/course/<course_id>/reviews)

5. **Update Review**
    - **Endpoint:** [http://0.0.0.0:5000/api/v1/reviews/<review_id>](http://0.0.0.0:5000/api/v1/reviews/<review_id>)
    - **Method:** `PUT`
    - **Description:** Update review information.
    - **Link:** [Update Review API](http://0.0.0.0:5000/api/v1/reviews/<review_id>)

Feel free to use these APIs to manage reviews associated with courses on EDDIFY.

- [Introduction](#)
- [Key Features](#key-features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)


## Key Features

1. **Extensive Course Catalog:** A diverse and comprehensive library of courses covering a wide range of subjects and industries.
2. **Adaptive Learning Paths:** Personalized learning experiences that adapt to the learner's pace, skill level, and preferred learning style.
3. **Expert Instructors:** Courses led by industry professionals and subject matter experts, providing valuable real-world insights.
4. **Collaborative Learning Community:** A vibrant community where learners can connect, collaborate, and share knowledge with peers and mentors.
5. **Mobile Accessibility** Responsive design or a dedicated mobile app for seamless learning experiences on various devices.
6. **Progress Tracking and Analytics:** Tools that allow learners to track their progress, receive performance analytics, and identify areas for improvement.
7. **User-Friendly Interface:** Intuitive and user-friendly interface for easy navigation and a positive user experience.
8. **Accessibility Features:** Inclusion of accessibility features to ensure that the platform is usable by individuals with diverse abilities.

## Testing

We've thoroughly tested our platform to ensure a smooth and efficient user experience. If you face any issues, feel free
to reach out

## Technologies Used

- Python
- MySQL
- Flask

## Deployed Site

Explore EDDIFY now: [EDDIFY Platform](https://eddify-frontend.onrender.com/) 

## Final Project Blog Article

Read about the journey of building EDDIFY: [EDDIFY Project Blog](https://medium.com/@kasshymoni0812/announcing-eddify1-0-f22a8a8d7c0a) 

## Authors

- [Adeniran Timilehin](https://www.linkedin.com/in/timilehin-adeniran-342710234?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) - [LinkedIn](https://www.linkedin.com/in/timilehin-adeniran-342710234?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) 
- [Oke Kolawole](https://www.linkedin.com/in/kolawole-sunday-oke-38b1871a3/) - [LinkedIn](https://www.linkedin.com/in/kolawole-sunday-oke-38b1871a3/)