from flask import Flask


# Each Flask's app needs to have an unique name
app = Flask(__name__)

# The command below is going to define what the application is going to do when
# a client requests some data from my app.
# The function is going to execute if the visitor enter in the home page (our endpoint)
@app.route("/")
def home():
	"""Return the Hello, world phrase if the endpoint used is the homepage."""
    return "Hello, world!"


if __name__ == "__main__":
    # Execute the app, considering the debug flag, which shows more data if it raises an error
    app.run(debug=True)
