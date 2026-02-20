# VS Code Extensions Setup
チーム内で使用する Visual Studio Code の拡張機能を統一し、新規メンバーや別チームでも開発環境を迅速に再現できるようにするためのリポジトリです。拡張機能の一覧をファイルで管理し、コマンド一つで自動インストールできます。

## 目次
- [背景（Docker/コンテナ環境の課題）](#背景dockerコンテナ環境の課題)
- [前提条件](#前提条件)
  - [Windows](#windows)
  - [Linux（Ubuntu/WSL）](#linuxubuntuwsl)
- [クイックスタート（一括インストール）](#クイックスタート一括インストール)
  - [OS差分を吸収するPythonスクリプト方式（推奨）](#os差分を吸収するpythonスクリプト方式推奨)
  - [拡張機能一覧表とマニュアル格納先](#拡張機能一覧表とマニュアル格納先)
- [インストール詳細](#インストール詳細)
  - [個別拡張インストール・アンインストール](#個別拡張インストールアンインストール)
- [スクリプト実行ポリシー（PowerShell/Bash両対応）](#スクリプト実行ポリシーパワーシェルbash両対応)
  - [Windows（PowerShell）](#windowsパワーシェル)
  - [Linux/WSL/Mac（Bash）](#linuxwslmacbash)
  - [確認コマンド（任意）](#確認コマンド任意)
  - [期待値（コマンド実行後の出力例）](#期待値コマンド実行後の出力例)
- [追加の検討事項](#追加の検討事項)
  - [Dockerからの実行（ボリューム連携）](#dockerからの実行ボリューム連携)

## 背景（Docker/コンテナ環境の課題）
- 課題: コンテナ内にインストールした拡張機能は、コンテナを再作成・再起動すると揮発的なストレージのため消えてしまいがちです（毎回入れ直しが必要）。
- 経緯: 毎回拡張が消えるのが運用上の負担だったため、このリポジトリに一括インストール/アンインストール用のスクリプトを導入し、環境再現を自動化しました。
- 対応: Docker利用時は拡張ディレクトリをボリュームで永続化する運用を推奨し、必要に応じて起動時（CI/コンテナ起動フック等）にスクリプトで拡張を適用します。

## 前提条件

### Windows
- VS Code の `code` CLI が PATH で利用可能であること
  - 通常はインストール時に有効化されます。未設定の場合は VS Code のインストールフォルダ配下 `bin` の `code` を PATH に追加してください。

### Linux（Ubuntu/WSL）
- VS Code の `code` CLI が PATH で利用可能であること
  - WSLの場合、`code`コマンドはVS Codeをインストールすると自動でPATHに追加されます。
  - `code`が見つからない場合は、VS Codeを再インストールするか、`/usr/bin/code`のパスを確認してください。
  - CLI確認は `which code` または `command -v code` で行います。

## クイックスタート（一括インストール）
実行場所: リポジトリ直下でコマンドを実行してください。

### OS差分を吸収するPythonスクリプト方式（推奨）
Pythonがインストールされていれば、OS問わず同じ手順で拡張機能の一括インストール/アンインストールが可能です。

1. Pythonがインストールされていることを確認
  - Windows: コマンドプロンプトやPowerShellで `python --version`
  - Linux/WSL: ターミナルで `python3 --version` または `python --version`
  - Pythonが入っていない場合は以下の手順でインストール（バージョンの指定は特にないため最新をインストールしてくだださい）
    - Windows: [公式サイト](https://www.python.org/downloads/windows/)からインストーラーをダウンロードし、PATHに追加するオプションを有効化してインストール
    - Linux/WSL: ターミナルで `sudo apt update && sudo apt install -y python3` を実行

---
2. `code` CLIが使えることを確認
  - `which code` または `Get-Command code` など
3. 拡張を一括インストール
  - リポジトリ直下で次のコマンドを実行
    - Windows: `python scripts/extensions/extensions.py install`
    - Linux/WSL: `python3 scripts/extensions/extensions.py install` または `python scripts/extensions/extensions.py install`
4. 拡張を一括アンインストール
  - Windows: `python scripts/extensions/extensions.py uninstall`
  - Linux/WSL: `python3 scripts/extensions/extensions.py uninstall` または `python scripts/extensions/extensions.py uninstall`
5. インストール確認（フィルタ表示）
  - Windows: `code --list-extensions | Select-String -Pattern 'vscode-edit-csv|markdown-pdf|git-graph|todo-tree'`
  - Linux/WSL: `code --list-extensions | grep -E 'vscode-edit-csv|markdown-pdf|git-graph|todo-tree'`

---

従来のPowerShell/Bash手順も参考として残しています。
### 拡張機能一覧表とマニュアル格納先
- 参照先: [docs/extensions.md](docs/extensions.md)

## インストール詳細
OS差分を吸収するため、拡張機能の一括インストールはPythonスクリプト（scripts/extensions/extensions.py）で行います。
拡張機能リストはスクリプト内で管理されており、コマンド一つで全てインストール可能です。

### 個別拡張インストール・アンインストール
拡張ごとに個別実行したい場合は、`scripts/extensions/extension_task.py` を利用してください。
例：
```bash
# インストール
python scripts/extensions/extension_task.py install janisdd.vscode-edit-csv
# アンインストール
python scripts/extensions/extension_task.py uninstall janisdd.vscode-edit-csv
```

---
  - インストール済みの例:
  ```
  mhutchie.git-graph
  yzane.markdown-pdf
  Gruntfuggly.todo-tree
  janisdd.vscode-edit-csv
  ```
  - アンインストール後の例: 該当拡張がなければ出力なし（何も表示されないのが期待値）。

  一括インストール（`python scripts/extensions/extensions.py install`）の例:
  ```
  Installing janisdd.vscode-edit-csv...
  Installed: janisdd.vscode-edit-csv
  このセクションは「Windows PowerShell」向けの実行ポリシー設定と、「Linux/WSL/Mac」向けの注意点を両方記載しています。どちらの手順も選択できます。

  #### Windows（PowerShell）
  PowerShellスクリプト（.ps1）を使う場合、既定の実行ポリシーやブロック属性で実行できないことがあります。必要に応じて下記コマンドで一時的に許可してください。

  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
  Get-ChildItem -Path . -Filter *.ps1 -Recurse | Unblock-File
  ```

  ---

  #### Linux/WSL/Mac（Bash）
  Linux/WSL/Macではスクリプト実行ポリシーの概念はありません。BashスクリプトやPythonスクリプトはそのまま実行できます。

### 確認コマンド（任意）
```powershell
code --list-extensions
```

### 期待値（コマンド実行後の出力例）

- 拡張一覧フィルタ（インストール確認）
  - インストール済みの例:
  ```
  mhutchie.git-graph
  yzane.markdown-pdf
  Gruntfuggly.todo-tree
  janisdd.vscode-edit-csv
  ```
  - アンインストール後の例: 該当拡張がなければ出力なし（何も表示されないのが期待値）。

- 一括インストールの例:
  ```
  Running edit-csv.ps1...
  Installing janisdd.vscode-edit-csv...
  Extension 'janisdd.vscode-edit-csv' was successfully installed!
  ...
  ```

- 一括アンインストールの例:
  ```
  Running edit-csv-uninstall.ps1...
  Uninstalling janisdd.vscode-edit-csv...
  Extension 'janisdd.vscode-edit-csv' was successfully uninstalled!
  Not installed: janisdd.vscode-edit-csv  # 既に削除済みの場合
  ...
  ```

## 追加の検討事項
### Dockerからの実行（ボリューム連携）
- 目的: コンテナから拡張インストール/アンインストールを実行できるようにし、CIや配布に対応。
- 前提: コンテナ側で`code`互換のCLI（例: `code-server`）を使用。ホスト側拡張ディレクトリをボリュームでマウントして反映。
- 注意: `code-server`の拡張保存先は環境に依存。以下は一般的な例で、環境に合わせてパス調整が必要。
- 例（Linuxホスト想定・code-server利用例）:
```bash
docker run --rm \
  -v "$HOME/.local/share/code-server":/home/coder/.local/share/code-server \
  -v "$PWD":/workspace \
  -w /workspace \
  <image-with-code-server> bash -lc "code-server --install-extension janisdd.vscode-edit-csv"
```
- 例（Windows PowerShell・code-server利用例・パス要調整）:
```powershell
docker run --rm `
  -v "$env:USERPROFILE\.code-server":/home/coder/.local/share/code-server `
  -v "$PWD":/workspace `
  -w /workspace `
  <image-with-code-server> bash -lc "code-server --install-extension janisdd.vscode-edit-csv"
```
- 次のステップ（提案）:
  - `Dockerfile` と `docker-compose.yml` の雛形を追加（`code-server`入りイメージ、拡張のバッチ適用コマンドを同梱）。
  - CI用ジョブからボリューム指定で一括インストール/アンインストールを実行。