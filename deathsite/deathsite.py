# deathsite/deathsite.py
"""personal site for projects/streams"""
import reflex as rx
import datetime
import videos
import asyncio




# constants
TWITCH_USERNAME = "Death916"
YOUTUBE_URL = "https://www.youtube.com/@916HS"
YOUTUBE_EMBED_URL = "https://www.youtube.com/embed/D43Ks8fxoz4"
TWITCH_CHAT_URL = f"https://www.twitch.tv/embed/{TWITCH_USERNAME}/chat?parent=localhost&muted=true"
TWITCH_EMBED_URL = f"https://player.twitch.tv/?channel={TWITCH_USERNAME}&parent=localhost&muted=true"
GITHUB_URL = "https://github.com/Death916"
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
    }, 
    {
        "title": "Death916's Guild",
        "description": "My guild page.",
        "status": "Planning",
        "link": "/guild",
    },
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

class State(rx.State):
    current_page: str = "Home"
    page_title: str = "Death916's Site"  # Added page_title attribute
    current_time: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    projects: list[dict[str, str]] = PROJECTS_DATA
    current_yt_video: str = ""

    def update_time(self):
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def go_to_page(self, page: str):
        self.current_page = page

    @rx.event(background=True)
    async def update_current_yt_video(self):
        """Fetch the current YouTube video in the background."""
        yt = videos.Youtube()
        yt.get_newest_video()
        self.current_yt_video = yt.current_yt_video
        await asyncio.sleep(86400)  # Update every 60 seconds
    

   
        
def navigation_button(text: str) -> rx.Component:
    """Creates a navigation button with proper routing."""
    route = text.lower() if text != "Home" else "/"
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
                "minHeight": "200px",  # Reduced from 300px to 200px
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
        padding="0.5em",  # Reduced padding
        border_top="1px solid #dee2e6",
        width="100%",
        text_align="center",  # Center the text
        position="fixed",  # Stick to the bottom
        bottom="0",  # Stick to the bottom
        bg="",  # 
    )

# (setq eldoc-echo-area-use-multiline-p nil)
def page_content(content):
    ## Wraps the content in a box with a dark background and padding
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
            "backgroundAttachment": "fixed",  # This makes the background stay fixed while scrolling
            "minHeight": "100vh",  # This ensures the background covers the full viewport height
        },
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="violet", 
        background_color="#212529",  # Dark background color
        text_color="#ffffff",  # Light text color
    )
)

from deathsite.home_page import home
from deathsite.projects_page import projects
from deathsite.blog_page import blog
from deathsite.videos_page import videos

app.add_page(home)
app.add_page(projects)
app.add_page(blog)
app.add_page(videos)


# TODO add guild page
# TODO add unzip to requirements for system?
# TODO move project data to a json file or something

# TODO add live printer stream
# TODO update videos using youtube api
