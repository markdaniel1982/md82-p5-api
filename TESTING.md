# TESTING

## Table of Contents

- [TESTING](#testing)
  - [Table of Contents](#table-of-contents)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Bugs](#bugs)
      - [Code](#code)
      - [CI Python Linter](#ci-python-linter)
      - [Heroku Deployment](#heroku-deployment)
    - [Unresolved Bugs](#unresolved-bugs)

### Manual testing of user stories

Profiles

| TEST | OUTCOME | PASS/FAIL | RESOLUTION |
|:---:|:---:|:---:|:---:|
| Add "/profiles" in deployed url | profile list page opens | Pass |
| User scrolls through the profile list | profiles of users are displayed | Pass |
| Add "/profiles/id" in deployed url | profile detail page loads | Pass |
| Add "/profiles/id" in deployed url (id of user's profile) | profile detail page loads with edit form | Pass |
| User update the data and click on put | updated data is shown in profile list  | Pass |
| Add "/profiles/id" in deployed url (id of user's profile) | profile detail page loads with delete button | Pass |
| User clicks on delete button  | profile is deleted | Pass |

Tasks
| TEST | OUTCOME | PASS/FAIL | RESOLUTION |
|:---:|:---:|:---:|:---:|
| Add "/tasks" in deployed url | tasks lists page loads with create form | Pass |
| User add the data and click on post | new task is shown in tasks list  | Pass |
| Add "/tasks/id" in deployed url (id of user's task) | task detail page loads with edit form | Pass |
| Add "/tasks/id" in deployed url (id of user's task) | task detail page loads with delete button | Pass |
| User update the data and click on put | updated data is shown in tasks list | Pass |
| User clicks on delete button  | task is deleted | Pass |

Comments
| TEST | OUTCOME | PASS/FAIL | RESOLUTION |
|:---:|:---:|:---:|:---:|
| User scrolls through the comments list | comments are displayed | Pass |
| Add "/comments" in deployed url | comment lists page loads with create form | Pass |
| User add the data and click on post | comment is shown in comments list | Pass |
| Add "/comments/id" in deployed url (id of user's comment) | comment detail page loads with edit form and delete button | Pass |
| User update the data and click on put | updated data is shown in comments list | Pass |
| User clicks on delete button  | comment is deleted | Pass |

### Bugs

During development, an issue arose when building the front end react app. When submitting the CreateTaskForm, the priority and privacy fields had been switched. This was fixed by amending the code in the API models and serializers and the react app form so the fields were matching in the axios request.

#### Code

- No error was found

#### CI Python Linter

- No bug was found during Python Validation

#### Heroku Deployment

- No error found during deployment

### Unresolved Bugs

- No unresolved bugs from developer side
