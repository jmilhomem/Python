from flask import Flask, render_template, request, redirect, url_for


# https://github.com/tecladocode/complete-python-course/blob/master/course_contents/15_flask/projects/first-flask-app-lectures/3-rendering-html/templates/post.jinja2
# https://github.com/tecladocode/first-flask-app/blob/master/templates/post.jinja2

# Each Flask's app needs to have an unique name
app = Flask(__name__)

posts = {
    0: {
        "post_id": 0,
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
    post_message = posts.get(post_id)
    if post_message:
    	return render_template("post.jinja2", post=posts.get(post_id))
    else:
        return render_template("404.jinja2", message=f"A post with id {post_id} was not found") 


# Another endpoint to get the parameters inside the form created to manipulate data
# and get the data as a query string parameters
@app.route("/post/form")
def form():
    """Get the parameters inputed inside the form."""
    return render_template("create.jinja2")


# This route will be arrived at looking like this:
# 127.0.0.1:5000/post/create
# http://127.0.0.1:5000/post/form?title=teste&content=teste123
# It will also have some inner data as part of the payload (which is hidden), containing the data in the form.
@app.route("/post/create")
def create():
    # Behind the scenes, Flask is turning the query string parameters into a dictionary
    title = request.arg.get("title")  # This takes the "Hello" from the form contents. 
    content = request.arg.get("content")  # This takes the "This is the post content" form the form contents.
    post_id = len(posts)
    posts[post_id] = {"id": post_id, "title": title, "content": content}

    # The url_for method is going to use the function post to get the URL, passing the post_id parameter
    # redirect method is going to redirect the browser to the url_for's result url
    return redirect(url_for("post", post_id=post_id))


if __name__ == "__main__":
    # Execute the app, considering the debug flag, which shows more data if it raises an error
    app.run(debug=True)
