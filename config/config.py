# config.py

from datetime import datetime

topics = [
    "Technical Leadership",
    "Software Development",
    "MENA Tech Talent",
    "US Market Opportunities",
    "Digital Transformation",
]

content_types = [
    "how-to",
    "case-study",
    "industry-insight",
    "technical-guide",
    "comparison",
]

target_markets = [
    {"name": "Michigan", "focus": ["automotive", "manufacturing"]},
    {"name": "Texas", "focus": ["technology", "startups"]},
    {"name": "North Carolina", "focus": ["banking", "biotech"]},
]

services = [
    {
        "name": "Fractional CTO Services",
        "topics": ["technical leadership", "architecture", "strategy"],
        "benefits": ["cost-effective", "flexible", "experienced"],
    },
    {
        "name": "Development Teams",
        "topics": ["software development", "team augmentation", "project delivery"],
        "benefits": ["skilled engineers", "cost savings", "scalable"],
    },
    {
        "name": "Technical Consultation",
        "topics": ["architecture review", "technology selection", "roadmap planning"],
        "benefits": ["expert guidance", "risk reduction", "optimization"],
    },
]

templates = {
    "how-to": "How to Leverage {service_name} for Your Business Growth",
    "case-study": "How {service_name} Transformed a {market} Company",
    "industry-insight": "The Future of {service_name} in {market}",
    "technical-guide": "A Complete Guide to Implementing {service_name}",
    "comparison": "Comparing US vs MENA {service_name}: Benefits and Considerations",
}

OUTPUT_DIR = "output"
MAX_BLOGS = 300
