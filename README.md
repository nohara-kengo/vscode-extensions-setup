# VS Code Extensions Setup
チーム内で使用する Visual Studio Code の拡張機能を統一し、新規メンバーや別チームでも開発環境を迅速に再現できるようにするためのリポジトリです。拡張機能の一覧をファイルで管理し、コマンド一つで自動インストールできます。

## 目次
- [VS Code Extensions Setup](#vs-code-extensions-setup)
  - [目次](#目次)
  - [前提条件（Windows）](#前提条件windows)
  - [クイックスタート（一括インストール）](#クイックスタート一括インストール)
    - [拡張機能一覧表とマニュアル格納先](#拡張機能一覧表とマニュアル格納先)
  - [インストール詳細](#インストール詳細)
  - [アンインストール詳細](#アンインストール詳細)
  - [追加の検討事項](#追加の検討事項)
    - [OS別コマンド差分（PowerShell / Bash）](#os別コマンド差分powershell--bash)
    - [Dockerからの実行（ボリューム連携）](#dockerからの実行ボリューム連携)

## 前提条件（Windows）
- VS Code の `code` CLI が PATH で利用可能であること
  - 通常はインストール時に有効化されます。未設定の場合は VS Code のインストールフォルダ配下 `bin` の `code` を PATH に追加してください。

## クイックスタート（一括インストール）
実行場所: リポジトリ直下でコマンドを実行してください。

```powershell
cd vscode-extensions-setup
```

1. `code` CLI が使えるか確認

```powershell
Get-Command code -ErrorAction SilentlyContinue | Select-Object -First 1 | Format-List | Out-String
```

出力に `Name : code.cmd` や `Path : ...\Microsoft VS Code\bin\code.cmd` が表示されればOKです。

2. 拡張を一括インストール（スクリプトを使用）

```powershell
.\install-extensions.ps1
```

3. インストール確認（フィルタ表示）

```powershell
code --list-extensions | Select-String -Pattern 'rainbow-csv|vscode-edit-csv|markdown-pdf|git-graph|todo-tree'
```
### 拡張機能一覧表とマニュアル格納先
- 参照先: [docs/extensions.md](docs/extensions.md)

## インストール詳細
配布・保守のしやすさから、拡張ごとの個別スクリプト（`scripts/extensions` 配下）を用意し、[install-extensions.ps1](install-extensions.ps1) でまとめて実行します。

```powershell
#  一括インストール
.\install-extensions.ps1

```

## アンインストール詳細
配布・保守のしやすさから、拡張ごとの個別スクリプト（`scripts/extensions/uninstall` 配下）を用意し、[uninstall-extensions.ps1](uninstall-extensions.ps1) でまとめて実行します。

```powershell
# 一括アンインストール
.\uninstall-extensions.ps1

```

## 追加の検討事項
### OS別コマンド差分（PowerShell / Bash）
- 例示のコマンドは原則 Windows PowerShell 向けです。Linux/Mac の Bash では記法が異なります。
- 主な差分:
  - フィルタ: PowerShell は `Select-String`/`Where-Object`、Bash は `grep`/`awk`
  - 行継続: PowerShell は `` ` ``、Bash は `\`
  - 環境変数: PowerShell は `$env:VAR`、Bash は `$VAR`

- コマンド対比例:
  - CLI確認
    - PowerShell
      ```powershell
      Get-Command code -ErrorAction SilentlyContinue | Select-Object -First 1 | Format-List | Out-String
      ```
    - Bash
      ```bash
      which code && code --version
      ```
  - 個別インストール/アンインストール
    - 共通（両OS）
      ```
      code --install-extension <extensionId>
      code --uninstall-extension <extensionId>
      ```
  - 確認（一覧から該当拡張のみ表示）
    - PowerShell
      ```powershell
      code --list-extensions | Where-Object { $_ -eq '<extensionId>' }
      ```
    - Bash
      ```bash
      code --list-extensions | grep -E '^<extensionId>$'
      ```
  - Docker（code-server例）
    - PowerShell
      ```powershell
      docker run --rm `
        -v "$env:USERPROFILE\.code-server":/home/coder/.local/share/code-server `
        -v "$PWD":/workspace `
        -w /workspace `
        <image-with-code-server> bash -lc "code-server --install-extension <extensionId>"
      ```
    - Bash
      ```bash
      docker run --rm \
        -v "$HOME/.local/share/code-server":/home/coder/.local/share/code-server \
        -v "$PWD":/workspace \
        -w /workspace \
        <image-with-code-server> bash -lc "code-server --install-extension <extensionId>"
      ```
      
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
  <image-with-code-server> bash -lc "code-server --install-extension mechatroner.rainbow-csv"
```
- 例（Windows PowerShell・code-server利用例・パス要調整）:
```powershell
docker run --rm `
  -v "$env:USERPROFILE\.code-server":/home/coder/.local/share/code-server `
  -v "$PWD":/workspace `
  -w /workspace `
  <image-with-code-server> bash -lc "code-server --install-extension mechatroner.rainbow-csv"
```
- 次のステップ（提案）:
  - `Dockerfile` と `docker-compose.yml` の雛形を追加（`code-server`入りイメージ、拡張のバッチ適用コマンドを同梱）。
  - CI用ジョブからボリューム指定で一括インストール/アンインストールを実行。