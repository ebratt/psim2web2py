# -*- coding: utf-8 -*-
import os


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to psim2web2py!")
    message = "Hello and welcome to psim2web2py!"
    return dict(message=message)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


auth.settings.allow_basic_login = True
# @auth.requires_login()
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection

    rules = {
        'Simulation': {
            'GET':    {'query': None, 'fields': ['id']},
            'POST':   {'query': None, 'fields': None},
            'PUT':    {'query': None, 'fields': ['id']},
            'DELETE': {'query': None},
            }}
    return Collection(db).process(request, response, rules)


# auth.settings.allow_basic_login = True
# @auth.requires_login()
# @request.restful()
# def api():
#     response.view = 'generic.'+request.extension
#     def GET(*args,**vars):
#         patterns = 'auto'
#         parser = db.parse_as_rest(patterns,args,vars)
#         if parser.status == 200:
#             return dict(content=parser.response)
#         else:
#             raise HTTP(parser.status,parser.error)
#     def POST(table_name,**vars):
#         return db[table_name].validate_and_insert(**vars)
#     def PUT(table_name,record_id,**vars):
#         return db(db[table_name]._id==record_id).update(**vars)
#     def DELETE(table_name,record_id):
#         return db(db[table_name]._id==record_id).delete()
#     return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)