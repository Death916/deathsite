import reflex as rx
from deathsite.deathsite import page_content, YOUTUBE_URL, State


@rx.page(route="/videos", on_load=State.update_videos)
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
            rx.flex(
                rx.foreach(
                    State.yt_video_list,
                    lambda video_url: rx.card(
                        rx.html(
                            f"""<iframe 
                                width="350" 
                                height="200" 
                                src="https://www.youtube.com/embed/{video_url.split('v=')[1]}" 
                                title="YouTube video player" 
                                frameborder="0" 
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                                allowfullscreen>
                            </iframe>"""
                        ),
                        width="auto",
                    ),
                ),
                direction="row",
                wrap="wrap",
                spacing="4",
                justify="center",
                align="start",
                padding="1em",
                width="100%",
            ),
            align_items="center",
            spacing="4",
            width="100%",
        )
    )
