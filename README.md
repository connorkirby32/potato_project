
# Potato Backend Developer Test

This is a basic Django project which is designed to provide you with a few challenges to demonstrate your ability.

The application is a ticketing application. It stores tickets within projects and allows users to be assigned to these tickets.

Please fix the bugs and implement the features listed below.

Ensure that your code is committed with meaningful commit messages; show your working.

When you are finished please provide us with a URL to a repository where we can check out your code.

## Setup

- Run `./install_deps` (this will pip install requirements, and download the App Engine SDK)
- `python manage.py loaddata site`
- `python manage.py runserver`

The application is written using the [Djangae](http://djangae.readthedocs.org/en/latest/) project

## Tasks - bugs


- Tickets with long descriptions break the layout

## Tasks - new features


- On the project list page, projects that the user has assigned tickets on should be shown above the other projects

- Add the ability to delete tickets
- Improve the multiselect for assignees on the edit ticket page. Consider using a library such as [Chosen](http://harvesthq.github.io/chosen/) to help with this
- Add a watch task to the default gulp task so that changes to any of the SCSS files result in the CSS files being updated


## Bonus tasks

If you feel like carrying on improving this application, please do!

The following consistency task is one that you might like to have a look at.

### Eventual consistency

Pages seem to need a refresh after updating an object in the application

This is due to the fact that the Google App Engine datastore is an 'eventually consistant' database. Once an entity is saved some data retrieval operations may not immediately reflect this change. To read more about this see the Google App Engine [Datastore](https://cloud.google.com/appengine/docs/python/datastore/) documentation.

Can you create a solution to solve this problem?  There is no right or wrong solution.
