#
#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2022] MakinaRocks Co., Ltd.
#  All Rights Reserved.
#
#  NOTICE:  All information contained herein is, and remains
#  the property of MakinaRocks Co., Ltd. and its suppliers, if any.
#  The intellectual and technical concepts contained herein are
#  proprietary to MakinaRocks Co., Ltd. and its suppliers and may be
#  covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law. Dissemination
#  of this information or reproduction of this material is
#  strictly forbidden unless prior written permission is obtained
#  from MakinaRocks Co., Ltd.
#
import argparse
import configparser
import os
import subprocess


def main(args):
    print(args.repo_root)
    config = configparser.ConfigParser()
    config.read(os.path.join(args.repo_root, ".gitmodules"))
    for section in config.sections():
        path = config[section]["path"]
        url = config[section]["url"]
        git_args = [url, path]
        branch = config[section].get("branch")
        if branch:
            git_args += ["-b", branch]
        p = subprocess.Popen(["/usr/bin/git", "submodule", "add"] + git_args)
        p.communicate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root")
    args = parser.parse_args()
    main(args)
