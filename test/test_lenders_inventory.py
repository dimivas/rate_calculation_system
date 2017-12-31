import unittest
import uuid

from lenders_inventory import map_lender_to_uuid, map_uuid_to_lender


class LendersInventoryTestSuite(unittest.TestCase):

    def test_map_lender_to_uuid(self):
        test_lender_id = "test_lender"
        test_lender_uuid = map_lender_to_uuid(test_lender_id)

        self.assertIsInstance(test_lender_uuid, uuid.UUID)
        self.assertEqual(test_lender_uuid, map_lender_to_uuid(test_lender_id))

    def test_map_uuid_to_lender_invalid(self):
        with self.assertRaises(ValueError):
            map_uuid_to_lender(uuid.uuid4())

    def test_map_uuid_to_lender_valid(self):
        test_lender_id = "test_lender"
        test_lender_uuid = map_lender_to_uuid(test_lender_id)

        self.assertEqual(test_lender_id, map_uuid_to_lender(test_lender_uuid))