#!/usr/bin/env python
"""Djangoの管理タスク用コマンドラインユーティリティ"""
import os
import sys


def main():
    """管理タスクを実行します。"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Djangoをインポートできませんでした。Djangoが正しくインストールされているか、"
            "PYTHONPATH環境変数に含まれているか確認してください。"
            "仮想環境を有効にしていない可能性もあります。"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
