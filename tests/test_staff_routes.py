import unittest
from app import create_app, db
from app.models.staff import Staff
from flask import url_for
# from sqlalchemy import text


class StaffRoutesTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database"""
        self.app = create_app('testing')  # Set up testing configurations
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create the database, schemas and tables
        # with self.app_context:
        #     with db.engine.connect() as connection:
        #         connection.execute(text("CREATE SCHEMA IF NOT EXISTS dev;"))
        #         connection.execute(text("CREATE SCHEMA IF NOT EXISTS aud;"))
        db.create_all()

        # Add sample staff member
        staff = Staff(name='Test Person', role='manager', email='test.person@example.com')
        db.session.add(staff)
        db.session.commit()

    def tearDown(self):
        """Tear down the database after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_staff_list(self):
        """Test retrieving the list of staff members"""
        response = self.client.get(url_for('staff.get_staff_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Person', str(response.data))

    def test_get_staff_by_id(self):
        """Test retrieving of staff by ID"""
        staff = Staff.query.first()
        response = self.client.get(url_for('staff.get_staff', staff_id=staff.staff_id))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Person', str(response.data))

    def test_get_staff_by_invalid_id(self):
        """Test retrieving a staff member with an invalid ID"""
        response = self.client.get(url_for('staff.get_staff', staff_id=999))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Staff member not found', str(response.data))

    # API Responses (Format & Status Codes)
    def test_api_response_time(self):
        response = self.client.get(url_for('staff.get_staff_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    # Performance Testing (Load Testing and Response Time)
    def test_response_time(self):
        with self.client as client:
            import time
            start_time = time.time()
            response = client.get(url_for('staff.get_staff_list'))
            end_time = time.time()
            self.assertTrue(end_time - start_time < 1)  # Response should be under 1 second.

    # Security (SQL Injection and XSS)
    def test_sql_injection(self):
        malicious_input = "'; DROP TABLE dev.staff; --"
        response = self.client.post(url_for('staff.create_staff'), data={'name': malicious_input})
        self.assertEqual(response.status_code, 400)  # Bad request.

    # Integration Testing



if __name__ == '__main__':
    unittest.main()
