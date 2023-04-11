import os
import glob
from ase.io import read, write

def rmc6f2xyz(directory):
    """指定されたディレクトリ内から最新の.rmc6fファイルを探し、xyz形式に変換する"""
    # 指定されたディレクトリ内から.rmc6fファイルを探す
    rmc6f_files = glob.glob(os.path.join(directory, '*.rmc6f'))
    if not rmc6f_files:
        print('存在しません')
        return

    # 最新の.rmc6fファイルを選択する
    latest_rmc6f = max(rmc6f_files, key=os.path.getctime)

    # ASEフレームワークを使用して、rmc6fファイルから直接xyz形式に変換する
    atoms = read(latest_rmc6f, format='rmc6f')
    stem = os.path.splitext(os.path.basename(latest_rmc6f))[0]
    xyz_file = f'{stem}.xyz'
    write(xyz_file, atoms)
    print(f'変換されたファイル: {xyz_file}')

# Example usage:
rmc6f2xyz('/path/to/directory')