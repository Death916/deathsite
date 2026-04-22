import reflex as rx

config = rx.Config(
    app_name="deathsite",
    tailwind=None,
    # frontend_port=3011,
    api_url="https://death916.xyz",
    cors_allowed_origins=[
        "https://death916.xyz",
        "https://death916.xyz/",
    ],
    # backend_port=8005,

)
