from unittest import TestCase
from chalicelib.hashing import hash_ssn


class HashSSNTestCase(TestCase):
    def test_hashing_ssn(self) -> None:
        hashed = hash_ssn('121290-123A')
        expected_hash = 'bc1143880b42b8378cb08385fe193f2d205965f05dbd7e9f26c56bb66aa9a49f80393688c3f907802250af27f4cc7c0b68f9cd25b898bd8d1f718de6314d8fe6'  # pylint: disable=E501
        self.assertEqual(hashed, expected_hash)
