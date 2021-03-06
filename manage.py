import os
import sys
# allows python to know starting point of app and find other folders in app

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from flask_blog import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver",
                    Server(
                        use_debugger=True,
                        use_reloader=True,
                        host=os.getenv('IP', '0.0.0.0'),
                        port=int(os.getenv('PORT', 5000))))

if __name__ == '__main__':
    manager.run()
