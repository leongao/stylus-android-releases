"""Generate the domestic update feed exclusively from published, signed APKs."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.request import urlopen
from shutil import copyfileobj

REPO = "leongao/stylus-android-releases"
CERT = "9d390abd726a7711bb1d5d31b69dc31c4377d47fc9128ca695fc9a1e696314be"


def output(*args):
    return subprocess.check_output(args, text=True)


def candidates(releases):
    prefix = f"https://github.com/{REPO}/releases/download/"
    for release in releases:
        if release["draft"] or release["prerelease"] or not release["published_at"]:
            continue
        for asset in release["assets"]:
            name = asset["name"].lower()
            if (asset["state"] == "uploaded" and name.startswith("peno") and name.endswith(".apk")
                    and asset["browser_download_url"].startswith(prefix)):
                yield asset["browser_download_url"]


def metadata(badging, resources, certs):
    package = re.search(r"^package: name='com\.leon\.still' versionCode='([0-9]+)' versionName='([^']+)'", badging, re.M)
    production = re.search(r'string/peno_api_origin\s+\(\) "https://peno-cn\.somestuff\.app"', resources)
    signers = re.findall(r"^Signer #\d+ certificate SHA-256 digest: (\w+)$", certs, re.M)
    if (not package or not production or signers != [CERT] or "application-debuggable" in badging
            or "com.android.vending.BILLING" in badging):
        return None
    code = int(package[1])
    return {"versionName": package[2], "versionCode": code} if code > 0 else None


def generate():
    sdk = Path(os.environ["ANDROID_HOME"]) / "build-tools"
    tools = max((p for p in sdk.iterdir() if re.fullmatch(r"\d+(\.\d+)+", p.name)),
                key=lambda p: tuple(map(int, p.name.split("."))))
    pages = json.loads(output("gh", "api", "--paginate", "--slurp", f"repos/{REPO}/releases?per_page=100"))
    latest = None
    with tempfile.TemporaryDirectory() as temp:
        apk = Path(temp) / "candidate.apk"
        for url in candidates(r for page in pages for r in page):
            with urlopen(url, timeout=60) as response, apk.open("wb") as dest:
                copyfileobj(response, dest)
            try:
                result = metadata(output(tools / "aapt", "dump", "badging", apk),
                                  output(tools / "aapt2", "dump", "resources", apk),
                                  output(tools / "apksigner", "verify", "--print-certs", apk))
            except subprocess.CalledProcessError:
                print(f"Skipping invalid APK: {url}")
                continue
            if result and (latest is None or result["versionCode"] > latest["versionCode"]):
                latest = {**result, "url": url}
    return {"release": latest}


if __name__ == "__main__":
    Path("peno-cn-update.json").write_text(json.dumps(generate(), ensure_ascii=False, indent=2) + "\n")
