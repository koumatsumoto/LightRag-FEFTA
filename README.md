# LightRag-FEFTA

軽量 RAG フレームワークを用いた外国為替及び外国貿易法(FEFTA)分析ツール。Python で実装された本ツールは、FEFTA 関連文書をローカル環境で効率的に検索・分析できます。法規制コンプライアンスの確認や貿易規制の把握に役立つ、専門家向けナレッジベースシステムです。オフライン環境でも高精度な情報抽出が可能。

## 開発者向け情報

### 必要要件

- Python 3.10 以上
- Poetry

### インストール方法

```bash
# リポジトリのクローン
git clone https://github.com/koumatsumoto/LightRag-FEFTA.git
cd LightRag-FEFTA

# 依存関係のインストール
poetry install
```

### 実行方法

以下のコマンドでツールを実行できます：

```bash
# RAGの構築
poetry run build

# クエリの実行
poetry run query "質問文" [--mode モード]

# ヘルプの表示
poetry run query --help
```

#### クエリコマンドのパラメータ

- `query`: 質問文（必須）

  - 1 文字以上の文字列である必要があります
  - 空文字列や空白文字のみの入力は無効です

- `--mode`: 検索モード（オプション、デフォルト: mix）
  - 以下のいずれかを指定できます：
    - naive: ナイーブな検索
    - local: ローカル検索
    - global: グローバル検索
    - hybrid: ハイブリッド検索
    - mix: 混合検索

使用例：

```bash
# 基本的な使用方法
poetry run query "日本の首都について教えてください"

# モードを指定する場合
poetry run query "日本の首都について教えてください" --mode naive
```

### コードフォーマット

コードの自動フォーマットには black を使用しています。以下の手順でフォーマットを実行してください：

1. コード変更後、以下のコマンドを実行：

```bash
poetry run black .
```

このコマンドは全ての Python ファイルを black の規約に従ってフォーマットします。プルリクエスト提出前に必ず実行してください。
