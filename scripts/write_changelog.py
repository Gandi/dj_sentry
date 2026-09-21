#!/usr/bin/env python3
import datetime
from importlib.metadata import version

header = (
    f"## {version('dj_sentry')}  - "
    f"Released on {datetime.datetime.now(datetime.UTC).date().isoformat()}"
)

with open("CHANGELOG.md.new", "w") as changelog:
    changelog.write(header)
    changelog.write("\n")
    changelog.write("* please write here")
    changelog.write("\n\n")
