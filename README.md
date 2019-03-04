# Welcome to Meleé Island!
This is a simple project that started as part of a training, just for learning purposes. But while I was learning I thought: "Why not make this fun?". So I started *insults_api*.

The project is build on [Python 2](https://www.python.org/downloads/release/python-272/), using [Flask](http://flask.pocoo.org/) framework, so you'll need to install some dependencies if you want to fork this one. A [virtual environment](https://docs.python-guide.org/dev/virtualenvs/) is recommended for this :)



## About the code
It's kinda self explanatory: *api.py* is the main entry point, while *get_data.py* is just a helpful module to get things in place.

## About the routes
Every route returns a JSON object related with insults in some way or another:

- */insults*: Get all the insults for every sword fight.
- */comebacks*: Get just the comebacks for the insults.
- */all*: Get every insult with every one of its comebacks!
