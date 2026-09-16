#!/usr/bin/env python3
"""
Régénère images/manifest.json à partir des fichiers images présents
dans le dossier images/.
Usage :  python generate_manifest.py
"""
import json
import os
import sys

IMAGES_DIR = "images"
MANIFEST   = os.path.join(IMAGES_DIR, "manifest.json")
EXTS       = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"}


def main():
    if not os.path.isdir(IMAGES_DIR):
        print(f"❌ Dossier '{IMAGES_DIR}/' introuvable. Créez-le d'abord.")
        sys.exit(1)

    files = sorted(
        f for f in os.listdir(IMAGES_DIR)
        if os.path.splitext(f)[1].lower() in EXTS
    )

    data = {"images": files}

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

    print(f"✅ {len(files)} image(s) écrite(s) dans {MANIFEST}")
    for f in files:
        print("   •", f)


if __name__ == "__main__":
    main()