from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>config generator</title>
    </head>
    <body>
        <h1>Complete the following form</h1>
    </body>
</html>
'''

