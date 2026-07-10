import json
import os
import shutil

import reflex as rx
import logging

from deathsite.deathsite import State, page_content

FREE_TIME_DIR = "/mnt/myjfs/gallery/"
ASSETS_DIR = "."  # set this to your Reflex assets dir for server use

"""
manifest.json schema
[
     {
       "slug": "abyssal-bloom",
       "title": "Abyssal Bloom",
       "type": "html",
       "description": "Generative art HTML",
       "thumbnail": "/gallery/thumbs/abyssal-bloom.png",
       "file": "/gallery/abyssal-bloom.html",
       "created": "2026-07-09",
       "tags": ["html"],
       "safety_checked": true,
       "safety_checked_at": "2026-07-09T11:11:17Z"
     }
   ]
"""


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

class GetFreeTime:
    def __init__(self, gallery_path=ASSETS_DIR):
        self.gallery_path = gallery_path
        self.manifest_path = os.path.join(gallery_path, "manifest.json")
        self.gallery_items = []
        if not os.path.exists(self.manifest_path):
            raise FileNotFoundError("manifest.json not found")
        with open(self.manifest_path, "r") as f:
            self.gallery_items = json.load(f)

    def get_items(self) -> list[dict]:
        logging.debug(f"get_items: {self.gallery_items}")
        return self.gallery_items

    def move_to_assets(self, assets_path=FREE_TIME_DIR):
        if not assets_path:
            return
        for item in self.gallery_items:
            src = os.path.join(self.gallery_path, item["file"])
            dst = os.path.join(assets_path, item["file"])
            shutil.copy(src, dst)


@rx.page(route="/free_time", on_load=State.load_free_time)
def free_time():
    return page_content(
        rx.vstack(
            rx.heading(
                "Sometimes I give my agents some 'Free Time' this is what they come up with",
                size="5",
                color="#ff2020",
                justify="center",
                align="center",
            ),
            rx.flex(
                rx.foreach(State.free_time, lambda f: rx.card(f["thumbnail"])),
            ),
        ),
    )
