#!/usr/bin/env python3
import pathlib
import sys

out_dir = pathlib.Path("out/arch/arm64/boot")
img_path = out_dir / "Image.gz"
if not img_path.exists():
    sys.exit(f"Image.gz not found at {img_path}")

img = img_path.read_bytes()
pad = (4 - (len(img) % 4)) % 4
out = bytearray(img + b"\x00" * pad)

print(f"Base Image.gz: {len(img)} bytes, pad={pad} bytes -> DTB start offset={len(out)} (aligned={len(out) % 4 == 0})")

dtb_dir = out_dir / "dts/samsung"
for name in ["r04", "r02", "r00", "r05"]:
    dtb_file = dtb_dir / f"msm8996-sec-gts3llte-eur-kor-{name}.dtb"
    if not dtb_file.exists():
        sys.exit(f"Missing DTB: {dtb_file}")
    dtb = dtb_file.read_bytes()
    print(f"Appending DTB {name}: {len(dtb)} bytes at offset {len(out)}")
    out.extend(dtb)

out_file = out_dir / "Image.gz-dtb"
out_file.write_bytes(out)
print(f"Successfully generated {out_file}: {len(out)} bytes total with 4 DTBs!")
