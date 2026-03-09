# 開発環境の概要（WSL + Docker）

このドキュメントでは、開発環境で使うWSLとDockerについて、PCの基本構造から順に説明します。

---

## 目次
- [PCの基本構造](#pcの基本構造)
- [WSLとは](#wslとは)
- [Dockerとは](#dockerとは)
- [なぜWSL + Dockerで開発するのか](#なぜwsl--dockerで開発するのか)
- [全体像まとめ](#全体像まとめ)
- [ワークフロー](#ワークフロー)

---

## PCの基本構造

普段使っているPCは、大きく分けて以下の5つの層で構成されています。

```mermaid
flowchart TB
  A["アプリケーション"]
  B["ミドルウェア"]
  C["OS"]
  D["ファームウェア"]
  E["ハードウェア"]

  A --> B --> C --> D --> E

  style A fill:#e8e8e8,stroke:#999,color:#333
  style B fill:#e8e8e8,stroke:#999,color:#333
  style C fill:#d0d0d0,stroke:#888,color:#333
  style D fill:#e8e8e8,stroke:#999,color:#333
  style E fill:#e8e8e8,stroke:#999,color:#333
```

| 層 | 説明 | 例 |
|---|---|---|
| **アプリケーション** | ユーザーが直接使うソフト | VS Code、ブラウザ |
| **ミドルウェア** | アプリとOSの間で動く基盤ソフト | Docker、データベース |
| **OS** | ハードウェアを管理しソフトを動かす土台 | Windows、Linux |
| **ファームウェア** | PC起動時にハードウェアを初期化するソフト | BIOS、UEFI |
| **ハードウェア** | 物理的な部品 | CPU、メモリ、ディスク |

---

## WSLとは

**WSL（Windows Subsystem for Linux）** は、Windows上でLinuxを動かせる仕組みです。

通常、1台のPCでは1つのOSしか使えませんが、WSLを使うとWindows内にLinux環境が追加され、両方のOSを同時に使えるようになります。

```mermaid
flowchart TB
  subgraph PC["Windows PC + WSL"]
    subgraph WIN["Windows"]
      WApp["Windowsアプリ"]
    end
    subgraph WSL["WSL"]
      LApp["Linuxコマンド"]
    end
    WApp -- 連携 --> WSL
  end

  style WIN fill:#e0e8f0,stroke:#8899aa,stroke-width:2px
  style WSL fill:#f0e8d8,stroke:#aa9977,stroke-width:2px
```

---

## Dockerとは

**Docker** は、アプリの実行環境をまるごとパッケージにして、どのPCでも同じ環境を再現できるツールです。

「自分のPCでは動くけど他の人のPCでは動かない」という問題を解決します。

```mermaid
flowchart LR
  subgraph Docker["Docker"]
    C1["コンテナA"]
    C2["コンテナB"]
  end

  style Docker fill:#dde5ed,stroke:#8899aa,stroke-width:2px
  style C1 fill:#f5f5f5,stroke:#aaa,color:#333
  style C2 fill:#f5f5f5,stroke:#aaa,color:#333
```

| 用語 | 説明 |
|---|---|
| **コンテナ** | アプリとその動作に必要なものをまとめた軽量な実行単位 |
| **イメージ** | コンテナの設計図。これを元にコンテナを作成する |

---

## なぜWSL + Dockerで開発するのか

### 開発環境の課題

| 課題 | 詳細 |
|---|---|
| 環境差異 | 人によってPCの設定が違い「自分のPCでは動く」問題が起きる |
| セットアップの手間 | 新メンバーが環境構築に何時間もかかる |
| 本番との差異 | 本番サーバーはLinuxだが開発PCはWindowsでOSが違う |

### WSL + Dockerによる解決

```mermaid
flowchart TB
  subgraph DEV["開発者のPC"]
    VSCode["VS Code"]
    subgraph WSL["WSL"]
      Docker["Docker"]
      subgraph CONT["コンテナ"]
        App["アプリ"]
        DB["データベース"]
      end
      Docker --> CONT
    end
    VSCode -- Remote WSL --> WSL
  end

  style WSL fill:#f0e8d8,stroke:#aa9977,stroke-width:2px
  style CONT fill:#f5f5f5,stroke:#aaa,stroke-width:2px
  style VSCode fill:#e0e8f0,stroke:#8899aa,stroke-width:2px
```

### メリット

| メリット | 説明 |
|---|---|
| **環境の統一** | 全員が同じDockerコンテナで開発するので環境差異がなくなる |
| **セットアップが簡単** | コマンド1つで開発環境が立ち上がる |
| **本番と同じOS** | WSL上のLinuxで開発するため本番サーバーとの差異が最小になる |
| **壊しても安心** | コンテナを消して作り直せば元通り。PC本体には影響しない |
| **複数プロジェクト対応** | プロジェクトごとに別のコンテナを使え依存関係が衝突しない |

---

## 全体像まとめ

```mermaid
flowchart LR
  A["Windows"] --> B["WSL"]
  B --> C["Docker"]
  C --> D["コンテナ"]
  E["VS Code"] -- Remote WSL --> B

  style A fill:#e0e8f0,stroke:#8899aa,stroke-width:2px
  style B fill:#f0e8d8,stroke:#aa9977,stroke-width:2px
  style C fill:#dde5ed,stroke:#8899aa,stroke-width:2px
  style D fill:#f5f5f5,stroke:#aaa,stroke-width:2px
  style E fill:#e0e8f0,stroke:#8899aa,stroke-width:2px
```

> Windows上のWSL（Linux）でDockerを動かし、コンテナ内で開発を行います。
> VS CodeからRemote WSL拡張で接続することで、Windows上で快適にLinux環境の開発ができます。

---

## ワークフロー

```mermaid
flowchart TB
  S1["1. 環境構築"]
  S2["2. Dockerマウント検証 / dockerファイル作成"]
  S3["3. READMEに使用方法を記載"]
  S4["4. GitHubでPR作成"]
  S5["5. 野原レビュー and FB"]
  S6["6. PTU全体に共有"]

  S1 --> S2 --> S3 --> S4 --> S5 --> S6

  style S1 fill:#e8e8e8,stroke:#999,color:#333
  style S2 fill:#e8e8e8,stroke:#999,color:#333
  style S3 fill:#e8e8e8,stroke:#999,color:#333
  style S4 fill:#d0d0d0,stroke:#888,color:#333
  style S5 fill:#d0d0d0,stroke:#888,color:#333
  style S6 fill:#d0d0d0,stroke:#888,color:#333
```

### スケジュール

| ステップ | 内容 | 期限 |
|---|---|---|
| 1 | WSL + Docker の環境構築 | 3/17(火)まで |
| 2 | Dockerマウント検証（dockerファイル作成） | 3/17(火)まで |
| 3 | READMEに使用方法を記載 | 3/17(火)まで |
| 4 | GitHubでPR作成 | **3/17(火)中** |
| 5 | 野原レビュー＆フィードバック | 3/18(水) |
| 6 | PTU全体に共有して完了 | 3/18(水)以降 |
