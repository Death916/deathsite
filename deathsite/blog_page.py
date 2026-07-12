import reflex as rx
from deathsite.deathsite import State, page_content


@rx.page(route="/blog", on_load=State.update_blog_posts)
def blog():
    return page_content(
        rx.vstack(
            rx.heading("Things", size="5", color="#ffffff"),
            rx.text(
                "Random Musings on what im working on or saw interesting",
                color="#ffffff",
            ),
            rx.scroll_area(
                rx.foreach(
                    State.blog_posts,
                    lambda post: rx.link(
                        rx.card(
                            rx.vstack(
                                rx.text(
                                    post["published_at"],
                                    color="#6c757d",
                                    font_size="0.85em",
                                ),
                                rx.heading(
                                    post["title"],
                                    size="4",
                                    color="#ffffff",
                                ),
                                rx.cond(
                                    post["excerpt"],
                                    rx.text(
                                        post["excerpt"],
                                        color="#adb5bd",
                                        font_size="0.9em",
                                    ),
                                ),
                                spacing="1",
                            ),
                            width="100%",
                            bg="rgba(255,255,255,0.05)",
                            _hover={"bg": "rgba(255,255,255,0.1)"},
                        ),
                        href=post["url"],
                        is_external=True,
                        text_decoration="none",
                        width="100%",
                    ),
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 580},
            ),
            padding="2em",
            spacing="1",
        )
    )
