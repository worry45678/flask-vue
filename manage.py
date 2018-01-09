#!/usr/bin/env python
import os
from app import create_app, db
from app.models import tblUser, tblRole
from flask_script import Manager, Shell


app = create_app(os.getenv('PYTHON_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, tblUser=tblUser,tblRole=tblRole)


manager.add_command("shell", Shell(make_context=make_shell_context))

# manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
