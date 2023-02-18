# imports Flask from the package flask
from flask import Flask, request

# creates an instance of the Flask object using our module's name as a parameter
# __name__ links our module to the Flask object
app = Flask(__name__)

# Flask uses decorators for URL routing
# this function calls whenever whenever a user visits the main root page of the web app
# in this case it is defined by a single forward slash
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"
    # user_agent = request.headers.get("User-Agent")
    # return f"<p>Your browser is {user_agent}</p>"

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
# it runs on port 5000, use port 80 for prod
# debug is set to true to see detailed errors in the web browser    
    app.run(port=5000, debug=True)

