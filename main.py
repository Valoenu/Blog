from flask import Flask, render_template
import requests
from make_post import MakePost


# You can use n;Point 
blogs = requests.get("Your blog posts JSON here")

blogs_elements = []
for blogs in blogs:
    blogs_elem = MakePost(blogs_elements['id'] blogs['title'], blogs['subtitle'], blogs['body'])
    blogs_elements.append(blogs_elements)


# Active our Flask 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_blogs=blogs_element)


@app.route("/post/<int:index>")
def show_blog(index):
    requested_post = None
    for blog_post in blogs_elements:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)



if __name__ == "__main__":
    app.run(debug=True)



