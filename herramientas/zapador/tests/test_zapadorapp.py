#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from zapador.zapadorapp import ZapadorApp


class TestZapadorApp(unittest.TestCase):
    """TestCase for ZapadorApp.
    """
    def setUp(self):
        self.app = ZapadorApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'zapador')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
