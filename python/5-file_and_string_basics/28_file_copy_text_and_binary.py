# 28_file_copy_text_and_binary.py
"""
텍스트/바이너리 파일 복사 스니펫 모음

- copy_text(src, dst, encoding='utf-8'):
    텍스트 파일을 한 번에 읽어 쓰는 간단 복사 (줄바꿈/인코딩 유지)
- copy_binary(src, dst, bufsize=256*1024):
    대용량 이진 파일을 버퍼 단위로 안전하게 복사
- verify_copy(src, dst, mode='size'|'hash'):
    크기 또는 해시(MD5)로 복사 검증

* 참고: shutil.copy2 를 사용하면 메타데이터까지 복사 가능하지만,
  학습 목적으로 수동 복사(버퍼 루프)를 예시로 포함했습니다.
"""

from __future__ import annotations
import os
import hashlib
from typing import Literal

# -----------------------------
# 유틸: 디렉터리 보장 & 사람친화적 바이트 표기
# -----------------------------
def ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)

def human_size(n: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    v = float(n)
    while v >= 1024 and i < len(units) - 1:
        v /= 1024.0
        i += 1
    return f"{v:.2f}{units[i]}"

# -----------------------------
# 텍스트 파일 복사
# -----------------------------
def copy_text(src: str, dst: str, encoding: str = "utf-8") -> None:
    """
    텍스트 파일을 통째로 읽어 그대로 기록.
    * 매우 큰 파일은 권장하지 않음 (메모리에 모두 적재)
    """
    if not os.path.isfile(src):
        raise FileNotFoundError(f"소스 파일 없음: {src}")

    ensure_parent_dir(dst)

    with open(src, "r", encoding=encoding, newline="") as f_src:
        data = f_src.read()

    with open(dst, "w", encoding=encoding, newline="") as f_dst:
        f_dst.write(data)

    print(f"[TEXT] {src} → {dst} 복사 완료 (encoding={encoding})")

# -----------------------------
# 바이너리 파일 복사 (버퍼 루프)
# -----------------------------
def copy_binary(src: str, dst: str, bufsize: int = 256 * 1024) -> None:
    """
    이진 파일을 버퍼 단위로 안전 복사.
    * bufsize 기본 256KB (대용량이면 1~4MB 권장)
    """
    if not os.path.isfile(src):
        raise FileNotFoundError(f"소스 파일 없음: {src}")

    ensure_parent_dir(dst)

    total = 0
    with open(src, "rb") as f_src, open(dst, "wb") as f_dst:
        chunk = f_src.read(bufsize)
        while chunk:
            f_dst.write(chunk)
            total += len(chunk)
            chunk = f_src.read(bufsize)

    print(f"[BINARY] {src} → {dst} 복사 완료 ({human_size(total)}, buf={human_size(bufsize)})")

# -----------------------------
# 검증: 크기 또는 해시
# -----------------------------
def md5sum(path: str, bufsize: int = 256 * 1024) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        chunk = f.read(bufsize)
        while chunk:
            h.update(chunk)
            chunk = f.read(bufsize)
    return h.hexdigest()

def verify_copy(
    src: str,
    dst: str,
    mode: Literal["size", "hash"] = "size",
) -> bool:
    if not (os.path.isfile(src) and os.path.isfile(dst)):
        print("[VERIFY] 소스 또는 대상 파일이 존재하지 않습니다.")
        return False

    if mode == "size":
        s1, s2 = os.path.getsize(src), os.path.getsize(dst)
        ok = (s1 == s2)
        print(f"[VERIFY:size] {human_size(s1)} vs {human_size(s2)} → {'OK' if ok else 'MISMATCH'}")
        return ok

    if mode == "hash":
        h1, h2 = md5sum(src), md5sum(dst)
        ok = (h1 == h2)
        print(f"[VERIFY:hash] {h1} vs {h2} → {'OK' if ok else 'MISMATCH'}")
        return ok

    raise ValueError("mode 는 'size' 또는 'hash' 중 하나여야 합니다.")

# -----------------------------
# 데모 실행 (직접 실행 시)
# -----------------------------
if __name__ == "__main__":
    # 예시 1) 텍스트 복사
    # copy_text("mydata.txt", "backup/mydata_copy.txt")
    # verify_copy("mydata.txt", "backup/mydata_copy.txt", mode="size")

    # 예시 2) 바이너리 복사 (버퍼 1MB)
    # copy_binary("img_sample.jpg", "backup/img_sample_copy.jpg", bufsize=1024*1024)
    # verify_copy("img_sample.jpg", "backup/img_sample_copy.jpg", mode="hash")

    print(
        "이 스크립트는 import 해서 함수 호출하거나, 위의 예시 주석을 해제하고 직접 실행하세요."
    )
