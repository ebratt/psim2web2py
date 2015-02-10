# -*- coding: utf-8 -*-


def get_status():
    sw = scheduler_db.scheduler_worker
    sr = scheduler_db.scheduler_run
    st = scheduler_db.scheduler_task

    swstatus = scheduler_db(sw.id>0).select()

    srstatus = scheduler_db(sr.id>0).select()

    ststatus = scheduler_db(st.id>0).select()

    return dict(swstatus=swstatus, srstatus=srstatus, ststatus=ststatus)
