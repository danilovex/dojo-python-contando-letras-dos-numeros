import unittest
import test_unittest
suite = unittest.TestLoader().loadTestsFromModule(test_unittest)
unittest.TextTestRunner(verbosity=2).run(suite)