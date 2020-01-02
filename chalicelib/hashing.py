import hashlib


def hash_ssn(ssn: str) -> str:
    """
    Return a hashed hex of a an ssn
    """
    ssn_bytes = str.encode(ssn)
    hex_hashed_ssn = hashlib.sha512(ssn_bytes).hexdigest()
    return hex_hashed_ssn
