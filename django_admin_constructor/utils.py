from django.core.management import call_command

def create_migrations_for_dynamic_model(model_class):

    app_name = 'DjangoAdminConstructor'

    call_command('makemigrations', app_name)

    call_command('migrate', app_name)
