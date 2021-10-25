import unittest
from admin.admin_interface_backend import Adminbackend
from staff.staff_interface_backend import Staffbackend
from admin.connection import MyDatabase

class MyTest(unittest.TestCase):
    admin_backend=Adminbackend()
    staff_backend=Staffbackend()


    def test_add_services(self):
        result = self.admin_backend.service_add('test_item', 'test_type',"100","test_availability","test_prescription")
        self.assertTrue(result)

    def test_add_services_priceistext(self):
        result = self.admin_backend.service_add('test_item', 'test_type', "test_price","test_availability","test_prescription")
        self.assertFalse(result)

    def test_add_services_single_emptydata(self):
        result = self.admin_backend.service_add('test_item', '', "test_price","test_availability","test_prescription")
        self.assertFalse(result)

    def test_add_services_entire_emptydata(self):
        result = self.admin_backend.service_add("","", "","","")
        self.assertFalse(result)

    def test_show_service_datas(self):
        data = self.admin_backend.service_backend_showdata()
        actual_result = len(data)
        expected_result = 14
        self.assertEqual(expected_result, actual_result)

    def test_search_services(self):
        data = self.admin_backend.return_service_search_data('X-ray','Service_name')
        actual_result = len(data)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_delete_Services(self):
        result=self.admin_backend.delete_services(16)
        self.assertTrue(result)

    def test_check_admin_login_empty_data(self):
        result=self.admin_backend.check_login("","")
        self.assertFalse(result)

    def test_check_admin_login(self):
        result = self.admin_backend.check_login("test", "test")
        self.assertFalse(result)

    def test_check_admin_login_realdata(self):
        result = self.admin_backend.check_login("admin", "admin1234")
        self.assertTrue(result)


        