# Contributing

I am so happy to whoever is reading this. If there are problems with grammar, story, ideas, images, the gitlab-ci or anything else, please let me know and I will try to resolve the problems. Open an issue over at [Gitlab](https://gitlab.com/kaictl/writing/summoning/-/issues) with any concerns or problems you see.

## Writing Style

* I am set on using a single line per paragraph, so no line-breaks as some people do in markdown or restructuredText. Yes, they'll work, but if I'm going back and editing, this makes it easier.
* The `Ideas/` directory is mostly for what it says, ideas. Nothing in there is set in stone, but it's included with the builds for reference to those reading.
* Images you want to include should have a link where they came from, or some kind of attribution. I have done this mostly in `Ideas/sources.rst`.
* `Book/` is where the actual final product goes.

## Criticism

Please, give me criticism. I'm no author myself and I have no illusions that I'm any good at this, so please make an issue if there's something you don't like or something I can improve.

However, if your criticism is just "This is garbage, you can't write for shit," then I agree, but get out. If you are going to say something, at least make it constructive.

Some things won't be possible or feasible, but I'll at least try if it's possible.

## Writing in VSCode

Yes, I'm a weird person and I *really* like vscode. I've set up this book in such a way that it can generate a really nice website and a readable ebook using sphinx. You'll need to set up the python stuff to be able to test it out locally, but even that isn't necessarily required.

### Setup

Run the `Python: Create Environment...` command in vscode's command pallet (ctrl+P) and use the `Venv` option with your installed python interpreter. You can either have vscode install the requirements or you can run `pip install -r requirements.txt` to install them.

### Merge Requests

If you don't want to install it locally, Gitlab is awesome, and I've set it up to make merge requests generate local environments where you can read the built product before I've merged it. (See [This MR](https://gitlab.com/kaictl/writing/summoning/-/merge_requests/6)) This is a totally valid thing to do if you either don't want to install python, don't trust my vscode tasks or just want to modify stuff in the browser.

---

Thank you for reading,

-- Kai
