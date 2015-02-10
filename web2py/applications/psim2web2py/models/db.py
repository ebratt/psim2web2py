# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite')
scheduler_db = DAL('sqlite://storage.sqlite')
response.generic_patterns = ['*'] if request.is_local else []

response.static_version = '0.0.1'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
crud, service, plugins = [Crud(db), Crud(scheduler_db)], Service(), PluginManager()

auth = Auth(db)
# service = Service()
# plugins = PluginManager()

auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
