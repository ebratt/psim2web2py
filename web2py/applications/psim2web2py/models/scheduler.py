# coding: utf8
import time
from gluon.scheduler import Scheduler
import subprocess
import os

def demo1(*args,**vars):
    print 'you passed args=%s and vars=%s' % (args, vars)
    time.sleep(5)
    print '50%'
    time.sleep(5)
    print '!clear!100%'
    return dict(a=1, b=2)


def floating_point_add(*args, **vars):
    module_folder = os.path.join(request.folder, 'modules/')
    private_folder = os.path.join(request.folder, 'private/')
    status = subprocess.call([module_folder + 'floating_point_add.sh', module_folder, private_folder])
    return dict(status=status)

# scheduler_db.scheduler_task.drop()
scheduler = Scheduler(scheduler_db)