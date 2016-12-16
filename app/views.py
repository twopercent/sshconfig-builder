from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>SSH config generator</title>
    </head>
    <body>
        <h1>SSH config generator</h1>

        <p1>Enter name:</p1>
    </body>
</html>
'''

