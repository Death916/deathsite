import json
import os
import shutil

import reflex as rx
from pydantic import BaseModel

from deathsite.deathsite import page_content, State

FREE_TIME_DIR = "/mnt/myjfs/gallery/"
ASSETS_DIR = ""

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


# test with files in assets first
class GetFreeTime:
    def __init__(self, gallery_path=FREE_TIME_DIR):
        self.gallery_path = gallery_path
        self.manifest_path = os.path.join(gallery_path, "manifest.json")
        self.gallery_items = []
        if not os.path.exists(self.manifest_path):
            raise FileNotFoundError("manifest.json not found")
        with open(self.manifest_path, "r") as f:
            data = json.load(f)
            for item in data:
                self.gallery_items.append(item)

    def move_to_assets(self, assets_path=ASSETS_DIR):
        for item in self.gallery_items:
            src = os.path.join(self.gallery_path, item["file"])
            dst = os.path.join(assets_path, item["file"])
            shutil.copy(src, dst)


class FreeTime(BaseModel):
    slug: str
    title: str
    type: str
    description: str
    thumbnail: str | None = None
    file: str | None = None
    created: str | None = None
    tags: list[str] = []
    safety_checked: bool | None = None
    safety_checked_at: str | None = None

    def parse_manifest(self, data: dict):
        self.slug = data.get("slug")
        self.title = data.get("title")
        self.type = data.get("type")
        self.description = data.get("description")
        self.thumbnail = data.get("thumbnail")
        self.file = data.get("file")
        self.created = data.get("created")
        self.tags = data.get("tags", [])
        self.safety_checked = data.get("safety_checked")
        self.safety_checked_at = data.get("safety_checked_at")


@rx.page(route="/free_time")
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
                rx.foreach(State.free_time, lambda f: rx.box()),
            ),
        ),
    )
