## nb2page

A script to convert a Jupyter notebook to a markdown file that can be posted on a GitHub page. It does:

- Call nbconvert to convert a notebook to markdown.
- Change MathJax mode so that inline math can be rendered when typed with single dollar symbols, e.g. `$f(x) = x + 1$`
- Add a front matter to specify layout, title, etc.
- Add a GitHub button that points to a repository.
- Replace image paths in the generated markdown file to an appropriate folder (e.g. `assets`).
- Move all the exported files to their respective folders in the page root directory.

Usage:

`./nb2page.sh NOTEBOOK PAGE_ROOT`

where
- `NOTEBOOK` is the path of the notebook
- `PAGE_ROOT` is the root directory of the GitHub page

This is just a rough and ready script to make the process of blogging with notebooks written in Python a little bit faster. Feel free to copy it, make it better, fit it to your needs, share it, etc.
