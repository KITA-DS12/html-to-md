.PHONY: help convert clean

help:
	@echo "使用可能なコマンド:"
	@echo "  make convert DIR=<directory>  - 指定したディレクトリ内のHTMLファイルをMarkdownに変換"
	@echo "  make clean DIR=<directory>    - 指定したディレクトリ内のmarkdownフォルダを削除"
	@echo "  make help                     - このヘルプメッセージを表示"
	@echo ""
	@echo "例:"
	@echo "  make convert DIR=path/to/your/directory"
	@echo "  make clean DIR=path/to/your/directory"

convert:
ifndef DIR
	@echo "エラー: DIRパラメータが必要です"
	@echo "使用例: make convert DIR=path/to/your/directory"
else
	python src/html_to_md/html_to_markdown.py $(DIR)
endif

clean:
ifndef DIR
	@echo "エラー: DIRパラメータが必要です"
	@echo "使用例: make clean DIR=path/to/your/directory"
else
	rm -rf $(DIR)/markdown
	@echo "$(DIR)/markdownフォルダを削除しました"
endif 
