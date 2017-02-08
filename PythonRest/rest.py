#!/usr/bin/env python

import web
import json

urls = (
    '/', 'index',
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class index:        
    def GET(self):
        return ""

class list_users:        
    def GET(self):
        pyDict = {'one':1,'two':2}
        web.header('Content-Type', 'application/json')
        return json.dumps(pyDict)

class get_user:
    def GET(self, userId):
        print self
        return "getUser:" + userId

if __name__ == "__main__":
    app.run()

