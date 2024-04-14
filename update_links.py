import os
import re

# 图片扩展名列表
img_exts = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff']

def create_replace_func(ext_pattern, base_url):
    """Create a replacement function tailored to the image extension pattern and base url."""
    def replace(match):
        file_name_with_ext = match.group(1).strip() + ext_pattern
        maybe_size_info = match.group(2).strip() if len(match.groups()) > 1 else ""
        size_part = f" {maybe_size_info}" if maybe_size_info else ""
        return f"![{match.group(1).strip()}]({base_url}/{file_name_with_ext.replace(' ', '%20')})"
    return replace

# The base URL for the images
base_image_url = "https://crystalbell98.github.io/Notes/docs/figure"

# Find and replace image markdown in all .md files
for subdir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(subdir, file)
            # Opening with 'utf-8' encoding
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            for ext in img_exts:
                # Regex pattern for images with potential size argument
                pattern_with_size = re.compile(rf'!\[\[(.*?){ext}\|(.*?)\]\]')
                # Regex pattern for images without size argument
                pattern_without_size = re.compile(rf'!\[\[(.*?){ext}\]\]')

                # Replace images with size info
                content = pattern_with_size.sub(create_replace_func(ext, base_image_url), content)
                # Replace images without size info
                content = pattern_without_size.sub(lambda match: create_replace_func(ext, base_image_url)(match), content)
            # Write back using 'utf-8' encoding
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        elif file.startswith('wowchemy.') and file.endswith('.css'):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            pattern = re.compile(r"(\.docs-article-container\s*\{[^}]*\})")
            content = pattern.sub(r'/* \1 */', content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Script has finished!")
