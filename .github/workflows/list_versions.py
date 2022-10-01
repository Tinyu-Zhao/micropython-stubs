import json
from os import environ

from github import Github
from packaging.version import parse


def micropython_versions(start="v1.9.2"):
    g = Github()
    repo = g.get_repo("micropython/micropython")
    return [tag.name for tag in repo.get_tags() if parse(tag.name) >= parse(start)]


if __name__ == "__main__":
    matrix = {}
    if environ.get("ACT"):
        # only run latests when running in ACT locally for testing
        matrix["version"] = ["latest"]
    else:
        matrix["version"] = micropython_versions(start="v1.17") + ["latest"]
    print(json.dumps(matrix))

    print(f"::set-output name=versions::{json.dumps(matrix)}")
