import hashlib
from pathlib import Path

path = Path(__file__).parent.parent / "scenarios" / "sample.txt"
digest_path = path.with_suffix(path.suffix + ".sha256")


with path.open("rb") as f:
    data = f.read()
    digest = hashlib.sha256(data).hexdigest()

print(f"SHA-256 of {path}: {digest}")

with digest_path.open("w", encoding="utf-8") as f:
    f.write( digest)

print(f"Saved to : {digest_path}")