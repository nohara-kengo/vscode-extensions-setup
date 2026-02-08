# Rainbow CSV 使用マニュアル

## 目的
CSV/TSVなどの区切りテキストを色分けして見やすくし、列ごとの視認性を高めます。

## インストール確認（任意）
- すべての拡張一覧:
```powershell
code --list-extensions
```
- この拡張の確認（存在すれば1行表示）:
```powershell
code --list-extensions | Where-Object { $_ -eq 'mechatroner.rainbow-csv' }
```

## 個別インストール
- コマンドでインストール：
```powershell
code --install-extension mechatroner.rainbow-csv
```
- スクリプトでインストール：
```powershell
.\scripts\extensions\rainbow-csv.ps1
```

## アンインストール
- コマンドで削除：
```powershell
code --uninstall-extension mechatroner.rainbow-csv
```
- スクリプトで削除：
```powershell
.\scripts\extensions\uninstall\rainbow-csv-uninstall.ps1
```

## 基本の使い方
- CSV/TSVファイルを開くと自動で列が色分けされます。
- 区切り文字（カンマ/タブ/セミコロン等）はファイル内容に応じて自動判定されます。
- コマンドパレットで「Rainbow CSV」と入力すると、利用可能なコマンド一覧が表示されます。

## よく使うヒント
- 列の視認性が悪い場合は、ファイルの区切り文字が正しく設定されているか確認してください。
- 特殊な区切りや固定幅の場合は、コマンドパレットの関連コマンドから整形・判定を試してください。

## 参考
- 設定で動作や配色を調整可能です（VS Code設定から「Rainbow CSV」を検索）。
