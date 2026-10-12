# Qiskitで実装するGrover探索｜「あたり」を高速に見つける

[![run](https://github.com/jumpei1228/quantum-grover-qiskit/actions/workflows/run.yml/badge.svg)](https://github.com/jumpei1228/quantum-grover-qiskit/actions/workflows/run.yml)

量子探索アルゴリズム「グローバー」をQiskitで手を動かして実装。オラクルと拡散演算子の作り方、なぜ√N回で見つかるのか、反復回数の決め方までコード付きで解説します。概念記事の実装版。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[Qiskitで実装するGrover探索｜「あたり」を高速に見つける](https://quantum.yurufuwa.work/learn/grover-qiskit)** — ゆるふわ量子コンピュータ

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python grover-qiskit.py
```

## これは何？

[ゆるふわ量子コンピュータ](https://quantum.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
