import reflex as rx
from deathsite.deathsite import page_content, YOUTUBE_URL

@rx.page(route="/videos")
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
