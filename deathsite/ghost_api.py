import os
import json
import requests


class GhostBlog:
    def __init__(self):
        keys_path = os.getenv(
            "KEYS_PATH", os.path.join(os.path.dirname(__file__), "keys.json")
        )
        try:
            with open(keys_path) as k:
                keys = json.load(k)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading keys.json: {e}")
            self.blog_url = "https://blog.death916.xyz"
            self.api_key = ""
            return
        self.blog_url = keys.get("ghost_blog_url", "https://blog.death916.xyz")
        self.api_key = keys.get("ghost_content_api_key", "")

    def get_posts(self):
        if not self.api_key:
            return []

        url = f"{self.blog_url}/ghost/api/content/posts/"
        params = {
            "key": self.api_key,
            "limit": 10,
            "order": "published_at desc",
            "fields": "title,slug,published_at,custom_excerpt",
            "formats": "",
        }

        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            posts = data.get("posts", [])
            formatted = []
            for post in posts:
                formatted.append(
                    {
                        "title": post["title"],
                        "slug": post["slug"],
                        "published_at": post["published_at"][:10],
                        "excerpt": post.get("custom_excerpt", ""),
                        "url": f"{self.blog_url}/{post['slug']}/",
                    }
                )
            return formatted
        except Exception as e:
            print(f"Error fetching Ghost posts: {e}")
            return []
