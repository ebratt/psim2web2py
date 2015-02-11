# -*- coding: utf-8 -*-
import random
import datetime

# db.define_table('Algorithm',
#                 Field('Name', 'string'),
#                 Field('Description', 'text'),
#                 format='%(Name)s')
# # if the Algorithm table is empty, populate it with data
# if db(db.Algorithm).isempty():
#     desc =  "Example taken from section 2.2.5 of An Introduction to Parallel "
#     desc += "Programming Peter S. Pacheco University of San Francisco "
#     desc += "Pacheco, Peter (2011-02-17). An Introduction to Parallel Programming "
#     desc += "Elsevier Science. Kindle Edition."
#     db.Algorithm.insert(Name='floating_point_add',
#                         Description=desc)

db.define_table('Input_Data',
                Field('Value', 'list:string'),
                format='%(Value)s')
if db(db.Input_Data).isempty():
    random.seed(12345)
    db.Input_Data.insert(Value=random.randint(0, 10))
    db.Input_Data.insert(Value=chr(random.randint(97, 122)))
    db.Input_Data.insert(Value=[random.randint(0, 10) for r in xrange(10)])
    db.Input_Data.insert(Value=[chr(random.randint(97, 122)) for r in xrange(97, 122)])

db.define_table('Simulation',
                Field('Date', 'datetime', writable=False, default=datetime.datetime.today()),
                Field('Algorithm', requires=IS_IN_SET([(1, 'Floating Point Add'), (2, 'Merge-Sort'), (3, '2nd Derivative')])),
                Field('Input_Data', 'reference Input_Data'),
                Field('Result', 'string'),
                Field('Owner', 'reference auth_user', default=auth.user_id, readable=False),
                format='%(Date)s-%(Algorithm)s')
_algorithm_options = dict(db.Simulation.Algorithm.requires.options())
db.Simulation.Algorithm.represent = lambda v: _algorithm_options[v]
# db.Simulation.Algorithm.widget = SQLFORM.widgets.autocomplete(
#     request, db.Algorithm.Name, limitby=(0, 10), min_length=2)

db.define_table('Log',
                Field('Simulation', 'reference Simulation'),
                Field('Content', 'upload'),
                Field('Owner', 'reference auth_user', default=auth.user_id),
                format='%(Simulation)')

db.define_table('Plot',
                Field('Simulation', 'reference Simulation'),
                Field('Plot', 'upload'),
                Field('Owner', 'reference auth_user', default=auth.user_id),
                format='%(Simulation)')
