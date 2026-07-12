# deathsite/deathsite.py
"""personal site for projects/streams"""

import asyncio
import datetime
import os

import reflex as rx
from pydantic import BaseModel

from deathsite.videos import Youtube
from deathsite.ghost_api import GhostBlog

UMAMI_WEBSITE_ID = os.getenv("UMAMI_WEBSITE_ID", "")
UMAMI_SCRIPT_URL = os.getenv("UMAMI_SCRIPT_URL", "")
TWITCH_USERNAME = "Death916"
YOUTUBE_URL = "https://www.youtube.com/@916HS"
YOUTUBE_EMBED_URL = "https://www.youtube.com/embed/D43Ks8fxoz4"
TWITCH_CHAT_URL = (
    f"https://www.twitch.tv/embed/{TWITCH_USERNAME}/chat?parent=death916.xyz&muted=true"
)
TWITCH_EMBED_URL = f"https://player.twitch.tv/?channel={TWITCH_USERNAME}&parent=death916.xyz&muted=true"
GITHUB_URL = "https://github.com/Death916"
GHOST_BLOG_URL = os.getenv("GHOST_BLOG_URL", "https://blog.death916.xyz")
PROJECTS_DATA = [
    {
        "title": "Death916's Site",
        "description": "This site is a personal portfolio and blog.",
        "status": "Ongoing",
        "link": "https://github.com/Death916/deathsite",
    },
    {
        "title": "Deathclock",
        "description": "Sports and weather clock and dashboard",
        "status": "Ongoing",
        "link": "https://github.com/Death916/deathclock",
        "hardware": {
            "Screen": "https://amzn.to/4xk3fpP",
            "Printer": "https://amzn.to/3S7pDme",
        },
    },
    {
        "title": "emailtrade",
        "description": "Automatically buy/sell crypto from TradingView alert email",
        "status": "Paused",
        "link": "https://github.com/Death916/emailtrade",
    },
    {
        "title": "mining_diff_scraper",
        "description": "Gets historical mining difficulty, nethash and other relevant data for crypto currencies",
        "status": "Completed",
        "link": "https://github.com/Death916/mining_diff_scraper",
    },
    {
        "title": "c2cscrape",
        "description": "Scrape archived episodes of c2c and create local feed for use in podcast app",
        "status": "Completed",
        "link": "https://github.com/Death916/c2cscrape",
    },
    {
        "title": "combo",
        "description": "IRC bot to call people out for monologue",
        "status": "Completed",
        "link": "https://github.com/Death916/combo",
    },
    {
        "title": "minestart",
        "description": "Automatically start crypto miner on PC startup and stop when games are opened",
        "status": "Completed",
        "link": "https://github.com/Death916/minestart",
    },
    # {
    #    "title": "Death916's Guild",
    #     "description": "My guild page.",
    #    "status": "Planning",
    #    "link": "https://guildsofwow.com/restoration",
    # },
]

# styles

NAV_BUTTON_STYLE = {
    "color": "#f8f9fa",
    "font_weight": "500",
    "padding": "10px 15px",
    "border_radius": "4px",
    "transition": "background-color 0.3s ease",
    "_hover": {
        "background_color": "#6f42c1",  # Dark purple on hover
        "color": "#212529",
        "text_decoration": "none",  # Override link hover underline
    },
}


class Project(BaseModel):
    title: str
    description: str
    status: str
    link: str
    hardware: dict[str, str] = {}


class State(rx.State):
    current_page: str = "Home"
    page_title: str = "Death916's Site"
    current_time: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    projects: list[Project] = PROJECTS_DATA
    current_yt_video: str = ""
    last_yt_fetch: str = ""
    yt_video_list: list[str] = []
    free_time: list[dict] = []
    blog_posts: list[dict] = []

    def update_time(self):
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    async def load_free_time(self):
        try:
            from deathsite.free_time import GetFreeTime, FREE_TIME_DIR

            if os.path.exists(FREE_TIME_DIR):
                GetFreeTime(gallery_path=FREE_TIME_DIR).move_to_assets(assets_path="assets")
                if os.path.exists(".web/public"):
                    GetFreeTime(gallery_path=FREE_TIME_DIR).move_to_assets(assets_path=".web/public")

            self.free_time = GetFreeTime().get_items()
        except FileNotFoundError as e:
            print(f"Error loading free time manifest: {e}")
            self.free_time = []

    @rx.var
    def selected_project(self) -> dict:
        slug = self.router.page.params.get("slug", "")
        for item in self.free_time:
            if item.get("slug") == slug:
                return item
        return {}

    @rx.var
    def selected_project_tags(self) -> list[str]:
        return self.selected_project.get("tags", [])

    @rx.var
    def selected_project_forgejo_url(self) -> str:
        if "link" in self.selected_project and self.selected_project["link"]:
            return self.selected_project["link"]
        slug = self.selected_project.get("slug", "")
        if not slug:
            return ""
        return f"https://git.death916.xyz/death916/freetime/src/branch/main/projects/{slug}"

    def go_to_page(self, page: str):
        self.current_page = page

    @rx.event(background=True)
    async def update_current_yt_video(self):
        """Fetch the current YouTube video in the background."""
        yt = Youtube()
        yt.get_newest_video()
        self.current_yt_video = yt.current_yt_video
        await asyncio.sleep(600)  # Update every 10 minutes (600 seconds)

    async def update_yt_video(self):
        today = datetime.date.today().isoformat()
        if self.last_yt_fetch != today or not self.current_yt_video:
            yt = Youtube()
            url = yt.get_current_yt_video()
            self.current_yt_video = url
            self.last_yt_fetch = today

    async def update_videos(self):
        yt_instance = Youtube()
        video_urls = yt_instance.get_last_5_yt_videos()
        self.yt_video_list = video_urls
        # look into rx.background for background updates

    async def update_blog_posts(self):
        ghost = GhostBlog()
        self.blog_posts = ghost.get_posts()

    def get_youtube_embed_url(self, watch_url: str) -> str:
        """Converts a YouTube watch URL to an embed URL."""
        if not isinstance(watch_url, str):
            return "about:blank"
        try:
            if "v=" in watch_url:
                video_id_part = watch_url.split("v=")[1]
                video_id = video_id_part.split("&")[
                    0
                ]  # Remove any other params like &list=
                return f"https://www.youtube.com/embed/{video_id}"
            return "about:blank"
        except Exception:
            return "about:blank"


def navigation_button(text: str) -> rx.Component:
    """Creates a navigation button with proper routing."""
    route = f"/{text.lower()}" if text != "Home" else "/"
    return rx.link(
        text,
        href=route,
        style=NAV_BUTTON_STYLE,
    )


def header() -> rx.Component:
    """Site header and navigation."""
    return rx.box(
        rx.vstack(
            rx.heading("Death916", size="8", color="#ffffff", padding_bottom="0.5em"),
            rx.hstack(
                navigation_button("Home"),
                navigation_button("Videos"),
                navigation_button("Blog"),
                navigation_button("Projects"),
                navigation_button("Free_Time"),
                spacing="4",
                justify="center",
                align="center",
            ),
            width="100%",
            padding="1.5em 0",
            border_bottom="3px solid #6f42c1",
            align="center",
            style={
                "background": "linear-gradient(rgba(33, 37, 41, 0.7), rgba(33, 37, 41, 0.7)), url('/header.png')",
                "backgroundSize": "cover",
                "backgroundPosition": "center",
                "backgroundRepeat": "no-repeat",
                "minHeight": "200px",
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "center",
            },
        ),
    )


def footer() -> rx.Component:
    return rx.box(
        rx.text(
            f"© {datetime.datetime.now().year} Death916 - Powered by Reflex",
            color="#6c757d",
            font_size="0.9em",
        ),
        padding="0.5em",
        border_top="1px solid #dee2e6",
        width="100%",
        text_align="center",
        position="fixed",
        bottom="0",
        bg="",
    )


def page_content(content):
    return rx.box(
        rx.vstack(
            rx.box(
                header(),
                padding="1em",
                width="100%",
                align_items="center",
            ),
            rx.box(
                content,
                align_items="center",
                justify="center",
                width="100%",
                padding="2em",
            ),
            rx.box(
                footer(),
                padding="1em",
                width="100%",
                align_items="end",
                justify="end",
            ),
        ),
        style={
            "background": "linear-gradient(rgba(33, 37, 41, 0.92), rgba(33, 37, 41, 0.92)), url('/header.png')",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "backgroundRepeat": "no-repeat",
            "backgroundAttachment": "fixed",
            "minHeight": "100vh",  # This ensures the background covers the full viewport height
        },
    )


from deathsite.blog_page import blog
from deathsite.free_time import free_time, view_project
from deathsite.home_page import home
from deathsite.projects_page import projects
from deathsite.videos_page import videos

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="violet",
        background_color="#212529",
        text_color="#ffffff",  # Light text color
    ),
    head_components=[
        rx.script(
            src=UMAMI_SCRIPT_URL,
            custom_attrs={
                "data-website-id": UMAMI_WEBSITE_ID,
                "defer": "true",
            },
        )
    ]
    if UMAMI_SCRIPT_URL and UMAMI_WEBSITE_ID
    else [],
)


app.add_page(home)
app.add_page(projects)
app.add_page(blog)
app.add_page(videos)
app.add_page(free_time)
app.add_page(view_project)

# TODO add guild page
# TODO add unzip to requirements for system?
# TODO move project data to a json file or something

# TODO add live printer stream
