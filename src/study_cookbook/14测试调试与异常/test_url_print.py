# -*- coding: utf-8 -*-
from 测试stdout输出 import url_print
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = "http"
        host = "www"
        domain = "example.com"
        expected_url = f"{protocol}://{host}.{domain}"

        with patch("sys.stout", new=StringIO()) as fake_out:
            url_print(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)
