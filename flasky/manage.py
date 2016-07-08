import os,sys
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)

def make_shell_context():
     return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
#manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()
