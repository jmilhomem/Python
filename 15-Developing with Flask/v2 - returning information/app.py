from flask import Flask


# Each Flask's app needs to have an unique name
app = Flask(__name__)

posts = {
    0: {
        "title": "Hello World",
        "content": "This is my first blog post!"
    }
}

# The command below is going to define what the application is going to do when
# a client requests some data from my app.
# The function is going to execute if the visitor enter in the home page (our endpoint)
@app.route("/")
def home():
	"""Return the Hello, world phrase if the endpoint used is the homepage."""
    return "Hello, world!"


# Another endpoint to return the post
@app.route("/post/<int:post_id>")
def post(post_id):
	"""Return the payload if the endpoint used is the some message's id."""
	post = posts.get(post_id)
	#return f"Post {post["title"], content: \n\n {post["content"]}}"
	return post


if __name__ == "__main__":
    # Execute the app, considering the debug flag, which shows more data if it raises an error
    app.run(debug=True)
