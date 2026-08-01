# Extract the domain name from a URL
# KATA: https://www.codewars.com/kata/514a024011ea4fb54200004b

import re

def domain_name(url):
    
    pattern = r"(?:https?://)?(?:www\.)?([^.]+)"

    match = re.search(pattern, url)
    domain_name = match.group(1) if match else "unknown"
        
    return domain_name