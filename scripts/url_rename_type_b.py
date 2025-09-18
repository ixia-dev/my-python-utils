import os

base_dir = os.path.dirname(os.path.abspath(__file__))

replacements = {
    '<link rel="stylesheet" href="../../': '<link rel="stylesheet" href="************',
    '<img src="../../': '<img src="************',
    '<script src="../../': '<script src="************',
}

for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        file_path = os.path.join(base_dir, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        for before, after in replacements.items():
            new_content = new_content.replace(before, after)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Updated: {filename}")
