"""Export a local print-ready HTML handbook using Playwright Chromium."""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import Error, sync_playwright


def launch_browser(chromium, channel):
    if channel is not None:
        return chromium.launch(channel=channel)

    candidates = ("msedge", "chrome", None) if sys.platform == "win32" else (None,)
    failures = []
    for candidate in candidates:
        try:
            return chromium.launch(channel=candidate)
        except Error as error:
            failures.append(f"{candidate or 'Playwright Chromium'}: {str(error).splitlines()[0]}")

    raise SystemExit("Unable to start a PDF export browser.\n" + "\n".join(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--channel", help="Use a specific installed Playwright Chromium channel.")
    args = parser.parse_args()
    source = args.html.resolve(strict=True)
    target = args.pdf.resolve()
    if source.suffix.lower() not in {".htm", ".html"} or target.suffix.lower() != ".pdf":
        parser.error("Expected an HTML input and a PDF output.")
    if target.exists():
        parser.error(f"Choose a new output filename. Already exists: {target}")

    with sync_playwright() as playwright:
        browser = launch_browser(playwright.chromium, args.channel)
        failures = []
        page = browser.new_page(offline=True)
        page.on("requestfailed", lambda request: failures.append(request.url))
        page.emulate_media(media="print")
        page.goto(source.as_uri(), wait_until="load")
        page.evaluate("""async () => {
            for (const image of document.images) image.loading = 'eager';
            await Promise.all(Array.from(document.images, image => image.decode()));
            await document.fonts.ready;
        }""")
        pdf = page.pdf(format="A4", print_background=True, prefer_css_page_size=True)
        browser.close()
    if failures:
        raise SystemExit("Failed resources: " + ", ".join(failures))
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as output:
        output.write(pdf)
    print(target)


if __name__ == "__main__":
    main()
