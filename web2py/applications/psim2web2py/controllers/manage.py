# coding: utf8
import datetime
from gluon.contrib.simplejson import loads, dumps

sw = scheduler_db.scheduler_worker
sr = scheduler_db.scheduler_run
st = scheduler_db.scheduler_task


def clear_all():

    sw = scheduler_db.scheduler_worker
    sr = scheduler_db.scheduler_run
    st = scheduler_db.scheduler_task

    swstatus = scheduler_db(sw.id>0).delete()
    srstatus = scheduler_db(sr.id>0).delete()
    ststatus = scheduler_db(st.id>0).delete()

    btn_status = '#' + request.cid.replace('_cleara', '_status')
    btn_queue = '#' + request.cid.replace('_cleara', '_queue')
    cont = '#' + request.cid.replace('_cleara', '_status_container')

    response.js = "$('%s').removeClass('disabled');$('%s').removeClass('disabled');$('%s').removeClass('w2p_component_stop');" % (btn_status, btn_queue, cont)
    response.flash = "Cleared correctly"


def worker1():
    scheduler.queue_task(floating_point_add, task_name='floating_point_add')
    response.js = "$('#worker_1_queue').addClass('disabled');"
    response.flash = "Function floating_point_add scheduled"


def enable_workers():
    scheduler.resume()
    response.flash = 'Workers enabled'


def disable_workers():
    scheduler.disable()
    response.flash = 'Workers disabled'


def terminate_workers():
    scheduler.terminate()
    response.flash = 'TERMINATE command sent'


def kill_workers():
    scheduler.kill()
    response.flash = 'KILL command sent'
