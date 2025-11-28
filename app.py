from flask import Flask, request, jsonify, make_response, url_for, redirect, render_template
import sqlite3


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("portofolio.db")
    conn.row_factory = sqlite3.Row
    return conn
    

#home route
@app.route('/')
def index():
    return render_template('index.html')

#about page
@app.route('/about')
def about():
    db = get_db_connection()
    skills = db.execute("select * from skills").fetchall()
    db.close()
    return render_template('about.html', skills = skills)

# project page
@app.route('/projects')
def projects():
    db = get_db_connection()
    projects = db.execute("select * from projects").fetchall()
    db.close()
    return render_template('projects.html', projects = projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    conn = get_db_connection()
    project = conn.execute('SELECT * FROM projects WHERE id = ?', (project_id,)).fetchone()
    conn.close()
    return render_template('project_detail.html', project=project)

#blog page
@app.route('/blog')
def blog():
    db = get_db_connection()
    blogs = db.execute("select * from posts").fetchall()
    db.close()
    return render_template("blog.html", blogs = blogs)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    db = get_db_connection()
    blog = db.execute("select * from posts where id = ?", (blog_id,)).fetchone()
    db.close()
    return render_template("blog_detail.html", blog = blog)

# for resume.html
@app.route('/resume')
def resume():
    return render_template("resume.html")

# for contact.html

@app.route('/contact')
def contact():
    return render_template("contact.html")