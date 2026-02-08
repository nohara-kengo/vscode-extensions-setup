# Git Graph 使用マニュアル

## 目的
リポジトリの変更履歴やブランチ構造をグラフで視覚化し、基本的なGit操作を行います。

## インストール確認（任意）
- すべての拡張一覧:
```powershell
code --list-extensions
```
- この拡張の確認（存在すれば1行表示）:
```powershell
code --list-extensions | Where-Object { $_ -eq 'mhutchie.git-graph' }
```

## 個別インストール
- コマンドでインストール：
```powershell
code --install-extension mhutchie.git-graph
```
- スクリプトでインストール：
```powershell
.\scripts\extensions\git-graph.ps1
```

## アンインストール
- コマンドで削除：
```powershell
code --uninstall-extension mhutchie.git-graph
```
- スクリプトで削除：
```powershell
.\scripts\extensions\uninstall\git-graph-uninstall.ps1
```

## 基本の使い方
- コマンドパレットで「Git Graph: View Git Graph」を実行してビューを開きます。
- コミット・ブランチ・タグを確認でき、チェックアウトやマージ、リバートなどの操作が可能です。

## よく使うヒント
- 大規模履歴ではフィルタや検索で対象コミットを絞り込みます。
- 競合や詳細な操作はVS Codeのソース管理ビューと併用すると便利です。

## 参考
- 設定や操作チップはGit Graphビュー内のメニューから確認できます。
