import json
import logging
import os
import shutil

import reflex as rx

from deathsite.deathsite import State, page_content

FREE_TIME_DIR = "/mnt/myjfs/gallery/"
ASSETS_DIR = "assets"

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
        for item in self.gallery_items:
            item["thumbnail"] = f"/thumbs/{item['slug']}.png"
            item["file"] = f"/{item['slug']}.html"
        logging.debug(f"get_items: {self.gallery_items}")
        print(f"get_items: {self.gallery_items}")
        return self.gallery_items

    def move_to_assets(self, assets_path=FREE_TIME_DIR):
        if not assets_path:
            return
        for item in self.gallery_items:
            slug = item["slug"]
            
            src_thumb = os.path.join(self.gallery_path, "thumbs", f"{slug}.png")
            if os.path.exists(src_thumb):
                dst_thumb = os.path.join(assets_path, "thumbs", f"{slug}.png")
                os.makedirs(os.path.dirname(dst_thumb), exist_ok=True)
                print(f"copying {src_thumb} to {dst_thumb}")
                shutil.copy(src_thumb, dst_thumb)

            if item.get("type") == "html":
                src_file = os.path.join(self.gallery_path, f"{slug}.html")
                if os.path.exists(src_file):
                    dst_file = os.path.join(assets_path, f"{slug}.html")
                    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                    print(f"copying {src_file} to {dst_file}")
                    shutil.copy(src_file, dst_file)


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
                rx.foreach(State.free_time, lambda f: rx.card(rx.image(src=f["thumbnail"]))),
            ),
        ),
    )
