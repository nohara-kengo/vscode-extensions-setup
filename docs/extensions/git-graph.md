# Git Graph 使用マニュアル

## 目的
リポジトリの変更履歴やブランチ構造をグラフで視覚化し、基本的なGit操作を行います。

## 解決する課題
- CLIだけでは履歴やブランチ関係を把握しづらい
- 複雑なマージ状況やタグの可視化不足

## 効率化できること
- コミット履歴のグラフ表示で把握を迅速化
- ブランチ作成/チェックアウト/マージ等をUIから実施
- 差分・タグ・検索の操作をまとめて行い、調査時間を短縮

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

## 利用手順
1. リポジトリを開く
	- VS Codeで対象フォルダを開きます（Git管理でない場合は初期化）。
	```powershell
	git init
	git status
	```
2. Git Graphビューを開く
	- コマンドパレットで「Git Graph: View Git Graph」を実行、またはステータスバーのGit Graphアイコンから開きます。
3. コミットを確認する
	- グラフ上でコミットを選択すると差分やメッセージ、著者が表示されます。
	- 右クリックで「Compare」「View Diff」などの操作が可能です。
4. ブランチ操作
	- 右クリックから「Create Branch」「Checkout」「Rename」「Delete」を実行できます。
	- 現在のHEADを別ブランチへ切り替える場合は「Checkout」を使用します。
5. マージ/リベース
	- 右クリックから「Merge into current branch」「Rebase current branch onto…」を選択します。
	- 競合が出た場合はエディタで解決し、再度コミットしてください。
6. タグ/チェリーピック/リバート
	- コミット右クリックでタグ付け（Create Tag）、チェリーピック（Cherry-pick）、リバート（Revert）が可能です。
7. 取得/更新（リモート連携）
	- ビュー上部のメニューや右クリックから「Fetch」「Pull」「Push」を実行できます。CLI例：
	```powershell
	git fetch --all
	git pull
	git push
	```
8. フィルタ/検索
	- ビュー上部のフィルタでブランチや作者、メッセージで絞り込み。検索バーでコミットを検索します。

## よく使う操作のヒント
- 比較: 2つのコミットを選択して差分比較（Compare）を使うと原因調査が速くなります。
- 作業ブランチの整理: 不要ブランチはビューからDelete。保護ブランチはリモート設定で保護してください。
- リベースとマージ: 履歴を揃えたい場合はリベース、履歴を残したい場合はマージを選択。
- 大規模履歴: フィルタと検索を併用して対象コミットを素早く特定。

## ガイドライン
- 大規模履歴ではフィルタや検索で対象コミットを絞り込みます。
- 競合や詳細な操作はVS Codeのソース管理ビューと併用すると便利です。

## 参考
- 設定や操作チップはGit Graphビュー内のメニューから確認できます。
