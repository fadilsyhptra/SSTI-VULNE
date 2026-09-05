from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import jinja2
import os

app = FastAPI()

def get_content():
    template_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get('/')
async def loads(name: str = Query(default = "Fadil")):
    html_raw = get_content()
    templateCode = html_raw.replace("{name}", name)

    rendered_html = jinja2.Template(templateCode).render()
    return HTMLResponse(content=rendered_html)