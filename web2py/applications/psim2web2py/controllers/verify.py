# coding: utf8
import datetime
from gluon.contrib.simplejson import loads, dumps

sw = scheduler_db.scheduler_worker
sr = scheduler_db.scheduler_run
st = scheduler_db.scheduler_task


def worker1():
    q = st.task_name == 'floating_point_add'
    try:
        info = scheduler.task_status(q, output=True)
        res = [
            ("task status completed", info.scheduler_task.status == 'COMPLETED'),
            ("task times_run is 1" , info.scheduler_task.times_run == 1),
            ("scheduler_run record is COMPLETED " , info.scheduler_run.status == 'COMPLETED')
        ]
    except:
        res = [("Wait a few seconds and retry the 'verify' button", False)]
    response.view = 'default/verify.load'
    return dict(res=res)
