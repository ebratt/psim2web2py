# -*- coding: utf-8 -*-
from plugin_tablescope import TableScope
from plugin_solidtable import SOLIDTABLE, OrderbySelector


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    logged_in = auth.user or False

    # build the SOLIDTABLE
    orderby_selector = OrderbySelector([~db.Simulation.Date])
    # dataset = db(db.Simulation.Owner==auth.user)
    dataset = db((db.Simulation.id==db.Log.Simulation) & (db.Simulation.id==db.Plot.Simulation) & (db.Simulation.Owner == auth.user))
    scope = TableScope(dataset, db.Simulation.Algorithm, renderstyle=True)
    rows = scope.scoped_dataset.select(db.Simulation.Date,
                                       db.Simulation.Algorithm,
                                       db.Simulation.Input_Data,
                                       db.Simulation.Result,
                                       db.Log.Content,
                                       db.Plot.Plot,
                                       orderby=orderby_selector.orderby())
    headers = {'Simulation.Date': {'selected': True},
               'Simulation.Algorithm': {'selected': False},
               'Simulation.Input_Data': {'selected': False},
               'Simulation.Result': {'selected': False}
    }
    extracolumns = [{'label': A('Log', _href='#'),
                     'content': lambda row, rc: A('Log', _href='download/%s' % row.Log.Content)},
                    {'label': A('Plot', _href='#'),
                     'content': lambda row, rc: A('Plot', _href='download/%s' % row.Plot.Plot)},
                    ]
    columns = [db.Simulation.Date,
               db.Simulation.Algorithm,
               db.Simulation.Input_Data,
               db.Simulation.Result, extracolumns[0]]
    table = SOLIDTABLE(rows,
                       columns=columns,
                       extracolumns=extracolumns,
                       headers=headers,
                       orderby=orderby_selector,
                       renderstyle=True)
    return dict(logged_in=logged_in, sample_1=dict(table=table, scope=scope))


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


