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
poetry run lightrag-fefta
```

### 開発環境のセットアップ

コードフォーマットには black を使用しています：

```bash
poetry run black .
```
