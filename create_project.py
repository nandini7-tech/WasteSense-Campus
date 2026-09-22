from pathlib import Path
import zipfile

PROJECT = "AI-Sustainability-Internship-Project"
project_dir = Path(PROJECT)

if not project_dir.exists():
    print(f"Error: {project_dir} not found")
    exit(1)

zip_path = Path(f"{PROJECT}.zip")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for file_path in project_dir.rglob("*"):
        if file_path.is_file():
            arcname = (Path(PROJECT) / file_path.relative_to(project_dir)).as_posix()
            zf.write(file_path, arcname)

print(f"Created: {zip_path.resolve()}")
print(f"Project directory successfully packaged: {project_dir.resolve()}")
