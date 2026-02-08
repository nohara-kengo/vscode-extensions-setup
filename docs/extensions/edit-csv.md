# Edit CSV 使用マニュアル

## 目的
CSV/TSVファイルを表形式のUIで編集し、視覚的に操作しやすくします。

## インストール確認（任意）
- すべての拡張一覧:
```powershell
code --list-extensions
```
- この拡張の確認（存在すれば1行表示）:
```powershell
code --list-extensions | Where-Object { $_ -eq 'janisdd.vscode-edit-csv' }
```

## 個別インストール
- コマンドでインストール：
```powershell
code --install-extension janisdd.vscode-edit-csv
```
- スクリプトでインストール：
```powershell
.\scripts\extensions\edit-csv.ps1
```

## アンインストール
- コマンドで削除：
```powershell
code --uninstall-extension janisdd.vscode-edit-csv
```
- スクリプトで削除：
```powershell
.\scripts\extensions\uninstall\edit-csv-uninstall.ps1
```

## OS別コマンド差分（参考）
- PowerShell（Windows）
	- 確認（該当拡張のみ表示）:
		```powershell
		code --list-extensions | Where-Object { $_ -eq 'janisdd.vscode-edit-csv' }
		```
	- 個別インストール/アンインストール:
		```powershell
		code --install-extension janisdd.vscode-edit-csv
		code --uninstall-extension janisdd.vscode-edit-csv
		```
- Bash（Linux/Mac）
	- 確認（該当拡張のみ表示）:
		```bash
		code --list-extensions | grep -E '^janisdd.vscode-edit-csv$'
		```
	- 個別インストール/アンインストール:
		```bash
		code --install-extension janisdd.vscode-edit-csv
		code --uninstall-extension janisdd.vscode-edit-csv
		```

## 基本の使い方
- コマンドパレットで「Edit CSV」と入力して、表形式UIで開きます。
- テーブルUIでセル編集・追加・削除が可能です。
- 保存すると元のCSVへ反映されます。

## よく使うヒント
- 区切り文字（カンマ/タブなど）はファイルによって異なるため、UI上で選択・変更できる場合があります。
- 大きなファイルではフィルタや検索を活用してください。

## 参考
- 詳細な操作はコマンドパレットから「Edit CSV」関連のコマンドを参照してください。
