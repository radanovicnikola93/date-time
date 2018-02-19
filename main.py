#!/usr/bin/env python
import os
import jinja2
import webapp2
import time
import datetime

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        params = {"datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  'currentyear': datetime.date.today().strftime("%Y"),
                  'currentmonth': datetime.date.today().strftime("%B"),
                  'numofweek': datetime.date.today().strftime("%W"),
                  'numofdayinweek': datetime.date.today().strftime("%w"),
                  'dayofyear': datetime.date.today().strftime("%j"),
                  'dayofmonth': datetime.date.today().strftime("%d"),
                  'dayofweek': datetime.date.today().strftime("%A")}


        return self.render_template("index.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
