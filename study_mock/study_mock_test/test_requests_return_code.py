# -*-coding:utf-8 -*-

import unittest
import mock
from study_mock.study_mock_common import request_status_code


class TestReturnCode(unittest.TestCase):
    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        request_status_code.send_request = success_send
        self.assertEqual(request_status_code.visit_tack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        request_status_code.send_request = fail_send
        self.assertEqual(request_status_code.visit_tack(), '404')


if __name__ == "__main__":
    unittest.main()
