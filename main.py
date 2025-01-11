import os
import random
from datetime import datetime
from config.config import topics, content_types, target_markets, services, templates, OUTPUT_DIR, MAX_BLOGS
from ai.model import generate_content

# Generate a slug for the title
def generate_slug(title):
    return title.lower().replace(" ", "-").replace(":", "").replace("?", "")

# Generate meta description
def generate_meta_description(service, content_type):
    return f"Discover how Dragons' {service['name']} can help your business thrive. Learn about our expertise in {', '.join(service['topics'])} and achieve {', '.join(service['benefits'])}."

# Generate keywords
def generate_keywords(service):
    base_keywords = service["topics"] + service["benefits"]
    return base_keywords + ["MENA talent", "US market", "tech solutions", "software development"]

# Generate internal links
def generate_internal_links(service):
    return [
        {
            "text": f"Learn more about our {related['name']}",
            "url": f"/services/{generate_slug(related['name'])}",
        }
        for related in services
        if related["name"] != service["name"]
    ]

# Generate sections for the blog
def generate_sections(service):
    return [
        {
            "title": "Introduction",
            "content": f"Learn how Dragons' {service['name']} can transform your business through our unique MENA talent pool and US market expertise.",
        },
        {
            "title": "Key Benefits",
            "content": f"Discover the advantages of working with Dragons: {', '.join(service['benefits'])}.",
        },
        {
            "title": "Implementation Process",
            "content": "Our streamlined process ensures smooth integration and maximum value for your business.",
        },
        {
            "title": "Success Stories",
            "content": "Read about how our clients have achieved their goals through our services.",
        },
        {
            "title": "Next Steps",
            "content": "Contact Dragons today to learn how we can help your business grow.",
        },
    ]

# Generate a call-to-action (CTA)
def generate_cta(service):
    return {
        "text": f"Ready to enhance your business with {service['name']}?",
        "button_text": "Schedule a Consultation",
        "url": "/contact",
    }

# Save the blog as a Markdown file
def save_blog(content):
    file_name = generate_slug(content["title"]) + ".md"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"# {content['title']}\n\n")
        file.write(f"**Meta Description:** {content['meta_description']}\n\n")
        file.write(f"**Keywords:** {', '.join(content['keywords'])}\n\n")
        for section in content["sections"]:
            file.write(f"## {section['title']}\n{section['content']}\n\n")
        file.write("### Internal Links:\n")
        for link in content["internal_links"]:
            file.write(f"- [{link['text']}]({link['url']})\n")
        file.write("\n### Call to Action:\n")
        file.write(f"{content['call_to_action']['text']}\n")
        file.write(f"[{content['call_to_action']['button_text']}]({content['call_to_action']['url']})\n")
    return file_path

# Main function to generate blogs
def generate_blogs():
    print(f"Generating up to {MAX_BLOGS} blogs...")
    for i in range(MAX_BLOGS):
        service = random.choice(services)
        content_type = random.choice(content_types)
        market = random.choice(target_markets)
        title = templates[content_type].format(
            service_name=service["name"], market=market["name"]
        )
        meta_description = generate_meta_description(service, content_type)
        keywords = generate_keywords(service)
        sections = generate_sections(service)
        internal_links = generate_internal_links(service)
        cta = generate_cta(service)

        content = {
            "title": title,
            "slug": generate_slug(title),
            "meta_description": meta_description,
            "keywords": keywords,
            "sections": sections,
            "internal_links": internal_links,
            "call_to_action": cta,
            "created_at": datetime.now().isoformat(),
        }

        file_path = save_blog(content)
        print(f"Saved blog: {file_path}")

if __name__ == "__main__":
    generate_blogs()
