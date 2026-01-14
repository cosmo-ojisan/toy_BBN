# Answer verification module (obfuscated)
import hashlib as _h
import base64 as _b

def _v(x, k):
    """Verify answer against encoded key."""
    if x is None:
        return False
    s = str(x).strip().upper()
    return _h.sha256(s.encode()).hexdigest()[:16] == k

def _n(x, t, e=0.01):
    """Verify numeric answer."""
    try:
        return abs(float(x) - t) < e
    except:
        return False

def _c(x, k):
    """Check answer."""
    return _v(x, k)

# Pre-computed hashes (sha256[:16])
# O -> 4f -> hash
# X -> 58 -> hash
# A -> 41 -> hash
# B -> 42 -> hash
# C -> 43 -> hash
# TRUE -> hash
# FALSE -> hash

_O = "44bd7ae60f478fab"  # O
_X = "02c3a5d7e8b2a3f1"  # X - computed
_A = "559aead08264d5ba"  # A
_B = "df7e70e521544494"  # B
_C = "6b23c0d5f35d1b11"  # C
_T = "b326b5062b2f0e69"  # TRUE
_F = "bc9a3f8d85e3b89e"  # FALSE

# Recompute hashes
import hashlib
_O = hashlib.sha256("O".encode()).hexdigest()[:16]
_X = hashlib.sha256("X".encode()).hexdigest()[:16]
_A = hashlib.sha256("A".encode()).hexdigest()[:16]
_B = hashlib.sha256("B".encode()).hexdigest()[:16]
_C = hashlib.sha256("C".encode()).hexdigest()[:16]
_T = hashlib.sha256("TRUE".encode()).hexdigest()[:16]
_F = hashlib.sha256("FALSE".encode()).hexdigest()[:16]
