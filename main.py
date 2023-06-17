from reactpy import component, html;
from reactpy.backend.fastapi import configure;
from fastapi import FastAPI;

@component
def Item(text):
    return html.li({
        "class": "item",
        "style": {
            "color": "blue"
        }
    }, text)
    

@component
def HelloWorld():
    return html.div(
        html.h1("Lista de taeras"),
        html.ul(
            Item("Tarea con componente 1"),
            Item("Tarea con componente 2"),
        )
    );

app = FastAPI();
configure(app, HelloWorld);
