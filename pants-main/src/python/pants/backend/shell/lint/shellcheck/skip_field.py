# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.shell.target_types import (
    ShellSourcesGeneratorTarget,
    ShellSourceTarget,
    Shunit2TestsGeneratorTarget,
    Shunit2TestTarget,
)
from pants.engine.target import BoolField


class SkipShellcheckField(BoolField):
    alias = "skip_shellcheck"
    default = False
    help = "If true, don't run Shellcheck on this target's code."


def rules():
    return [
        ShellSourceTarget.register_plugin_field(SkipShellcheckField),
        ShellSourcesGeneratorTarget.register_plugin_field(SkipShellcheckField),
        Shunit2TestTarget.register_plugin_field(SkipShellcheckField),
        Shunit2TestsGeneratorTarget.register_plugin_field(SkipShellcheckField),
    ]
