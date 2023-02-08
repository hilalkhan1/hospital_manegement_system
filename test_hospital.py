from unittest import TestCase
from hospital import Hospital
from patient import Patient, Investigation
from doctor import Doctor
from nurse import Nurse


class TestPatient(TestCase):

    def setUp(self):
        self.p1 = Patient("Hilal", "21", "Hidayat", "Male", "cardio", "1")
        self.p2 = Patient("Naik", "22", "abc", "M", "ortho", "2")
        self.p3 = Patient("Waqas", "23", "xyz", "Ma", "liver", "3")

        

    def test_patients_id(self):
        self.assertEqual(self.p1.get_id(), "Patient-0")
        self.assertEqual(self.p2.get_id(), "Patient-1")
        self.assertEqual(self.p3.get_id(), "Patient-2")
        
    def test_patients_name(self):
        self.assertEqual(self.p1.get_name(), "Hilal")
        self.assertEqual(self.p2.get_name(), "Naik")
        self.assertEqual(self.p3.get_name(), "Waqas")

    def test_patients_age(self):
        self.assertEqual(self.p1.get_age(), "21")
        self.assertEqual(self.p2.get_age(), "22")
        self.assertEqual(self.p3.get_age(), "23")

    def test_patients_disease(self):
        self.assertEqual(self.p1.get_dieases(), "cardio")
        self.assertEqual(self.p2.get_dieases(), "ortho")
        self.assertEqual(self.p3.get_dieases(), "liver")




class TestDoctor(TestCase):

    def setUp(self):
        self.d1 = Doctor("Ali", "khan", "Male", "cardio")
        self.d2 = Doctor("saeed", "xyz", "Male", "ortho")
        self.d3 = Doctor("abbas", "ali", "Male", "general")

    def test_doc_id(self):
        self.assertEqual(self.d1.get_id(), "Dr-0")
        self.assertEqual(self.d2.get_id(), "Dr-1")
        self.assertEqual(self.d3.get_id(), "Dr-2")

    def test_doc_name(self):
        self.assertEqual(self.d1.get_name(), "Ali")
        self.assertEqual(self.d2.get_name(), "saeed")
        self.assertEqual(self.d3.get_name(), "abbas")
    def test_doc_specility(self):
        self.assertEqual(self.d1.get_specility(), "cardio")
        self.assertEqual(self.d2.get_specility(), "ortho")
        self.assertEqual(self.d3.get_specility(), "general")




class TestNurse(TestCase):

    def setUp(self):
        self.n1 = Nurse("Afzaal", "abc", "Male", "Surgical")
        self.n2 = Nurse("asif", "xyz", "Male", "Medical")
        self.n3 = Nurse("Haroon", "qaz", "Male", "Emergency")


    def test_nurse_id(self):
        self.assertEqual(self.n1.get_id(), "Nurse-0")
        self.assertEqual(self.n2.get_id(), "Nurse-1")
        self.assertEqual(self.n3.get_id(), "Nurse-2")

    def test_nurse_name(self):
        self.assertEqual(self.n1.get_name(), "Afzaal")
        self.assertEqual(self.n2.get_name(), "asif")
        self.assertEqual(self.n3.get_name(), "Haroon")

    def test_nurse_duty(self):
        self.assertEqual(self.n1.get_duty(), "Surgical")
        self.assertEqual(self.n2.get_duty(), "Medical")
        self.assertEqual(self.n3.get_duty(), "Emergency")



class TestInvestigation(TestCase):

    def setUp(self):
        self.i1 = Investigation("CBC", "01-23", "Normal")
        self.i2 = Investigation("X-ray", "02-23", "Fracture",)
        self.i3 = Investigation("CT-scan", "03-23", "Abnormal")

    def test_in_date(self):
        self.assertEqual(self.i1.get_date(), "01-23")
        self.assertEqual(self.i2.get_date(), "02-23")
        self.assertEqual(self.i3.get_date(), "03-23")

    def test_in_type(self):
        self.assertEqual(self.i1.get_invest_type(), "CBC")
        self.assertEqual(self.i2.get_invest_type(), "X-ray")
        self.assertEqual(self.i3.get_invest_type(), "CT-scan")

    def test_in_result(self):
        self.assertEqual(self.i1.get_result(), "Normal")
        self.assertEqual(self.i2.get_result(), "Fracture")
        self.assertEqual(self.i3.get_result(), "Abnormal")
        
        
            
class TestHospital(TestCase):        
        
    def setUp(self):
        self.p = Patient("Hilal", "12", "Hidayat", "Male", "abc", "Dr-0")
        self.d = Doctor("Waqas", "ahmad", "M", "Cardio")
        self.n = Nurse("Waqar", "Waqas", "M", "Surgical")
        self.h = Hospital(100, [])
        
