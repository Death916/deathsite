# deathsite/deathsite.py
"""personal site for projects/streams"""
import reflex as rx
import datetime


# constants
TWITCH_USERNAME = "Death916"
YOUTUBE_URL = "https://www.youtube.com/@916HS"
YOUTUBE_EMBED_URL = "https://www.youtube.com/embed/D43Ks8fxoz4" 


#styles

NAV_BUTTON_STYLE = {
    "color": "#f8f9fa",
    "font_weight": "500",
    "padding": "10px 15px",
    "border_radius": "4px",
    "transition": "background-color 0.3s ease",
    "_hover": {
        "background_color": "#ffc107",
        "color": "#212529",
        "text_decoration": "none", # Override link hover underline
    },
}

class State(rx.State):
    current_page: str = "Home"
    page_title: str = "Death916's Site" # Added page_title attribute

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
        )
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
                
                spacing="4", # Spacing between nav items
                justify="center",
                align="center",
            ),
            width="100%",
            bg="#212529", # Dark background
            padding="1.5em 0",
            border_bottom="3px solid #6f42c1", # Dark purple accent border
            align="center", # Center heading and nav horizontally
        ),
    )
       

def home():
    return rx.box(
        rx.vstack(
            rx.heading("Home Page", size="3", color="#ffffff"),
            rx.text("This is the home page content.", color="#ffffff"),
            padding="2em",
            spacing="1",
            align_items="start", # Align content to the start (left)
        ),
        rx.vstack(
            rx.heading("Whats New:", size="2", color="#ffffff"),
                rx.text("Latest Stream: ", color="#ffffff"),
                rx.link(
                    "Twitch Stream",
                    href=f"https://www.twitch.tv/{TWITCH_USERNAME}",
                    color="#ffffff",
                    is_external=True,
                      ),
            rx.html(
                f"""
                <iframe width="560" height="315" src="{YOUTUBE_EMBED_URL}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                """
            ),
            align_items="start", # Align content to the start (left)
            ),
        align_items="start", # Align content to the start (left)
        width="100%", # Take up full width
    )


def projects():
    return rx.box(
        rx.vstack(
            rx.heading("Projects Page", size="3", color="#ffffff"),
            rx.text("This is the projects page content.", color="#ffffff"),
            padding="2em",
            spacing="1",
            align_items="start", # Align content to the start (left)
        ),
        align_items="start", # Align content to the start (left)
        width="100%", # Take up full width
    )

def blog():
    return rx.box(
        rx.vstack(
            rx.heading("Blog Page", size="3", color="#ffffff"),
            rx.text("This is the blog page content.", color="#ffffff"),
            padding="2em",
            spacing="1",
            align_items="start", # Align content to the start (left)
        ),
        align_items="start", # Align content to the start (left)
        width="100%", # Take up full width
    )

def videos():
    return rx.box(
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
            align_items="start", # Align content to the start (left)
            ),
        align_items="start", # Align content to the start (left)
        width="100%", # Take up full width
        
    )

def index():
    return rx.box(
        header(),
        rx.container(
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
                            rx.vstack(
                                rx.heading("Welcome to My Personal Site", size="1", color="#ffffff"),
                                rx.text("This is a personal site for my projects and streams.", color="#ffffff"),
                                rx.text(f"Current time: {State.current_time}", color="#ffffff"),
                                padding="2em",
                                spacing="2",
                                align_items="start", # Align content to the start (left)
                            ),
                        )
                    )
                )
            ),
            # Take up full width
            align_items="start", # Align content to the start (left)
        ),
        # Take up full width
    )
    

app = rx.App()
app.add_page(
    index,
    title=State.page_title,
)
