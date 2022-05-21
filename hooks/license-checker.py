#!/usr/bin/env python3
# MAKINAROCKS CONFIDENTIAL
# ________________________
#
# [2017] - [2022] MakinaRocks Co., Ltd.
# All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of MakinaRocks Co., Ltd. and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to MakinaRocks Co., Ltd. and its suppliers and may be
# covered by U.S. and Foreign Patents, patents in process, and
# are protected by trade secret or copyright law. Dissemination
# of this information or reproduction of this material is
# strictly forbidden unless prior written permission is obtained
# from MakinaRocks Co., Ltd.


import argparse
import os
import re
import subprocess
from datetime import datetime as dt
from typing import Any, Optional


# reference by https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/util.py
class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd: str, retcode: Optional[int] = 0, **kwargs: Any) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="license-checker")
    parser.add_argument("filenames", nargs="*")
    parser.add_argument("--license-file-path", type=str, default="./LICENSE")
    parsed = parser.parse_args()

    content: Optional[str] = None
    pattern = ""
    license_txt = ""
    recent = f"{str(dt.now().year)}"

    with open(parsed.license_file_path, "r", encoding="utf-8") as f:
        for line in f:
            pattern += r"^.*" + line.strip() + r".*$\n"
            license_txt += "# " + line.strip() + "\n"

    license_txt = license_txt.replace("\\", "")
    license_txt = license_txt.replace("[d{4}]", f"[{recent}]")

    for filename in parsed.filenames:
        if filename.endswith(".ipynb"):
            with open(filename, "r", encoding="utf-8") as fp:
                content = fp.read()
                if not re.search(pattern, content, re.MULTILINE):
                    raise RuntimeError(f'File "{filename}" does not contain correct license clauses!')

        elif filename.endswith(".py"):
            if os.path.basename(filename) == "__init__.py":
                continue
            with open(filename, "r+", encoding="utf-8") as fp:
                write_offset = 0
                content = fp.readlines()
                if len(content):
                    shell_info = content[0]
                    if re.search("#!/.*", shell_info):
                        write_offset += len(shell_info)
                        content.pop(0)

                content = "".join(content)
                fp.seek(write_offset)

                print("Recent info is", not re.search(recent, content))

                if not re.search(pattern, content, re.MULTILINE):
                    fp.write(license_txt + "\n" + content)

                elif not re.search(f"\[{recent}\]", content):
                    start, _ = re.search("- \[\d{4}\]", content).span()
                    fp.seek(write_offset + start)
                    fp.write(f"- [{recent}]")
