import unittest
from service_calc import calculate_technician_fee

class TestTechnicianBilling(unittest.TestCase):
    
    def test_standard_visit(self):
        self.assertEqual(calculate_technician_fee(2, False), 2100)

    def test_emergency_visit(self):
        self.assertEqual(calculate_technician_fee(1, True), 2300)

    def test_invalid_negative_hours(self):
        with self.assertRaises(ValueError):
            calculate_technician_fee(-1, False)

if __name__ == '__main__':
    unittest.main()