# Explore code

When exploring new projects: I often want to get an overview of the folder & file structure,  
see where the "bulk" of code is written.

This tool shows all the structure.


<br />

## How to use

Run the script like this:
`python generate_code_structure.py ./relative/path/to/folder/for/analysing`

This generates the `_gitignore_code_structure.json` file (in the current folder).


<br />

✅ Then View the Output:

1. Start a simple HTTP server (required for D3 to load the JSON):

    ```bash
    python -m http.server
    ```

2. Open your browser and go to:
    http://localhost:8000/code_structure_viewer.html

    The D3 script in `code_structure_viewer.html` loads `_gitignore_code_structure.json`.



<br />

## Features:

- clicking on a folder: collapses / expands it
- double clicking on a folder / file: copies its absolute path to clipboard
- hovering: shows info
- files are sorted and colored by filetype; size of box corresponds to number of lines


<br />

## TODO:

- make a VSCode extension out of this? - so that clicking on file opens it
- add ability for nice rules which files to include/exclude (by list of regexes? or maybe better: gitignore syntax?)


<br />

## Alternatives

- `Crabviz`: VSCode ext: https://marketplace.visualstudio.com/items?itemName=chanhx.crabviz
- `code2flow`: cli tool: https://github.com/scottrogowski/code2flow
- `Graphviz Interactive Preview`: https://marketplace.visualstudio.com/items?itemName=tintinweb.graphviz-interactive-preview
- `Code Analyzer 2.0`: VSCode ext: https://marketplace.visualstudio.com/items?itemName=SoftwareEvolutionLab.codeanalyzer2 - uses gitinspector
- `gitinspector`: cli tool: https://github.com/ejwa/gitinspector

**Not** useful for Python in VSCode:
- `Code Graph`: only VisualStudio: https://marketplace.visualstudio.com/items?itemName=YaobinOuyang.CodeAtlas
- `Dependency Cruiser`: only JS ecosystem: https://github.com/sverweij/dependency-cruiser

