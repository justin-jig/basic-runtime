# 41_file_chunking_and_zip.py
# 파일 분할/병합 + ZIP 압축/해제

from zipfile import ZipFile, ZIP_DEFLATED
import os

# ------------------------------------------------------------
# 1) 바이너리 파일 분할 (기본 3MB 청크)
# ------------------------------------------------------------
def split_file(filename, subsize=1024 * 1024 * 3):
    suffix = 0
    with open(filename, 'rb') as f:
        buf = f.read(subsize)
        while buf:
            subfilename = f'{filename}_{suffix}'
            with open(subfilename, 'wb') as h:
                h.write(buf)
            print(f'[{subfilename}] 완료')
            buf = f.read(subsize)
            suffix += 1
    return suffix  # 생성된 조각 수

# ------------------------------------------------------------
# 2) 분할 파일 병합
# ------------------------------------------------------------
def merge_files(base_filename, parts, outname='merged.bin', buflen=256 * 1024):
    with open(outname, 'wb') as out:
        for i in range(parts):
            chunk = f'{base_filename}_{i}'
            print(f'[{chunk}] 합치는 중..')
            with open(chunk, 'rb') as h:
                buf = h.read(buflen)
                while buf:
                    out.write(buf)
                    buf = h.read(buflen)
    print('[병합 완료] →', outname)

# ------------------------------------------------------------
# 3) 단일 파일 ZIP 압축
# ------------------------------------------------------------
def compress_zip(zipname, filename):
    print(f'[{filename}] -> [{zipname}] 압축...')
    with ZipFile(zipname, 'w', compression=ZIP_DEFLATED) as ziph:
        ziph.write(filename, arcname=os.path.basename(filename))
    print('압축이 끝났습니다.')

# ------------------------------------------------------------
# 4) 폴더 전체 ZIP 압축 (상대 경로 보존)
# ------------------------------------------------------------
def compress_folder(zipname, folder):
    print(f'[{folder}] -> [{zipname}] 압축...')
    with ZipFile(zipname, 'w', compression=ZIP_DEFLATED) as ziph:
        for dirname, _, files in os.walk(folder):
            for file in files:
                full = os.path.join(dirname, file)
                arc = os.path.relpath(full, start=folder)
                ziph.write(full, arcname=os.path.join(os.path.basename(folder), arc))
    print('폴더 압축이 끝났습니다.')

# ------------------------------------------------------------
# 5) ZIP 해제
# ------------------------------------------------------------
def extract_zip(zipname, outdir='.'):
    with ZipFile(zipname, 'r') as ziph:
        ziph.extractall(outdir)
    print(f'[{zipname}]가 [{outdir}] 아래에 성공적으로 추출되었습니다.')

# ==========================
# 데모 (필요 시 주석 해제)
# ==========================
if __name__ == '__main__':
    # 1) 분할
    base = 'python-3.5.2.exe'
    if os.path.exists(base):
        parts = split_file(base, subsize=1024 * 1024 * 3)  # 3MB
        # 2) 병합
        merge_files(base, parts, outname='ret.exe')

    # 3) 단일 파일 압축
    filename = 'mydata.txt'
    if os.path.exists(filename):
        compress_zip(filename + '.zip', filename)

    # 4) 폴더 압축
    folder = 'tmp'
    if os.path.isdir(folder):
        compress_folder(folder + '.zip', folder)

    # 5) 해제
    if os.path.exists('tmp.zip'):
        extract_zip('tmp.zip')
