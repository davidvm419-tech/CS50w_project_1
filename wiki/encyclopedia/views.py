from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import util
# Library to convert md to html
from markdown2 import Markdown
markdowner = Markdown()
# Regex to get matches on query
import re

# Class to search query
class SearchEntry(forms.Form):
    q = forms.CharField(label="Search Query")


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


# Function to get a query from the search bar


def search_query(request):
    if request.method == "POST":
        form = SearchEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["q"]
            entry = util.get_entry(title)
            if entry:
                return redirect("entry", title=title)
            else:
                entries = util.list_entries()
                matches = []
                for entry in entries:
                    if re.search(title, entry, re.IGNORECASE):
                        matches.append(entry)
                return render(request, "encyclopedia/search.html", {
                    "entries": matches,
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })