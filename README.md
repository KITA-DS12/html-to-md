# HTML to Markdown

このプロジェクトは、HTMLファイルをMarkdown形式に変換するツールです。また、ファイル連結機能も備えています。

## 機能

### HTML to Markdown 変換
- 指定したディレクトリ内のHTMLファイルをMarkdown形式に変換
- `markdownify`ライブラリを使用してHTMLコンテンツをMarkdownに変換

### ファイル連結
- 指定したディレクトリ内のすべてのファイルを1つのファイルに連結
- ファイルはアルファベット順にソートされて連結
- 各ファイルの内容の前にファイル名がヘッダーとして追加
- UTF-8エンコーディングをサポート

## 必要条件

- Python 3.8以上
- Rye（依存関係管理用）

## インストール

依存関係を同期するには、以下のコマンドを実行してください：

```bash
rye sync
```

## 使い方

### HTML to Markdown 変換

```bash
# HTMLファイルをMarkdownに変換
make convert DIR=path/to/your/directory

# 変換済みファイルを削除
make clean DIR=path/to/your/directory
```

### ファイル連結

```bash
# 指定したディレクトリ内のファイルを連結
make concat INPUT_DIR=path/to/directory OUTPUT_FILE=result.md
```

### 使用例

```bash
# HTMLをMarkdownに変換
make convert DIR=docs/articles

# 変換したファイルを削除
make clean DIR=docs/articles

# ファイルを連結
make concat INPUT_DIR=docs/articles OUTPUT_FILE=combined_articles.md
```

## 出力例

### ファイル連結の出力形式

連結されたファイルは以下のような形式になります：

```markdown
# File: document1.md

（document1.mdの内容）

# File: document2.md

（document2.mdの内容）
```

## エラーハンドリング

- 指定されたディレクトリが存在しない場合はエラーメッセージを表示
- ファイル読み込み/変換時にエラーが発生した場合は警告メッセージを表示して処理を継続

## コマンド一覧

すべての利用可能なコマンドを表示するには：

```bash
make help
```