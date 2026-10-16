# Patch to disable version and environment in runcellpose
from pathlib import Path

PLUGIN = Path("/opt/CellProfiler-plugins/active_plugins/runcellpose.py")

text = PLUGIN.read_text()

replacements = {
    "choices=['omnipose', 'v2', 'v3', 'v4']":
        "choices=['v3']",

    'choices=["Docker", "Podman", "Python"]':
        'choices=["Python"]',

    'value="Docker"':
        'value="Python"',
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f"Expected text not found: {old}")

    text = text.replace(old, new)

PLUGIN.write_text(text)

print("RunCellpose patched successfully")
