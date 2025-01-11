import os
from config.templates import BLOG_TEMPLATE
from logic.seo import generate_meta_description, generate_keywords
from logic.deep_linking import add_deep_links

def generate_blog_file(title, content, output_dir="output"):
    file_name = f"{title.replace(' ', '_').replace('/', '-')}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return file_path

def create_blog(title, content, service_name):
    meta_description = generate_meta_description(service_name)
    keywords = generate_keywords(service_name)
    content_with_links = add_deep_links(content)

    return BLOG_TEMPLATE.format(
        title=title,
        meta_description=meta_description,
        keywords=", ".join(keywords),
        content=content_with_links,
    )
