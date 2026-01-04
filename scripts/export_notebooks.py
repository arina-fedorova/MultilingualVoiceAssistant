#!/usr/bin/env python3
"""Export Jupyter notebooks to HTML for portfolio visibility.

This script converts notebooks from notebooks/ to HTML in reports/.
Outputs include all cell outputs (plots, tables, etc.) for documentation.

Usage:
    poetry run python scripts/export_notebooks.py
    poetry run python scripts/export_notebooks.py notebooks/exploration/01_eda.ipynb
"""

import subprocess
import sys
from pathlib import Path


def export_notebook(notebook_path: Path, output_dir: Path) -> bool:
    """Export a single notebook to HTML.

    Args:
        notebook_path: Path to the .ipynb file
        output_dir: Directory to save the HTML output

    Returns:
        True if export succeeded, False otherwise
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "jupyter",
        "nbconvert",
        "--to",
        "html",
        str(notebook_path),
        "--output-dir",
        str(output_dir),
    ]

    print(f"Exporting: {notebook_path.name} -> {output_dir}/")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ERROR: {result.stderr}")
        return False

    print(f"  OK: {notebook_path.stem}.html")
    return True


def export_all_notebooks(notebooks_dir: Path, reports_dir: Path) -> tuple[int, int]:
    """Export all notebooks from notebooks/ to reports/.

    Args:
        notebooks_dir: Root notebooks directory
        reports_dir: Root reports directory

    Returns:
        Tuple of (success_count, failure_count)
    """
    success = 0
    failure = 0

    for notebook in notebooks_dir.rglob("*.ipynb"):
        # Skip checkpoint files
        if ".ipynb_checkpoints" in str(notebook):
            continue

        # Maintain folder structure in reports/
        relative_path = notebook.relative_to(notebooks_dir)
        output_dir = reports_dir / relative_path.parent

        if export_notebook(notebook, output_dir):
            success += 1
        else:
            failure += 1

    return success, failure


def main() -> int:
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    notebooks_dir = project_root / "notebooks"
    reports_dir = project_root / "reports"

    if len(sys.argv) > 1:
        # Export specific notebook
        notebook_path = Path(sys.argv[1])
        if not notebook_path.exists():
            print(f"Error: {notebook_path} not found")
            return 1

        # Determine output directory based on notebook location
        if notebooks_dir in notebook_path.parents or notebook_path.parent == notebooks_dir:
            relative = notebook_path.relative_to(notebooks_dir)
            output_dir = reports_dir / relative.parent
        else:
            output_dir = reports_dir

        success = export_notebook(notebook_path, output_dir)
        return 0 if success else 1

    # Export all notebooks
    print(f"Exporting notebooks from {notebooks_dir} to {reports_dir}\n")

    success, failure = export_all_notebooks(notebooks_dir, reports_dir)

    print(f"\nDone: {success} exported, {failure} failed")
    return 0 if failure == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
