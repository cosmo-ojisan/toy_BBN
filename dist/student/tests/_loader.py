# Test loader module (obfuscated)
import base64 as _b
import zlib as _z
import pickle as _p

def _d(s):
    """Decode test data."""
    return _p.loads(_z.decompress(_b.b64decode(s)))

def _e(obj):
    """Encode test data (for generation only)."""
    return _b.b64encode(_z.compress(_p.dumps(obj))).decode()
