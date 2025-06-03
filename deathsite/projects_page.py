import reflex as rx
from deathsite.deathsite import page_content, State 

def render_project(project: dict) -> rx.Component:
    """Renders a single project card."""
    return rx.vstack(
        rx.heading(project["title"], size="5"),
        rx.badge(
            project["status"],
            color_scheme=rx.cond(
                project["status"] == "Ongoing", "blue",
                rx.cond(
                    project["status"] == "Completed", "green",
                    rx.cond(
                        project["status"] == "Planning", "yellow",
                        rx.cond(
                            project["status"] == "Paused", "red",
                            "gray"
                        )
                    )
                )
            ),
            margin_y="0.3em",
        ),
        rx.text(project["description"], margin_y="0.5em"),
        rx.cond(
            project["link"],
            rx.link(project["title"], href=project["link"], is_external=True),
            rx.fragment(),
        ),
        padding_bottom="1.5em", margin_bottom="1.5em",
        border_bottom="1px solid #e9ecef", align_items="start", width="100%",
        _last={"border_bottom": "none"},
    )


def github_graph():
    return rx.box(
        rx.heading("GitHub Contributions", size="5", margin_bottom="1em"),
        rx.html(
            #get the graph from github specifically
            """
            <img src="https://ghchart.rshah.org/Death916" alt="GitHub Chart" style="width: 100%; height: auto;">

            """,
        ),
        padding="2em",
        spacing="1",
    )


@rx.page(route="/projects")
def projects() -> rx.Component:
    """Renders the projects page."""
    return page_content( 
            rx.vstack(
                rx.box(
                
            
                    rx.heading("Projects", size="7", margin_bottom="1em"),
                    rx.cond(
                        State.projects,
                        rx.foreach(State.projects, render_project),
                        rx.text("No projects listed yet."),
                        
                    ),
                    padding="2em",
                    spacing="1",
                    width="100%",
                    align_items="start",
                ),
            rx.hstack(
                
                github_graph(),
                spacing="2",
                align_items="center",
                justify="center",
            ),
            align_items="start", width="100%",
            
        )
    )

