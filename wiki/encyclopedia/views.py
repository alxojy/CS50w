from django.shortcuts import render
from django.http import Http404
from django import forms
import markdown2
from random import randrange

from . import util

class SearchForm(forms.Form): # lhs search form
    search = forms.CharField(label='', 
    widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia'}))

class TitleForm(forms.Form):
    title = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder':'Enter title'}))

class ContentForm(forms.Form):
    content = forms.CharField(label='',
    widget=forms.Textarea(attrs={'placeholder':'Enter content'}))

def index(request):
    query = ""
    res = []
    
    if request.method == "POST": # search bar
        form = SearchForm(request.POST)

        if form.is_valid():
            query = form.cleaned_data["search"]

            for title in util.list_entries():
                if query.lower() == title.lower(): # found exact match
                    return wiki_title(request, title) # redirect to wiki/[query]

                if query.lower() in title.lower(): # substring match - find all matches
                    res.append(title)

        if res != []: # all results with substring 
            return render(request, "encyclopedia/search.html", {
                "results":res,
                "form": SearchForm()
            })
        else: 
            return wiki_title(request, query) # error 404

    else: # home page. list all entries
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form": SearchForm()
        })

# entry page for wiki/[title]
def wiki_title(request, title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/404.html", {
                "message": "Requested page was not found"}) # resource is already available
    else:
        return render(request, "encyclopedia/title.html", {
            "title":title.capitalize(),
            "entry":markdown2.markdown(util.get_entry(title)),
            "form": SearchForm()
        })

def new(request):
    title_form = TitleForm(request.POST)
    content_form = ContentForm(request.POST)

    if request.method == "POST":
        if title_form.is_valid() and content_form.is_valid():
            title = title_form.cleaned_data["title"]
            content = content_form.cleaned_data["content"]

            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/404.html", {
                "message": "Entry has already been created for this topic"}) # resource is already available
            else:
                util.save_entry(title, '#' + title + '\n' + content)
                return wiki_title(request, title)
    else:
        return render(request, "encyclopedia/new.html", {
            "form": SearchForm(),
            "new_title": TitleForm(),
            "new_content": ContentForm()
        })

def edit(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "form": SearchForm(),
            "text_edit": ContentForm(initial={'content':content})
        })

    else:
        content_form = ContentForm(request.POST)
        if content_form.is_valid():
            content = content_form.cleaned_data["content"]
            util.save_entry(title, content)

            return wiki_title(request, title)

def random(request):
    index = randrange(len(util.list_entries()))
    return wiki_title(request, util.list_entries()[index])