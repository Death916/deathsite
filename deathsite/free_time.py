import reflex as rx
from pydantic import BaseModel

from deathsite.deathsite import page_content, State

FREE_TIME_MANIFEST_FILE = ""
FREE_TIME_DIR = ""

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

    def  get_free_time(manifest,fol )

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
                rx.foreach(
                    State.free_time,
                    lambda f: rx.box(
                    
                    )
                ),
            ),
        ),
    )
