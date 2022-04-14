from django.shortcuts import render, redirect
from random import choice
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, title):
    content = util.get_entry(title)
    markdowner = Markdown()
    entry = markdowner.convert(content)
    if entry == None:
        entry = "Your requested page was not found!"
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "title": title,
    })

def search(request):
    if request.method == 'POST':
        entries = util.list_entries()
        q = request.POST['q']
        if q in entries:
            return redirect('encyclopedia:display', title=q)
        else:
            results = list(filter(lambda x: q in x, entries))
            return render(request, "encyclopedia/results.html", {'results': results})

def new_page(request):
    if request.method != "POST":
        return render(request, 'encyclopedia/new_entry.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        if title in util.list_entries():
            return render(request, 'encyclopedia/new_entry.html', {'message': "This entry is already in the Wiki. Please try again"})
        util.save_entry(title, content)
        return redirect('encyclopedia:display', title=title)

def edit_entry(request, title):
    if request.method != "POST":
        content = util.get_entry(title)
        markdowner = Markdown()
        entry = markdowner.convert(content)
        return render(request, 'encyclopedia/edit_entry.html', {
            "title": title,
            "entry": entry,
        })
    else:
        entry = request.POST['content']
        util.save_entry(title, entry)
        return redirect('encyclopedia:display', title=title)

def random(request):
    entries = util.list_entries()
    title = choice(entries)
    return redirect('encyclopedia:display', title=title)