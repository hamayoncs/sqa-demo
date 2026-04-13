import unittest
from service_calc import calculate_technician_fee
#unit tests
class TestTechnicianBilling(unittest.TestCase):
    
    def test_standard_visit(self):
        # base_visit_fee(500) + hours(2) * hourly_rate(800) = 2100
        self.assertEqual(calculate_technician_fee(2, False), 2100)

    def test_emergency_visit(self):
        # base_visit_fee(500) + hours(1) * hourly_rate(800) + emergency_surcharge(1000) = 2300
        self.assertEqual(calculate_technician_fee(1, True), 2300)

    def test_invalid_negative_hours(self):
        # negative hours are invalid, function should raise ValueError
        with self.assertRaises(ValueError):
            calculate_technician_fee(-1, False)

if __name__ == '__main__':
    unittest.main()

    