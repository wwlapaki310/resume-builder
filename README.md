# Resume Builder

英語版履歴書（`index.html` → `resume-english.pdf`）の管理リポジトリ。

---

## ファイル構成

```
resume-builder/
├── index.html           # 履歴書のソースファイル（編集対象）
└── resume-english.pdf   # index.html をブラウザからPDF出力したもの
```

---

## 仕組み

### `index.html` の構造

外部ライブラリや依存関係は一切なし。1ファイルで完結している。

| 要素 | 内容 |
|------|------|
| コンテンツ | HTMLに直接記述 |
| スタイル | `<style>` タグに CSS を埋め込み |
| アイコン | インライン SVG（外部ファイル不要） |
| レイアウト | CSS Grid（左2/右1の2カラム構成） |

**印刷用 CSS の仕組み:**

```css
@page {
    size: A4;
    margin: 5mm 8mm;   /* A4、余白を最小限に */
}

@media print {
    /* 画面表示用より小さいフォント、タイトな余白に切り替え */
    li { font-size: 9pt; }
    ...
}
```

- 画面で見るときは読みやすいサイズで表示
- 印刷時（PDF出力時）は `@media print` ブロックが適用され、A4 1枚に収まるようフォントサイズ・余白が自動調整される

---

### `resume-english.pdf` の生成方法

`index.html` をブラウザで開いてPDF印刷するだけ。

1. `index.html` をブラウザ（Chrome 推奨）で開く
2. `Ctrl + P`（Mac は `Cmd + P`）で印刷ダイアログを開く
3. 以下の設定にする：
   - 送信先: **「PDFに保存」**
   - 用紙サイズ: **A4**
   - 余白: **「なし」**（`@page` CSS が余白を制御するため）
   - 背景のグラフィック: オフでOK
4. 「保存」→ `resume-english.pdf` として出力

---

## 編集方法

履歴書の内容を更新する場合は `index.html` を直接編集し、上記手順で PDF を再生成する。

```
index.html を編集
    ↓
ブラウザで確認（画面表示）
    ↓
Ctrl+P → PDFに保存
    ↓
resume-english.pdf を上書き保存
```

---

## リンク

- LinkedIn: https://www.linkedin.com/in/satoru-akita-6070a4145/
- Portfolio: https://wwlapaki310.github.io/
- GitHub: https://github.com/wwlapaki310
