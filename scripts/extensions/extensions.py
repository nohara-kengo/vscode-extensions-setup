import subprocess
import sys


"""
VS Code拡張機能一括インストール・アンインストール用スクリプト
============================================================
このスクリプトは、Visual Studio Code（VS Code）の拡張機能を
まとめてインストール・アンインストールできる自動化ツールです。

■ できること
・拡張機能IDリストに書かれた全ての拡張を一括でインストール/アンインストール
・Windows/Mac/Linux/WSL どのOSでも同じように使える

■ 使い方（ターミナルで実行）
    python scripts/extensions/extensions.py install      # 一括インストール
    python scripts/extensions/extensions.py uninstall    # 一括アンインストール

■ 注意
・VS Codeの「code」コマンドが使える状態であること（which code で確認）
・拡張IDは「publisher.extension-name」の形式
・Pythonがインストールされていない場合は先にインストールしてください
"""

# 一括で管理したい拡張機能IDのリスト
# ここに追加した拡張が全て対象になります
EXTENSIONS = [
    "janisdd.vscode-edit-csv",      # CSVファイルを直接編集できる拡張
    "yzane.markdown-pdf",           # MarkdownファイルをPDFに変換する拡張
    "mhutchie.git-graph",           # Gitリポジトリの履歴をグラフ表示する拡張
    "Gruntfuggly.todo-tree"          # TODOコメントをツリー表示する拡張
]


def install_extensions():
    """
    EXTENSIONSリストにある全ての拡張機能をインストールします。
    すでにインストール済みの拡張も再度コマンドを実行します（VS Code側で自動判定）。
    インストール結果は標準出力に表示されます。
    """
    for ext in EXTENSIONS:
        print(f"Installing {ext}...")  # 何をインストールするか表示
        # codeコマンドで拡張をインストール
        result = subprocess.run(["code", "--install-extension", ext], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Installed: {ext}")
        else:
            print(f"Failed: {ext}\n{result.stderr}")


def uninstall_extensions():
    """
    EXTENSIONSリストにある全ての拡張機能をアンインストールします。
    インストールされていない拡張もコマンドを実行します（VS Code側で自動判定）。
    アンインストール結果は標準出力に表示されます。
    """
    for ext in EXTENSIONS:
        print(f"Uninstalling {ext}...")  # 何をアンインストールするか表示
        # codeコマンドで拡張をアンインストール
        result = subprocess.run(["code", "--uninstall-extension", ext], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Uninstalled: {ext}")
        else:
            print(f"Failed: {ext}\n{result.stderr}")


def main():
    """
    コマンドライン引数でinstall/uninstallを受け取り、
    拡張機能の一括インストールまたはアンインストールを実行します。
    Usage:
        python scripts/extensions/extensions.py install
        python scripts/extensions/extensions.py uninstall
    """
    if len(sys.argv) < 2:
        print("Usage: python scripts/extensions/extensions.py [install|uninstall]")
        print("例: python scripts/extensions/extensions.py install")
        sys.exit(1)
    if sys.argv[1] == "install":
        install_extensions()
    elif sys.argv[1] == "uninstall":
        uninstall_extensions()
    else:
        print("Unknown command. Use 'install' or 'uninstall'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
