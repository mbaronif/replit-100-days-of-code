from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    page = """<html><body>
    <p><a href="/home">Go home</a></p>
    </body></html>"""
    return page

@app.route("/home")
def home():
    page = """<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>Mari's Portfolio</title>
        <link href="style-main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <h1>Mari's Portfolio</h1>
        <h2>Day 44</h2>
        <p>
            <h3>The project: Bingo</h3>
            <p>The program randomly generates a bingo card (3x3).
            The user inputs the numbers. If the number is in the bingo card,
            it's marked with an "X", otherwise, the game continues.
            </p>
            <h3>Strength:</h3>
            <ul>
                <li>Use of different modes of the random library</li>
                <li>Use of arrays to create the bingo card</li>
                <li>Use of "try/except" to prevent errors</li>
            </ul> 
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-44-bingo.png" width="50%">
            <br><br>
            <a href="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2044%20-%20Bingo%20Game.py" class="pointer">GitHub</a>
        </p>
        <hr width="50%" align="left">
        <h2>Day 47</h2>
        <p>
            <h3>The project: Top Trumps</h3>
            <p>Inspired by the Pokémon world, this game is a very simple
            version of the old Top Trumps, where the highest value wins.
            Here, the user plays against the computer. There is a predefined
            list of characters the user can choose to the battle. Once they
            choose their Pokémon, the computer randomly picks one too. Next,
            the user will pick one feature to compare, then the game reveals
            the winner.
            </p>
            <h3>Strength:</h3>
            <ul>
                <li>Use of dictionaries to store the characters' features</li>
                <li>Use of different modes of the random library</li>
                <li>Strategic use of comments in the code, explaining just the necessary aspects of it</li>
            </ul> 
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-47-top-trumps.png" width="50%">
            <br><br>
            <a href="https://raw.githubusercontent.com/replit-100-days-of-code/blob/main/Day%2047%20-%20Top%20Trumps.py" class="pointer">GitHub</a>
        </p>
        <hr width="50%" align="left">
        <h2>Day 59</h2>
        <p>
            <h3>The project: Palindrome</h3>
            <p>This program only checks whether a word inputed by the user
            is a palindrome. For a positive response, it prints "TRUE", 
            otherwise it prints "FALSE".
            </p>
            <h3>Strength:</h3>
            <ul>
                <li>Explores the possibility of reading a word backwards, considering it's length</li>
                <li>Very simple and straightfoward</li>
                <li>Use of methods to prevent errors with the user's input</li>
            </ul> 
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-59-palindrome-false.png" width="50%">
            <br>
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-59-palindrome-true.png" width="50%">
            <br><br>
            <a href="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2059%20-%20Palindrome.py" class="pointer">GitHub</a>
        </p>
        <hr width="50%" align="left">
        <h2>Day 60</h2>
        <p>
            <h3>The project: Event Countdown Timer</h3>
            <p>This program helps the user forseen how many days are left
            until the big day of an event. If the event is in the past,
            the program will let the user know they already lost it.
            </p>
            <h3>Strength:</h3>
            <ul>
                <li>Introducing the use of the datetime library</li>
                <li>Informs the user about how many days in the future or
                    in the past the event is.</li>
            </ul> 
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-60-event-countdown-1.png" width="50%">
            <br>
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-60-event-countdown-2.png" width="50%">
            <br><br>
            <a href="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2060%20-%20Time.py" class="pointer">GitHub</a>
        </p>
        <hr width="50%" align="left">
        <h2>Day 61</h2>
        <p>
            <h3>The project: One-Person Tweeter</h3>
            <p>This program prompts the person for a tweet. The user can
            input as many messages as they want. The messages are saved 
            and can be accessed later, trough the main menu. The messages 
            are displayed chronologically, with the respective data/time.
            </p>
            <h3>Strength:</h3>
            <ul>
                <li>Use of different resourses of the datetime library</li>
                <li>Store of messages chronologically</li>
                <li>Messages can be accessed by the user</li>
            </ul> 
            <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/day-61-one-person-tweeter.png" width="50%">
            <br><br>
            <a href="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2061%20-%20DB_One-Person-Tweeter.py" class="pointer">GitHub</a>
        </p>
    </body>
</html>""" 
    return page

@app.route("/linktree")
def linkTree():
    page = """<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <link href="style-link-tree.css" rel="stylesheet" type="text/css">
        <title>Where to find me</title>
    </head>
    <body>
        <img src="https://github.com/mbaronif/replit-100-days-of-code/blob/main/Day%2076%20-%20Flask/day-76-flask/images/eu.jpg" alt="Person wearing a pink sweater sitting indoors with hand resting on chin, in front of a decorative black tapestry with cranes and red flowers, and a framed photo on a cream-colored wall in the background. The setting appears calm and cozy." >
        <h1>Mariana Baroni</h1>
        <h3>Software developer</h3>
        <br><br>
        <h2>Socials</h2>
        <ul>
            <li><a href="https://www.linkedin.com/in/maribaroni/">LinkedIn</a></li>
            <li><a href="https://github.com/mbaronif/">GitHub</a></li>
            <li><a href="https://x.com/amaribaroni">X</a></li>
            <li><a href="https://bsky.app/profile/maribaroni.bsky.social">Bluesky</a></li>
        </ul>
    </body>
</html>"""
    return page

app.run(host="0.0.0.0", port=81)