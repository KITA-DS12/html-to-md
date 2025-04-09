.PHONY: help convert clean concat

help:
	@echo "使用可能なコマンド:"
	@echo "  make convert DIR=<directory>  - 指定したディレクトリ内のHTMLファイルをMarkdownに変換"
	@echo "  make clean DIR=<directory>    - 指定したディレクトリ内のmarkdownフォルダを削除"
	@echo "  make concat INPUT_DIR=<dir> OUTPUT_FILE=<file>  - 指定したディレクトリ内のファイルを連結"
	@echo "  make help                     - このヘルプメッセージを表示"
	@echo ""
	@echo "例:"
	@echo "  make convert DIR=path/to/your/directory"
	@echo "  make clean DIR=path/to/your/directory"
	@echo "  make concat INPUT_DIR=docs/articles OUTPUT_FILE=combined.md"

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

concat:
ifndef INPUT_DIR
	@echo "エラー: INPUT_DIRパラメータが必要です"
	@echo "使用例: make concat INPUT_DIR=path/to/directory OUTPUT_FILE=result.md"
	exit 1
endif
ifndef OUTPUT_FILE
	@echo "エラー: OUTPUT_FILEパラメータが必要です"
	@echo "使用例: make concat INPUT_DIR=path/to/directory OUTPUT_FILE=result.md"
	exit 1
endif
	@echo "ファイルを連結中..."
	@python -m html_to_md.utils.concat_files $(INPUT_DIR) $(OUTPUT_FILE) 
