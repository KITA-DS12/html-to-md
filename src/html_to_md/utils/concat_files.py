"""
ディレクトリ内のファイルを1つのファイルに連結するユーティリティ
"""

import os
import sys
from pathlib import Path


def concat_files(input_dir: str, output_file: str) -> None:
    """
    指定されたディレクトリ内のすべてのファイルを1つのファイルに連結します。
    
    Args:
        input_dir (str): 入力ディレクトリのパス
        output_file (str): 出力ファイルのパス
    """
    input_path = Path(input_dir)
    
    if not input_path.exists() or not input_path.is_dir():
        print(f"エラー: ディレクトリ '{input_dir}' が存在しないか、ディレクトリではありません。")
        sys.exit(1)
    
    # 出力ファイルを作成
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # ディレクトリ内のすべてのファイルを取得してソート
        files = sorted([f for f in input_path.glob('*') if f.is_file()])
        
        for file_path in files:
            try:
                # ファイル名をヘッダーとして追加
                outfile.write(f"\n\n# File: {file_path.name}\n\n")
                
                # ファイルの内容を読み込んで追加
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    
                print(f"ファイル '{file_path.name}' を連結しました。")
                
            except Exception as e:
                print(f"警告: ファイル '{file_path.name}' の処理中にエラーが発生しました: {str(e)}")


def main():
    """
    コマンドラインからの実行用のメイン関数
    """
    if len(sys.argv) != 3:
        print("使用方法: python -m html_to_md.utils.concat_files <入力ディレクトリ> <出力ファイル>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    concat_files(input_dir, output_file)
    print(f"\n完了: すべてのファイルが '{output_file}' に連結されました。")


if __name__ == "__main__":
    main() 