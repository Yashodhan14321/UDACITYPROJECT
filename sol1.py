#!/usr/bin/env python
from flask import Flask, request, redirect, url_for
from dbsol1 import get_posts

app = Flask(__name__)


HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>SOLUTION1</title>
    </head>
    <body>
        MOST POPULAR THREE ARTICLES OF ALL THE TIME<br>
                %s
    </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
            %s &nbsp; - &nbsp; %s &nbsp; views <br>
'''


@app.route('/', methods=['GET'])
def main():
    posts = "".join(POST % (title, num) for title, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
