#!/usr/bin/env python3
"""No-op legacy README updater.

The new multi-market README is maintained by src.utils.readme_updater.
"""


class ReadmeUpdater:
    def __init__(self, project_root: str):
        self.project_root = project_root

    def update_exchange_table(self):
        return ""
