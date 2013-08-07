# AlwaysHighlight

常に任意のテキストをハイライトする[Sublime Text 2](http://www.sublimetext.com/2)のプラグインです。[全角スペースをハイライト表示するプラグイン](http://qiita.com/kuronekomichael/items/865e1a6605b1146d4341)をちょっと改造しただけのものです。

## インストール

パッケージをSublime Text 2のPackagesフォルダに置いてください。

## 設定

ハイライトするテキストは正規表現で指定します。Preferences > Settings - Userで設定ファイルを開いて、次のように書いてください。

```
    ...
    // "foo"、"bar"、全角空白、全角英数字を常にハイライトする
    "alwayshighlight_pattern": "foo|bar|[　０-９Ａ-Ｚａ-ｚ]",
    ...
```
