# Configuration for content templates
BLOG_TEMPLATE = """
# {title}

## Meta Description
{meta_description}

## Keywords
{keywords}

## Content
{content}
"""

PROMPT_TEMPLATE = """
system:
You are an AI assistant tasked with generating blog posts for a company's services.
Focus on public-facing content while protecting sensitive information.
Each post should include:
- A unique and catchy title.
- Detailed blog content optimized for SEO.
- Keywords for SEO and a meta description.
- Links to other relevant pages (deep linking).
- Content targeting diverse markets.

The company's data is: {company_data}
"""
