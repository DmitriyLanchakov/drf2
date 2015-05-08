# Django REST Framework v2 demo app

This app was created for presentation during OpenWest 2015. It borrows heavily from [the canonical tutorials](http://tomchristie.github.io/rest-framework-2-docs/#tutorial) by [Tom Christie](https://twitter.com/_tomchristie).

## Note: this app uses v2 of Django REST Framework.
Looking for v3? [Try here](https://github.com/zeantsoi/drf3).

### Requirements
As specified in the `requirements.txt`, this demo is designed to run the following:
- Django 1.6.2
- South 0.7.5
- Django REST Framework 2.4.5

### Getting up and running
Do this, more or less:
- Clone [this repository](git@github.com:zeantsoi/drf2) from GitHub
- From the project root, run `pip install -r requirements.txt`
- `python manage.py syncdb`
- `python manage.py migrate`
- Fire up your webserver and grab [the API docs](http://tomchristie.github.io/rest-framework-2-docs/#api-guide); you're ready to go!
 
### What to do
Play around with these endpoints to see how the RESTful interface works.
- `/basic/campaigns` _(pure JSON implementation)_
- `/basic/campaigns/:id` _(pure JSON implementation)_
- `/browseable/campaigns`
- `/browseable/campaigns/:id`
- `/class_based/campaigns`
- `/class_based/campaigns/:id`
- `/generic_class_based/campaigns`
- `/generic_class_based/campaigns/:id`
- `/authenticated/campaigns`
- `/authenticated/campaigns/:id`
- `/viewset/campaigns`
- `/viewset/campaigns/:id`
- `/viewset/users`
- `/viewset/users/:id`

### What's the purpose of this app?
To show just a fraction of the wonders of Django REST Framework in its past glory and to highlight some shortcomings that are resolved in v3.

### Questions?
[@zeantsoi](https://twitter.com/zeantsoi)
