from config.business_rules import META_DESCRIPTION_TEMPLATE, SEO_KEYWORDS

def generate_meta_description(service_name):
    return META_DESCRIPTION_TEMPLATE.format(service_name=service_name)

def generate_keywords(service_name):
    return [service_name] + SEO_KEYWORDS
