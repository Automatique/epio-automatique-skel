from fabric.api import local, env

def production():
    env['epioapp'] = 'chummee'

def staging():
    env['epioapp'] = 'chummee' # staging epio instance

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))

def deploy():
    """ An example deploy workflow """
    local("./manage.py collectstatic")
    epio('upload')
    epio('django syncdb')
    epio('django migrate')
    epio('django epio_flush_cache')
