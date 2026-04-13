import unittest
from service_calc import calculate_technician_fee

class TestTechnicianBilling(unittest.TestCase):
    
    def test_standard_visit(self):
        # 2 hours standard: 500 + (2 * 800) = 2100
        self.assertEqual(calculate_technician_fee(2, False), 2100)

    def test_emergency_visit(self):
        # 1 hour emergency: 500 + (1 * 800) + 1000 = 2300
        self.assertEqual(calculate_technician_fee(1, True), 2300)

    def test_invalid_negative_hours(self):
        # The system must block negative time logging
        with self.assertRaises(ValueError):
            calculate_technician_fee(-1, False)

if __name__ == '__main__':
    unittest.main()