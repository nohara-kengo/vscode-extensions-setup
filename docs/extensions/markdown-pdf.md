# Markdown PDF 使用マニュアル

## 目的
MarkdownファイルをPDFへ変換します。

## インストール確認（任意）
- すべての拡張一覧:
```powershell
code --list-extensions
```
- この拡張の確認（存在すれば1行表示）:
```powershell
code --list-extensions | Where-Object { $_ -eq 'yzane.markdown-pdf' }
```

## 個別インストール
- コマンドでインストール：
```powershell
code --install-extension yzane.markdown-pdf
```
- スクリプトでインストール：
```powershell
.\scripts\extensions\markdown-pdf.ps1
```

## アンインストール
- コマンドで削除：
```powershell
code --uninstall-extension yzane.markdown-pdf
```
- スクリプトで削除：
```powershell
.\scripts\extensions\uninstall\markdown-pdf-uninstall.ps1
```

## 基本の使い方
- エディタでMarkdownを開き、コマンドパレットで「Markdown PDF」と入力し、PDFへエクスポートします。
- 右クリックメニューからのエクスポート（PDF/HTML/PNG/JPEG等）も利用可能です。

## ガイドライン
- 画像や数式、図（mermaid/PlantUML等）のレンダリングは環境や設定に依存します。うまく出力できない場合は拡張設定を確認してください。
- 出力先フォルダ・ファイル名の規約は設定で変更可能です。

## 参考
- 詳細設定はVS Code設定で「Markdown PDF」を検索して確認できます。
