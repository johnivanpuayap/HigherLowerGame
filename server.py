import random

from flask import Flask


def check_valid_number(function):
    def wrapper(**kwargs):
        number = kwargs.get('number')
        if number is None or number < 0 or number > 9:
            return ("<h1>Invalid Number: Make sure to guess a number between 0 and 9!</h1>"
                    "<img src='https://media.giphy.com/media/B0uJ6d5OXb50k/giphy.gif' alt='gif of a warning sign'>")
        return function(**kwargs)

    return wrapper


random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif of numbers from 0 to 9'>"


@app.route("/<int:number>")
@check_valid_number
def check_it(number):
    if number > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='gif of a dog'>"
    elif number < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='gif of a dog'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='gif of a dog'>"


if __name__ == "__main__":
    app.run(debug=True)
