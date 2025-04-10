# deathsite/deathsite.py
"""personal site for projects/streams"""
import reflex as rx
import datetime


# constants
TWITCH_USERNAME = "Death916"
YOUTUBE_URL = "https://www.youtube.com/@916HS"
YOUTUBE_EMBED_URL = "https://www.youtube.com/embed/D43Ks8fxoz4"
TWITCH_CHAT_URL = f"https://www.twitch.tv/embed/{TWITCH_USERNAME}/chat?parent=localhost&muted=true"
TWITCH_EMBED_URL = f"https://player.twitch.tv/?video=2424240989&parent=localhost&autoplay=false"
GITHUB_URL = "https://github.com/Death916"

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

    def update_time(self):
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def go_to_page(self, page: str):
        self.current_page = page


def navigation_button(text: str) -> rx.Component:
    """Creates a navigation button with conditional active styling."""
    active_style_dict = {
        "background_color": "#ffc107",
        "color": "#212529",
        "text_decoration": "none",
    }
    return rx.button(
        text,
        on_click=lambda: State.go_to_page(text),
        variant="soft",
        style=rx.cond(
            State.current_page == text,
            {**NAV_BUTTON_STYLE, **active_style_dict},
            NAV_BUTTON_STYLE,
        ),
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
        position="sticky",  # Stick to the bottom
        bottom="0",  # Stick to the bottom
        bg="",  # 
    )


def home():
    return rx.box(
        rx.vstack(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Welcome to my domain",
                        color="#ffffff",
                        style={"text_align": "center"},
                    ),
                    rx.text(
                        "This is a personal site for my projects and streams. Never really made a full site for myself before so this will be a work in progress.",
                        color="#ffffff",
                        style={"text_align": "center"},
                    ),
                    spacing="1",
                    width="100%",
                    align_items="center",
                    justify="center",
                ),
                padding="2em",
                width="100%",
                align_items="center",
                justify="center",
            ),
            align_items="center",
            justify="center",
            width="100%",
        ),
        rx.hstack(
            rx.vstack(
                rx.heading("Whats New:", size="8", color="#ffffff"),
                rx.html(
                    f"""
                    <iframe width="350" height="200" src="{YOUTUBE_EMBED_URL}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    """
                ),
                rx.text("Latest Stream: ", color="#ffffff"),
                rx.html(
                    f"""
                    <iframe width="350" height="200" src="{TWITCH_EMBED_URL}" title="Twitch video player" frameborder="0" autoplay="false" allowfullscreen></iframe>

                    """
                ),
                align_items="start",
                spacing="2",
                justify="start",
            
            ),
            rx.vstack(
                rx.heading(
                    "Links",
                    size="8",
                    color="#ffffff",
                ),
                rx.link(
                    "GitHub",
                    href=GITHUB_URL,
                    color="#736E77",
                    size="4",
                    effect="underline",
                    is_external=True,
                ),
                align_items="end",
                justify="end",
                width="100%",
            ),
            
        ),
         
        
        align_items="start",
        width="100%",
       
    )


def page_content(content):
    ## Wraps the content in a box with a dark background and padding
    return rx.box(
        rx.vstack(
            content,
            align_items="center",
            justify="center",
            width="100%",
        ),
        width="100%",
    )


def projects():
    return page_content(
        rx.vstack(
            rx.heading("Projects Page", size="3", color="#ffffff"),
            rx.text("This is the projects page content.", color="#ffffff"),
            padding="2em",
            spacing="1",
        )
    )


def blog():
    return page_content(
        rx.vstack(
            rx.heading("Things", size="5", color="#ffffff"),
            rx.text("Random Musings on what im working on or saw interesting", color="#ffffff"),
            rx.scroll_area(
                rx.flex(
                    rx.markdown(
                         "# April 05 2025"
                        "\n\n## Starting this site\n\n"
                        "I wanted to finally have a central place for all my doings. Figured now was the time to get a personal site going when I saw the reflex framework for python. I really didnt like always having to drop to JS or something for web"
                        

                        
                    ),
                    
                    direction="column",
                    spacing="4",
                ),
    type="always",
    scrollbars="vertical",
    style={"height": 580},
            ),
            padding="2em",
            spacing="1",

        
        )
    )


def videos():
    return page_content(
        rx.vstack(
            rx.heading("Videos Page", size="3", color="#ffffff"),
            rx.text("NEWEST VIDEOS:", color="#ffffff"),
            rx.link(
                "YouTube Channel",
                href=YOUTUBE_URL,
                color="#ffffff",
                is_external=True,
            ),
            padding="2em",
            spacing="1",
        )
    )


def index() -> rx.Component:
    return rx.box(
        header(),
        rx.box(
            rx.cond(
                State.current_page == "Home",
                home(),
                rx.cond(
                    State.current_page == "Videos",
                    videos(),
                    rx.cond(
                        State.current_page == "Blog",
                        blog(),
                        rx.cond(
                            State.current_page == "Projects",
                            projects(),
                            home()  # default case
                        )
                    )
                )
            ),
            width="100%",
            flex_grow="1",
        ),
        footer(),
        width="100%",
        display="flex",
        flex_direction="column",
        min_height="100vh",
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="violet",  # Dark purple accent color
        background_color="#212529",  # Dark background color
        text_color="#ffffff",  # Light text color
    )
)
app.add_page(
    index,
    title=State.page_title,
)


# TODO add guild page
