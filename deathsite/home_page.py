import reflex as rx
from deathsite.deathsite import page_content, YOUTUBE_EMBED_URL, TWITCH_EMBED_URL, GITHUB_URL

@rx.page(route="/")
@rx.page(route="/home")
def home():
     return page_content(
        rx.box(
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
                    rx.text("Stream: ", color="#ffffff"),
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
                        padding="0.5em",
                    ),
                    rx.spacer(
                        min_height="15em"
                    ),  
                    rx.heading(
                        "Contact",
                        size="8",
                        color="#ffffff",
                    ),
                    rx.link(
                        "Email",
                        href="mailto:mail@death916.xyz.com",
                        color="#736E77",
                        size="4",
                        effect="underline",
                    ),
                    padding="2em",
                    spacing="1",
                    height="100%",  
                    align_items="end",
                     
                    width="100%",
                ),
            ),
            
            
            align_items="start",
            width="100%",
        
        )
    )