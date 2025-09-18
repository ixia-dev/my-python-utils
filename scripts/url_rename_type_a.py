import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

target_keyword = "ここにキーワードを作成"

pattern = re.compile(r"\.\./[A-Za-z0-9_]+/([A-Za-z0-9_]+)\.html([?#][^\"'\s<]*)?")

for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        file_path = os.path.join(base_dir, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        def replacer(match):
            file_id = match.group(1)  
            params = match.group(2) if match.group(2) else ""  
            return f"?param1={target_keyword}&param2={file_id}{params}"

        new_content = pattern.sub(replacer, content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"{filename}のアップロード完了")
