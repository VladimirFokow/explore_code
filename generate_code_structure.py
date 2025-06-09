import os
import json

EXT_LANG_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".html": "HTML",
    ".css": "CSS",
    ".cpp": "C++",
    ".cs": "C#",
    ".java": "Java",
    ".json": "JSON",
    ".md": "Markdown",
    ".sh": "Shell",
    ".yml": "YAML",
    ".yaml": "YAML",
}

def get_language(file_name):
    ext = os.path.splitext(file_name)[1]
    return EXT_LANG_MAP.get(ext.lower(), "Unknown")

def count_lines_in_file(file_path):
    """Count non-empty lines in a file, handling encoding issues gracefully."""
    try:
        # Try UTF-8 first
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        try:
            # Fallback to latin-1 for binary-ish files
            with open(file_path, 'r', encoding='latin-1') as f:
                lines = f.readlines()
        except Exception:
            # If all else fails, skip this file
            return 0
    except Exception:
        # Handle permission errors, etc.
        return 0
    
    # Count non-empty lines (strip whitespace and check if line has content)
    non_empty_lines = sum(1 for line in lines if line.strip())
    return non_empty_lines

def build_tree(path):
    name = os.path.basename(path)
    if os.path.isdir(path):
        try:
            children = []
            for item in os.listdir(path):
                # Skip hidden files and common build/cache directories
                if item.startswith('.') or item in ['node_modules', '__pycache__', 'build', 'dist']:
                    continue
                child_path = os.path.join(path, item)
                children.append(build_tree(child_path))
            
            return {
                "name": name,
                "type": "folder",
                "children": children
            }
        except PermissionError:
            # Handle directories we can't access
            return {
                "name": name,
                "type": "folder",
                "children": []
            }
    else:
        file_info = {
            "name": name,
            "type": "file",
            "language": get_language(name)
        }
        
        # Count lines for text files
        language = file_info["language"]
        if language in ["Python", "JavaScript", "TypeScript", "HTML", "CSS", "C++", "C#", "Java", "JSON", "Markdown", "Shell", "YAML"]:
            lines = count_lines_in_file(path)
            if lines > 0:
                file_info["lines"] = lines
        
        return file_info

if __name__ == "__main__":
    import sys
    root_path = sys.argv[1] if len(sys.argv) > 1 else "."
    tree = build_tree(root_path)
    with open("_gitignore_code_structure.json", "w") as f:
        json.dump(tree, f, indent=2)