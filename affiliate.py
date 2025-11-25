def inject_affiliates(content, affiliate_template):
    # Replace placeholder token with affiliate link (ASIN placeholder)
    return content.replace('{AFFILIATE_PLACEHOLDER}', affiliate_template.format(asin='B08EXAMPLE'))
