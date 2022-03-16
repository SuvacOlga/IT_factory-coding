import unittest
import HtmlTestRunner

from src.part_2_automation import test_auth, context_menu, multitab


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_auth.Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(context_menu.ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(multitab.Multitab)

        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
