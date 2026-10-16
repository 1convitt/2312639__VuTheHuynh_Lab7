import unittest
from unittest.mock import patch

import gps_service
from yummy_app import YummyApp


class TestEasyLevel(unittest.TestCase):
    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total_for_single_item(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 2}), 100000)

    def test_calculate_total_for_multiple_items(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 1, "bun": 1}), 95000)

    def test_calculate_total_for_empty_cart(self):
        self.assertEqual(self.app.calculate_order_total({}), 0.0)

    def test_calculate_total_with_zero_quantity(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 0}), 0.0)

    def test_unknown_item_and_negative_quantity(self):
        self.assertEqual(self.app.calculate_order_total({"unknown": 2, "bun": -1}), 0)

    def test_com_price(self):
        self.assertEqual(self.app.calculate_order_total({"com": 2}), 60000)


class TestMediumLevel(unittest.TestCase):
    def test_online_valid_promo(self):
        self.assertAlmostEqual(YummyApp().apply_promo_code(100000, "GIAM10"), 90000)

    def test_offline_raises_connection_error(self):
        app = YummyApp(network_status="offline")
        with self.assertRaisesRegex(ConnectionError, "Khong co ket noi mang"):
            app.apply_promo_code(100000, "GIAM10")

    def test_special_promo_on_os_15(self):
        self.assertAlmostEqual(
            YummyApp(os_version=15).apply_promo_code(100000, "NEW_OS_ONLY"), 80000
        )

    def test_special_promo_on_os_14(self):
        with self.assertRaisesRegex(ValueError, "HDH phien ban 15"):
            YummyApp(os_version=14).apply_promo_code(100000, "NEW_OS_ONLY")

    def test_invalid_promo(self):
        with self.assertRaisesRegex(ValueError, "khong hop le"):
            YummyApp().apply_promo_code(100000, "INVALID")


class TestHardLevel(unittest.TestCase):
    @patch("yummy_app.gps_service.get_current_location", return_value=(10.0, 105.0))
    def test_gps_in_supported_area(self, mock_gps):
        self.assertEqual(YummyApp().get_nearby_restaurants(), [
            "Nha hang Pho Ly Quoc Su", "Bun cha Huong Lien"
        ])
        mock_gps.assert_called_once_with()

    @patch("yummy_app.gps_service.get_current_location", return_value=(20.0, 110.0))
    def test_gps_outside_supported_area(self, mock_gps):
        self.assertEqual(YummyApp().get_nearby_restaurants(), [])
        mock_gps.assert_called_once_with()

    @patch("yummy_app.gps_service.get_current_location",
           side_effect=gps_service.GPSSignalLostError("GPS lost"))
    def test_gps_signal_lost(self, mock_gps):
        self.assertEqual(YummyApp().get_nearby_restaurants(),
                         "Khong the xac dinh vi tri.")
        mock_gps.assert_called_once_with()


class TestGPSService(unittest.TestCase):
    def test_simulated_default_location(self):
        self.assertEqual(gps_service.get_current_location(), (10.0, 105.0))


if __name__ == "__main__":
    unittest.main()
