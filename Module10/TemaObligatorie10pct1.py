import unittest

from Context_menu import TestContext
from Alerts import TestAlerts
from Prompt import TestLogin
from Tema_Obligatorie9 import TestLogIn
import HtmlTestRunner


class MyTestSuites(unittest.TestCase):

    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContext),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogIn),

        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Report1', report_name='smoke Test', combine_reports=True
        )
        runner.run(smoketest)
