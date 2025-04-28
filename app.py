from flask import Flask

# Create a Flask application instance
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses it to determine where to look for resources like templates and static files.
app = Flask(__name__)

# The @app.route('/') decorator associates the URL '/' with the hello_world function.
# When you visit the root URL of the application, this function will be executed.
@app.route('/')
def hello_world():
  """Returns a simple 'Hello, World!' string."""
  return 'Hello, World!'

# This block ensures that the development server is only started when
# the script is executed directly (not when imported as a module).
if __name__ == '__main__':
  # app.run() starts the Flask development server.
  # debug=True allows the server to reload automatically when you make changes
  # and provides a debugger in the browser for errors.
  app.run(debug=True)