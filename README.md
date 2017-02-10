Introduction
Python is an excellent language for web programming due to its flexibility and high-level functionality. Web frameworks can make programming web applications much simpler because they connect many of the components necessary for a robust web interface.

While some web frameworks attempt to provide everything, others try to stay out of the way while taking care of the important, difficult to implement issues. Bottle is a Python framework that falls into the second category. It is extremely lightweight, but also makes it easy to develop applications quickly.

In this guide, we will cover how to set up and use Bottle to create simple web applications on a Ubuntu 14.04 server.

Prerequisites
Before you begin this guide you'll need the following:

A Ubuntu 14.04 Droplet
A working knowledge of how to edit text files from the command line
A sudo user
Step 1 — Install a Virtual Environment for Python
Python, the programming language that Bottle is built for, comes installed on Ubuntu by default.

We will install the python-virtualenv package to isolate our Python project from the system's Python environment. The virtualenv software allows us to create a separate, contained environment for our Python projects that will not affect the entire OS.

Update your package lists:

sudo apt-get update
Install python-virtualenv from the repositories:

sudo apt-get install python-virtualenv
We are going to create a projects folder in our home directory, and then create a virtual environment within this folder:

mkdir ~/projects
cd ~/projects
virtualenv --no-site-packages venv
This creates a directory called venv within the projects directory. It installs some Python utilities within this folder and created a directory structure to install additional tools.

Step 2 — Activate the Virtual Environment for Python
We must activate the virtual environment before beginning to work on our project:

source venv/bin/activate
The command prompt will change to reflect the fact that we are operating in a virtual environment now.

If you need to reconnect later, make sure you activate the environment again with these commands:

cd ~/projects
source venv/bin/activate
If you need to exit the virtual environment, you can type this at any time:

deactivate
Do not deactivate your virtual environment at this point.

Step 3 — Install Bottle
One of the tools that the virtualenv program installed was pip.

This tool allows us to easily install Python packages from the Python package index, an online repository.

If we want to search for Python packages that have to do with Bottle, we can run:

pip search bottle
We will start by installing the Bottle package:

pip install bottle
After the process completes, we should have the ability to use the Bottle framework within our applications.

Step 4 — Create Your First Bottle Application
Bottle, like most frameworks, implements a version of the MVC software pattern. MVC stands for model, view, and controller, and it describes a decision to separate the different functions of a user interface.

The model is a representation of a set of data and is responsible for storing, querying, and updating data. The view describes how information should be rendered to the user. It is used to format and control the presentation of data. The controller is the main processing center of the app, which decides how to respond to user requests.

Bottle applications can be incredibly simple. In their most bare form, they can implement all of these components within a single file. We will create a "hello world" application to show how this is done.

With your favorite text editor, create a Python application called hello.py:

nano ~/projects/hello.py
We'll show you each line one a time, and include the final file at the end of this section.

Within this file, the first line we will add imports some functionality from the Bottle package. This will allow us to use the framework tools within our application:

hello.py
from bottle import route, run
This line tells our program that we want to import the route and run modules from the Bottle package.

The run module that we are importing can be used to run the application on a development server, which is great for quickly seeing the results of your program
The route module that we are importing is responsible for telling the application what URL requests get handled by which Python functions. Bottle applications implement routing by calling a single Python function for each URL requested. It then returns the results of the function to the user
We can add a route right now that will match the URL pattern /hello. Add one new line at the bottom of the file:

hello.py
from bottle import route, run

@route('/hello')
This route decorator matches the URL /hello, so when that path is requested on the server, the function that directly follows will be executed. Add two more lines at the end of the file:

hello.py
from bottle import route, run

@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"
This function is very simple, but it completes the only requirement of a routing function: it returns a value that can be displayed in the web browser. In this case, the value is a simple HTML string. We could remove the h1 header tags and the same information would be displayed in an undecorated fashion.

Finally, we need to run our application using the development server. Add the final line, and now your file is complete:

hello.py
from bottle import route, run

@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

run(host='0.0.0.0', port=8080)
This line will run the server instance.

By passing the parameter host='0.0.0.0', this will serve the content to any computer, not just the local machine. This is important since our application is being hosted remotely
The port parameter specifies the port that this will be using
Save and close the file.

We can run this application with this command:

python ~/projects/hello.py
You can visit this application in your web browser by going to your IP address, followed by the port we chose to run on (8080), followed by the route we created (/hello):

http://your_server_ip:8080/hello
It will look like this:

DigitalOcean Bottle hello world

You can stop the server at any time by typing:

CTRL-C
