## nb2page

A script to convert a Jupyter notebook to a markdown file to be used on a GitHub page. It does:

- Call nbconvert to obtain a markdown file.
- Change MathJax mode so that inline math can be typed with single dollar symbols, e.g. `$f(x) = x + 1$`
- Add a front matter to specify layout, title, etc.
- Add a GitHub button that points to a repository.
- Replaces image paths in the generated markdown file to a different folder (e.g. `assets`).
