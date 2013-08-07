#!/usr/bin/python
# -*- coding: utf8 -*-
import sublime
import sublime_plugin

class AlwaysHighlight(sublime_plugin.EventListener):
    # highlight
    def highlight(self, view):
        pattern = view.settings().get('alwayshighlight_pattern')
        if pattern:
            view.add_regions('AlwaysHighlight', view.find_all(pattern), "invalid", sublime.DRAW_OUTLINED)

    # Called after changes have been made to a view.
    # @override
    def on_modified(self, view):
        self.highlight(view)

    # Called when a view gains input focus.
    # @override
    def on_activated(self, view):
        self.highlight(view)

    # Called when the file is finished loading.
    # @override
    def on_load(self, view):
        self.highlight(view)
