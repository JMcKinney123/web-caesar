from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True


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
                form = method['POST']
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="rotate_by">Rotate by:</label>
            <input id="rotate_by" type="text" name="rot" value=0 />
            <input type="submit" />
            <textarea name="text"></textarea>
        </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])

def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text= request.form['text']
    answer = ""
    for char in text:
        new = rotated_character(char, rot)
        answer = answer + new
        rotated = form.format(answer)
        return '<h1>rotated</h1>'
app.run()