# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.docker.goals.tailor import rules as tailor_rules
from pants.backend.docker.rules import rules as docker_rules
from pants.backend.docker.target_types import DockerImageTarget
from pants.backend.docker.target_types import rules as target_types_rules


def rules():
    return (
        *docker_rules(),
        *tailor_rules(),
        *target_types_rules(),
    )


def target_types():
    return (DockerImageTarget,)
