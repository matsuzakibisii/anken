#!/usr/bin/env python3
"""ANKENブログ 画像最適化スクリプト
blog/images/ 内の未変換PNGを2サイズのWebPに変換する。
  img-X1-hero.png -> img-X1-hero.webp       (最大1200px幅 / 記事ページ表示用)
                  -> img-X1-hero-thumb.webp (最大900px幅  / media.html・index.html一覧用)
新記事のヒーロー画像を images/ に保存したあと、このスクリプトを実行するだけでよい。
  python3 blog/optimize-images.py
既に変換済みのものはスキップする（--force で再変換）。
"""
import os, glob, sys
from PIL import Image

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"))
force = "--force" in sys.argv
done = 0
for f in sorted(glob.glob("*.png")):
    base = f[:-4]
    big, thumb = base + ".webp", base + "-thumb.webp"
    if not force and os.path.exists(big) and os.path.exists(thumb):
        continue
    im = Image.open(f).convert("RGB")
    a = im.copy(); a.thumbnail((1200, 1200), Image.LANCZOS); a.save(big, "WEBP", quality=80, method=6)
    b = im.copy(); b.thumbnail((900, 900), Image.LANCZOS); b.save(thumb, "WEBP", quality=78, method=6)
    print(f"{f} {os.path.getsize(f)//1024}KB -> {os.path.getsize(big)//1024}KB / {os.path.getsize(thumb)//1024}KB")
    done += 1
print(f"変換 {done} 件" if done else "未変換のPNGはありません")
