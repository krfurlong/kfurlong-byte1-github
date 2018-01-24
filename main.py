# Initial .py template courtesy and copyright 2016 Google Inc.
# Subsequent work by Kyle Furlong
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Imports
import os
import jinja2
import webapp2
import logging


JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def helloIndex():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()
    
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Oops, nothing up my sleeve! Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Dang, something went wrong! Unexpected error: {}'.format(e), 500   
   
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello, World!')




#app = webapp2.WSGIApplication([
#    ('/', MainPage),
#], debug=True)

