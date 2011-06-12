# -*- coding: utf-8 -*-

"""
httpbin.core
~~~~~~~~~~~~

This module provides the core HttpBin experience.
"""

import json

from decorator import decorator
from flask import Flask, request, render_template

from .structures import CaseInsensitiveDict


app = Flask(__name__)

@decorator
def json_resource(f, *args, **kwargs):

    _dict = f(*args, **kwargs)

    dump = json.dumps(_dict)

    r = app.make_response(dump)
    r.headers['Content-Type'] = 'application/json'

    return r


# ------
# Routes
# ------


@app.route('/')
def view_landing_page():
    """Generates Landing Page."""
    return render_template('httpbin.1.html')


@app.route('/ip')
@json_resource
def view_origin():
    """Returns Origin IP."""

    return dict(ip=request.remote_addr)


@app.route('/headers')
@json_resource
def view_headers():
    """Returns HTTP HEADERS."""

    return dict(headers=get_headers())



@app.route('/user-agent')
@json_resource
def view_user_agent():
    """Returns User-Agent."""

    headers = CaseInsensitiveDict(request.headers.items())

    return dict(useragent=headers['user-agent'])



@app.route('/get')
@json_resource
def view_get():
    return 'get'



# /headers
# /get
# /post
# /put
# /delete



if __name__ == '__main__':
    app.run()