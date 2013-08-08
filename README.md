# AlwaysHighlight

This plugin for [Sublime Text 2](http://www.sublimetext.com/2) enables to constantly highlight optional text.
It is a slight restructuring of [the plugin that highlights full-width spaces](http://qiita.com/kuronekomichael/items/865e1a6605b1146d4341).

## Installation

Save the package in Sublime Text 2's "Packages" folder.

## Settings

Highlighted text is designated as regular expression.
Open the Setting file in Preferences > Settings - User and write the text as follows:

```
    ...
    // always highlight "foo", "bar", and non-ASCII characters
    "alwayshighlight_pattern": "foo|bar|[^\\x00-\\x7E]",
    ...
```
