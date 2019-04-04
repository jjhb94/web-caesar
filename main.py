from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['# DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <!-- put some stuff into here :) -->
        <form method="post">
            <label for="rot">Rotate By</label>
            <input type="text" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="submit" name="submit query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"] #this takes the number field and converts it into int
    text = request.form["text"] # this takes what is is the text box and passes it to the the variable 

    new_message = rotate_string(text, int(rot))  # this calls the rotate_string function from Caesar and passes text and rot as parameters
    encrypted_message = '<h1>' + new_message + '</h1>' # this prints the returned value after the function manipulates the parameters above

    return encrypted_message  # make sure to return your final variable every time or else it will not do anything. 

app.run()
