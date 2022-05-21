#!python
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

# pylint: disable=line-too-long,missing-function-docstring

import getpass
import http
import platform
import re
import shutil
import sys
from typing import Any, Dict, List

import requests


def input_github_token() -> str:
    return getpass.getpass("Enter Github Personal Acceess Token (PAT): ")


def get_wheel_sys_name_pattern() -> str:
    if sys.platform == "win32":
        return "win_amd64"
    if sys.platform == "linux":
        return "linux_x86_64"
    if sys.platform == "darwin":
        if platform.processor() == "arm":
            return r"macosx_.*_arm64"
        return r"macosx_.*_x86_64"

    raise SystemError(f"Unsupported system platform type: {sys.platform}")


def get_wheel_file_pattern() -> str:
    if sys.version_info.major != 3:
        raise SystemError("Not a Python 3")
    if sys.version_info.minor not in (6, 7, 8, 9):
        raise SystemError(f"Unsupported Python version {sys.version_info.minor}")
    sys_name = get_wheel_sys_name_pattern()
    pattern = rf"mrx_link-.*-cp3{sys.version_info.minor}-.*-{sys_name}.whl"
    return pattern


def get_latest_release_url(token: str) -> str:
    return f"https://{token}:@api.github.com/repos/makinarocks/makina-link/releases/latest"


def get_file_url_by_asset_id(token: str, asset_id: str) -> str:
    return f"https://{token}:@api.github.com/repos/makinarocks/makina-link/releases/assets/{asset_id}"


def get_assets_info(url: str) -> Any:
    resp = requests.get(url)
    if resp.status_code != http.HTTPStatus.OK:
        raise SystemError(f"Response code = {resp.status_code}, message = {resp.text}")
    return resp.json()


def download_file(url: str, local_filename: str) -> None:
    with requests.get(url, stream=True, headers={"Accept": "application/octet-stream"}) as resp:
        with open(local_filename, "wb") as file:
            shutil.copyfileobj(resp.raw, file)


def main() -> None:
    """Download Link installation wheel file according to python version and platform type
    If successful, print path of the downloaded file to standard-output
    """
    token = input_github_token()
    latest_release_url = get_latest_release_url(token)
    info = get_assets_info(latest_release_url)
    assets: List[Dict[str, Any]] = info["assets"]
    pattern = get_wheel_file_pattern()
    for asset in assets:
        matched = re.match(pattern, asset["name"])
        if matched:
            break
    else:
        asset = {}
        print(f"Wheel file pattern: {pattern}")
        print("Current wheel file lists:")
        print([asset["name"] for asset in assets])
        raise SystemError("Can't find wheel file for this system")

    asset_id = asset["id"]
    file_name = asset["name"]
    file_url = get_file_url_by_asset_id(token, asset_id)
    download_file(file_url, file_name)
    print(file_name)


if __name__ == "__main__":
    main()
