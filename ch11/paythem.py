import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Testing paying the person."""

# Since we're using numbers, don't quote 20000
    def setUp(self):
        first = 'tim'
        last = 'timson'
        salary = 20000
        self.ttimson = Employee(first, last, salary)

# Should have paid attention here.
# "test_" is critical, it lets python know you're doing a test.
# It won't test unless your method begins with that.
    def test_give_them_default_raise(self):
        self.ttimson.give_raise(amount=5000)
        self.assertEqual(self.ttimson.salary, 25000)

unittest.main()
