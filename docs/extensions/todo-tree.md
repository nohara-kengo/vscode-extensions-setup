# Todo Tree 使用マニュアル

## 目的
コード中の`TODO`や`FIXME`などのタグを収集し、ツリー表示で管理します。

## インストール確認（任意）
- すべての拡張一覧:
```powershell
code --list-extensions
```
- この拡張の確認（存在すれば1行表示）:
```powershell
code --list-extensions | Where-Object { $_ -eq 'Gruntfuggly.todo-tree' }
```

## 個別インストール
- コマンドでインストール：
```powershell
code --install-extension Gruntfuggly.todo-tree
```
- スクリプトでインストール：
```powershell
.\scripts\extensions\todo-tree.ps1
```

## アンインストール
- コマンドで削除：
```powershell
code --uninstall-extension Gruntfuggly.todo-tree
```
- スクリプトで削除：
```powershell
.\scripts\extensions\uninstall\todo-tree-uninstall.ps1
```

## 基本の使い方
- サイドバーにTodo Treeビューが追加され、タグが一覧表示されます。
- 項目をクリックすると該当箇所へジャンプできます。

## ガイドライン
- タグの種類や検出パターンは設定でカスタマイズ可能です（例: `TODO`, `FIXME`, `BUG` など）。
- ワークスペースごとに設定を調整するとチームの規約に合わせて運用できます。

## 参考
- VS Code設定で「Todo Tree」を検索し、タグ・アイコン・除外パターンなどを調整してください。
