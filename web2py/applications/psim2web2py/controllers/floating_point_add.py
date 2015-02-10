# -*- coding: utf-8 -*-
from gluon.storage import Storage

response.files.append(URL('static', 'css/prettify.css'))
response.files.append(URL('static', 'js/prettify.js'))

def index():
    steps = [
        'floating_point_add'
        ]
    return dict(steps=steps)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def tasks():
    steps = [
        'floating_point_add'
        ]
    docs = Storage()
    comments = Storage()
    docs.floating_point_add = """
#### Floating Point Example
provide the number of processing nodes and the
size of the vector of random numbers

example taken from section 2.2.5 of An Introduction to Parallel
Programming Peter S. Pacheco University of San Francisco
Pacheco, Peter (2011-02-17). An Introduction to Parallel Programming
Elsevier Science. Kindle Edition.

``
scheduler.queue_task(floating_point_add, task_name='floating_point_add')
``:python

Instructions:
 - Push "Clear All"
 - Push "Start Monitoring"
 - If not yet, start a worker in another shell ``web2py.py -K w2p_scheduler_tests``
 - Wait a few seconds, a worker shows up
 - Push "Queue Task"
 - Wait a few seconds

What you should see:
 - one worker is **ACTIVE**
 - one scheduler_task gets **QUEUED**, goes into **RUNNING** for a while and then becomes **COMPLETED**
 - when the task is **RUNNING**, a scheduler_run record pops up (**RUNNING**)
 - When the task is **COMPLETED**, the scheduler_run record is updated to show a **COMPLETED** status.

Than, click "Stop Monitoring" and "Verify"
    """
    comments.floating_point_add = """
Thanks for scheduling this task!s
"""
    return dict(docs=docs, comments=comments)

