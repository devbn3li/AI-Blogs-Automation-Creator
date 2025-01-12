import os

# Blog settings
MAX_BLOGS = 30
OUTPUT_DIR = "generated_content"

# Topics and content types
topics = [
    "Technical Leadership",
    "Software Development",
    "MENA Tech Talent",
    "US Market Opportunities",
    "Digital Transformation",
    "IT Strategy",
    "Technology Trends",
    "Innovation",
    "Startups",
    "Entrepreneurship",
    "Business Growth",
    "Digital Marketing",
    "E-commerce",
    "Mobile Development",
    "Agile Methodologies",
    "Web Development",
    "Project Management",
    "Quality Assurance",
    "Product Design",
    "Cybersecurity",
    "Cloud Computing",
    "Data Analytics",
    "AI and Machine Learning",
    "Blockchain",
]

content_types = [
    "how-to",
    "case-study",
    "industry-insight",
    "technical-guide",
    "what is",
    "why",
    "introduction",
    "benefits",
    "want-to-know",
    "comparison",
]

# Target markets
target_markets = [
    {"name": "Michigan", "focus": ["automotive", "manufacturing"]},
    {"name": "Texas", "focus": ["technology", "startups"]},
    {"name": "North Carolina", "focus": ["banking", "biotech"]},
    {"name": "California", "focus": ["entertainment", "healthcare"]},
    {"name": "New York", "focus": ["finance", "media"]},
    {"name": "Florida", "focus": ["tourism", "real estate"]},
    {"name": "Georgia", "focus": ["logistics", "agriculture"]},
    {"name": "Illinois", "focus": ["retail", "food industry"]},
    {"name": "Ohio", "focus": ["education", "energy sector"]},
    {"name": "Washington", "focus": ["aerospace", "software development"]},
    {"name": "Massachusetts", "focus": ["biotech", "education"]},
    {"name": "Colorado", "focus": ["renewable energy", "technology"]},
    {"name": "Pennsylvania", "focus": ["pharmaceuticals", "manufacturing"]},
    {"name": "New Jersey", "focus": ["pharmaceuticals", "finance"]},
    {"name": "Virginia", "focus": ["defense", "technology"]},
    {"name": "Arizona", "focus": ["healthcare", "technology"]},
    {"name": "Tennessee", "focus": ["healthcare", "automotive"]},
    {"name": "Indiana", "focus": ["manufacturing", "technology"]},
    {"name": "Missouri", "focus": ["agriculture", "manufacturing"]},
    {"name": "Maryland", "focus": ["biotech", "cybersecurity"]},
    {"name": "Wisconsin", "focus": ["manufacturing", "agriculture"]},
    {"name": "Minnesota", "focus": ["healthcare", "technology"]},
    {"name": "South Carolina", "focus": ["tourism", "manufacturing"]},
    {"name": "Alabama", "focus": ["aerospace", "manufacturing"]},
    {"name": "Louisiana", "focus": ["energy sector", "manufacturing"]},
    {"name": "Kentucky", "focus": ["manufacturing", "agriculture"]},
    {"name": "Oregon", "focus": ["technology", "renewable energy"]},
    {"name": "Oklahoma", "focus": ["energy sector", "agriculture"]},
    {"name": "Connecticut", "focus": ["finance", "insurance"]},
    {"name": "Iowa", "focus": ["agriculture", "manufacturing"]},
    {"name": "Mississippi", "focus": ["agriculture", "manufacturing"]},
    {"name": "Arkansas", "focus": ["agriculture", "manufacturing"]},
    {"name": "Utah", "focus": ["technology", "renewable energy"]},
    {"name": "Nevada", "focus": ["tourism", "technology"]},
    {"name": "New Mexico", "focus": ["energy sector", "technology"]},
]

# Services offered
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
    {
        "name": "Product Design",
        "topics": ["UX/UI design", "prototyping", "user research"],
        "benefits": ["user-centric", "innovative", "engaging"],
    },
    {
        "name": "Quality Assurance",
        "topics": ["test automation", "manual testing", "QA strategy"],
        "benefits": ["reliable", "efficient", "scalable"],
    },
    {
        "name": "Digital Marketing",
        "topics": ["SEO", "PPC", "content marketing"],
        "benefits": ["increased visibility", "targeted campaigns", "measurable results"],
    },
    {
        "name": "E-commerce Solutions",
        "topics": ["online store", "payment gateway", "inventory management"],
        "benefits": ["scalable", "secure", "customizable"],
    },
    {
        "name": "Mobile App Development",
        "topics": ["iOS", "Android", "cross-platform"],
        "benefits": ["user-friendly", "innovative", "scalable"],
    },
    {
        "name": "Web Development",
        "topics": ["front-end", "back-end", "full-stack"],
        "benefits": ["responsive", "customizable", "scalable"],
    },
    {
        "name": "Agile Methodologies",
        "topics": ["scrum", "kanban", "agile transformation"],
        "benefits": ["flexible", "collaborative", "efficient"],
    },
    {
        "name": "IT Strategy",
        "topics": ["roadmap", "technology stack", "digital transformation"],
        "benefits": ["aligned goals", "innovation", "competitive advantage"],
    },
    {
        "name": "Cybersecurity",
        "topics": ["risk assessment", "compliance", "incident response"],
        "benefits": ["secure", "compliant", "resilient"],
    },
    {
        "name": "Cloud Computing",
        "topics": ["AWS", "Azure", "Google Cloud"],
        "benefits": ["scalable", "cost-effective", "flexible"],
    },
    {
        "name": "Data Analytics",
        "topics": ["BI", "data visualization", "predictive analytics"],
        "benefits": ["insights", "data-driven decisions", "competitive advantage"],
    },
    {
        "name": "AI and Machine Learning",
        "topics": ["ML models", "NLP", "computer vision"],
        "benefits": ["automation", "personalization", "efficiency"],
    },
    {
        "name": "Blockchain",
        "topics": ["smart contracts", "decentralized apps", "cryptocurrency"],
        "benefits": ["transparency", "security", "trust"],
    },
    {
        "name": "Startups",
        "topics": ["MVP development", "funding", "growth hacking"],
        "benefits": ["innovative", "agile", "scalable"],
    },
    {
        "name": "Entrepreneurship",
        "topics": ["business plan", "pitch deck", "market research"],
        "benefits": ["visionary", "resilient", "adaptive"],
    },
    {
        "name": "Business Growth",
        "topics": ["market expansion", "customer acquisition", "revenue growth"],
        "benefits": ["sustainable", "competitive", "scalable"],
    },
    {
        "name": "Innovation",
        "topics": ["disruption", "creativity", "design thinking"],
        "benefits": ["competitive advantage", "market leadership", "growth"],
    },
    {
        "name": "Digital Transformation",
        "topics": ["legacy systems", "cloud migration", "automation"],
        "benefits": ["efficiency", "agility", "innovation"],
    }
]

# Blog templates
templates = {
    "how-to": "How to Leverage {service_name} for Your Business Growth",
    "case-study": "How {service_name} Transformed a {market} Company",
    "industry-insight": "The Future of {service_name} in {market}",
    "what is": "What is {service_name} and How Can It Benefit Your Business?",
    "why": "Why Your Business Needs {service_name} to Stay Competitive",
    "introduction": "An Introduction to {service_name} and Its Benefits for Your Business",
    "benefits": "The Top Benefits of Using {service_name} for Your Business",
    "technical-guide": "A Complete Guide to Implementing {service_name}",
    "comparison": "Comparing US vs MENA {service_name}: Benefits and Considerations",
    "default": "Discover the Power of {service_name} for Your Business",
    "want-to-know": "Everything You Want to Know About {service_name}",
}
