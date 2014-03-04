from path import path

from clld.tests.util import TestWithApp

import sails


class Tests(TestWithApp):
    __cfg__ = path(sails.__file__).dirname().joinpath('..', 'development.ini').abspath()
    __setup_db__ = False

    def test_home(self):
        res = self.app.get('/', status=200)
