import subprocess


"""
VS Code拡張機能管理スクリプト
=============================
このスクリプトは、Visual Studio Code（VS Code）の拡張機能を
コマンドラインからインストール・アンインストールできるツールです。

■ できること
・拡張機能IDを指定して、インストールまたはアンインストール
・Windows/Mac/Linux/WSL どのOSでも同じように使える

■ 使い方（ターミナルで実行）
    python extension_task.py install janisdd.vscode-edit-csv
    python extension_task.py uninstall mhutchie.git-graph

■ 注意
・VS Codeの「code」コマンドが使える状態であること（which code で確認）
・拡張IDは「publisher.extension-name」の形式
・Pythonがインストールされていない場合は先にインストールしてください
"""

###########################################################
# 一括管理したい拡張機能IDのリスト（参考用）
# 必要に応じてこのリストをfor文で回して一括処理も可能です。
# 例: for ext in EXTENSIONS: install(ext)
###########################################################
EXTENSIONS = [
    "janisdd.vscode-edit-csv",      # CSVファイルを直接編集できる拡張
    "yzane.markdown-pdf",           # MarkdownファイルをPDFに変換する拡張
    "mhutchie.git-graph",           # Gitリポジトリの履歴をグラフ表示する拡張
    "Gruntfuggly.todo-tree"          # TODOコメントをツリー表示する拡張
]


def install(ext):
    """
    指定した拡張機能をVS Codeにインストールします。
    すでにインストール済みの場合は何もせずメッセージだけ表示します。

    Parameters:
        ext (str): 拡張機能ID（例: janisdd.vscode-edit-csv）

    Returns:
        なし（標準出力に結果を表示）

    注意:
        ・拡張IDは正確に指定してください。
        ・codeコマンドが使えない場合はエラーになります。
    """
    # code --list-extensions で現在インストール済みの拡張一覧を取得
    result = subprocess.run(["code", "--list-extensions"], capture_output=True, text=True)
    # すでにインストール済みかどうか判定
    if ext in result.stdout:
        print(f"Already installed: {ext}")
        return
    # インストール処理
    print(f"Installing {ext}...")
    subprocess.run(["code", "--install-extension", ext])
    # インストール完了後のメッセージはcodeコマンドが自動で出力します


def uninstall(ext):
    """
    指定した拡張機能をVS Codeからアンインストールします。
    インストールされていない場合は何もせずメッセージだけ表示します。

    Parameters:
        ext (str): 拡張機能ID

    Returns:
        なし（標準出力に結果を表示）

    注意:
        ・拡張IDは正確に指定してください。
        ・codeコマンドが使えない場合はエラーになります。
    """
    # code --list-extensions で現在インストール済みの拡張一覧を取得
    result = subprocess.run(["code", "--list-extensions"], capture_output=True, text=True)
    # インストールされていない場合
    if ext not in result.stdout:
        print(f"Not installed: {ext}")
        return
    # アンインストール処理
    print(f"Uninstalling {ext}...")
    subprocess.run(["code", "--uninstall-extension", ext])
    print(f"Uninstall completed: {ext}")


if __name__ == "__main__":
    """
    コマンドライン引数でinstall/uninstallと拡張IDを受け取り、該当処理を実行します。

    例:
        python extension_task.py install janisdd.vscode-edit-csv
        python extension_task.py uninstall mhutchie.git-graph

    install:    指定した拡張機能をインストール
    uninstall:  指定した拡張機能をアンインストール
    """
    import sys  # コマンドライン引数を扱う標準ライブラリ
    # 引数が足りない場合は使い方を表示して終了
    if len(sys.argv) < 3:
        print("Usage: python extension_task.py [install|uninstall] <extensionId>")
        print("例: python extension_task.py install janisdd.vscode-edit-csv")
        sys.exit(1)
    action = sys.argv[1]  # install か uninstall
    ext = sys.argv[2]     # 拡張ID
    # install か uninstall を実行
    if action == "install":
        install(ext)
    elif action == "uninstall":
        uninstall(ext)
    else:
        print("Unknown action. Use 'install' or 'uninstall'.")
        sys.exit(1)
