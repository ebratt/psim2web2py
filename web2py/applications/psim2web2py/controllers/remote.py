# -*- coding: utf-8 -*-

auth.settings.allow_basic_login = True
@auth.requires_login()
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