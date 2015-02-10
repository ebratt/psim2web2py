# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('psim', SPAN(2), 'web', SPAN(2), 'py'),
                  _class="brand", _href=URL('default', 'index'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = HTML('PSIM is a ', I('P'), 'arallel algorithm ', I('SIM'), 'ulator')
## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Eric Bratt <eric_bratt@yahoo.com>'
response.meta.description = 'Simulate parallel algorithm processing with psim2web2py'
response.meta.keywords = 'web2py, python, framework, psim'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2015'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    ('Home', False, URL('default', 'index'), []),
    ('Tasks', False, None, [
        ('Floating Point Add', False, URL('floating_point_add', 'tasks', anchor='floating_point_add')),
        ])
]