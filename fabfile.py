from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/dismalstarshine/blog.git"
env.user = 'zimoli'
env.password = 'uselinux'
env.hosts = ['www.bzxhn.ml']
env.port = '27075'


def deploy():
    source_folder = '/home/zimoli/sites/www.bzxhn.ml/blog'
    run('cd %s && git pull' % source_folder)
    run("""
    cd {} &&
    ../env/bin/pip install -r requirements.txt &&
    ../env/bin/python3 manage.py collectstatic --noinput &&
    ../env/bin/python3 manage.py migrate
    """.format(source_folder))
    #run('gunicorn --bind unix:/tmp/www.bzxhn.ml.socket blogproject.wsgi:application')
    sudo('service nginx reload')
