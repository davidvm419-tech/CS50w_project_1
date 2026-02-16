from django.shortcuts import render

from . import util

# Library to convert md to html
from markdown2 import Markdown
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Function to get entries of the wiki


def entry(request, title):
    content = util.get_entry(title)
    if not content:
        return render(request,"encyclopedia/error.html", {
            "title": title.capitalize()
        })
    else:
        html_content = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "content": html_content
        })
