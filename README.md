# HTML to Markdown

このプロジェクトは、指定されたディレクトリ内のHTMLファイルをMarkdown形式に変換するツールです。`markdownify`ライブラリを使用して、HTMLコンテンツをMarkdownに変換します。

## 目次

- [インストール](#インストール)
- [使い方](#使い方)
- [コマンド](#コマンド)
- [ライセンス](#ライセンス)

## インストール

このプロジェクトを使用するには、Python 3.8以上が必要です。Ryeを使用して依存関係を同期するには、以下のコマンドを実行してください。

```bash
rye sync
```

## 使い方

HTMLファイルをMarkdownに変換するには、以下のコマンドを実行します。

```bash
make convert DIR=<directory>
```

ここで、`<directory>`はHTMLファイルが格納されているディレクトリのパスです。

### 例

```bash
make convert DIR=path/to/your/directory
```

## コマンド

- `make help`
  - 使用可能なコマンドとその使用方法を表示します。

- `make convert DIR=<directory>`
  - 指定したディレクトリ内のHTMLファイルをMarkdownに変換します。

- `make clean DIR=<directory>`
  - 指定したディレクトリ内のmarkdownフォルダを削除します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
