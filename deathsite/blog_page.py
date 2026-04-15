import reflex as rx
from deathsite.deathsite import page_content

@rx.page(route="/blog")
def blog():
    return page_content(
        rx.vstack(
            rx.heading("Things", size="5", color="#ffffff"),
            rx.text("Random Musings on what im working on or saw interesting", color="#ffffff"),
            rx.scroll_area(
                rx.flex(
                    rx.markdown(
                        """# April 19 2025

Been using a new IRC client called Halloy. Its written in rust and has a very nice interface. Its pretty much my go to now.

Its made me want to get my rust skills back up again and drop some contributions. Heres the link to the project: [Halloy](https://github.com/squidowl/halloy)

# April 05 2025

## Starting this site

I wanted to finally have a central place for all my doings. Figured now was the time to get a personal site going when I saw the reflex framework for python. I really didnt like always having to drop to JS or something for web"""
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
