# 🧭 `xc` - Explore code

When exploring new projects: I often want to get an overview of the folder & file structure,  
see where the "bulk" of code is written.

This tool **shows all the structure**, e.g.:

<img src="./img/example.png" alt="Example image" width="400" />


<br />

## How to use

**Step 1**

Install this package:
```bash
cd explore_code  # the root folder of this repo
pip install -e .
```

(For convenience) Set an alias, e.g. in `~/.bashrc`:
```bash
alias xc='python -m explore_code.serve'
# Or even (to automatically open the browser as well):
alias xc='open -a "Google Chrome" http://localhost:8000 & python -m explore_code.serve'  # for macOS
alias xc='xdg-open http://localhost:8000 & python -m explore_code.serve'  # for Linux
```

**Step 2**

Use:

```bash
cd any/folder
xc
```

or:

```bash
xc path/to/any/folder
```

✅ Open [http://localhost:8000/](http://localhost:8000/) in your browser.


<br />

## Features:

- zooming, panning
- clicking on a folder: collapses / expands it
- double clicking on a folder / file: copies its absolute path to clipboard
- files are sorted and colored by filetype
- size of box corresponds to number of lines
- hovering over a box: shows info


<br />

## TODO:

- make a VSCode extension out of this? - so that clicking on file box -> opens this file in VSCode (e.g. in the tab on the right)
- add ability for nice rules which files to include/exclude (by list of regexes? or maybe better: gitignore syntax?)


<br />

## Alternatives

- `Crabviz`: VSCode ext: https://marketplace.visualstudio.com/items?itemName=chanhx.crabviz
- `code2flow`: cli tool: https://github.com/scottrogowski/code2flow
- `Graphviz Interactive Preview`: VSCode ext: https://marketplace.visualstudio.com/items?itemName=tintinweb.graphviz-interactive-preview
- `Code Analyzer 2.0`: VSCode ext: https://marketplace.visualstudio.com/items?itemName=SoftwareEvolutionLab.codeanalyzer2 - uses gitinspector
- `gitinspector`: cli tool: https://github.com/ejwa/gitinspector
- `VS Code Counter`: VSCode ext (no viz, but maybe I could use info from it for my viz): https://marketplace.visualstudio.com/items?itemName=uctakeoff.vscode-counter

**Not** useful for Python in VSCode:
- `Code Graph`: only VisualStudio: https://marketplace.visualstudio.com/items?itemName=YaobinOuyang.CodeAtlas
- `Dependency Cruiser`: only JS ecosystem: https://github.com/sverweij/dependency-cruiser

