import yaml
import json

# Sample YAML content as a string
yaml_content = """
rest:
  url: "https://example.org/primenumbers/v1"
  port: 8443
prime_numbers: [2, 3, 5, 7, 11, 13, 17, 19]

containers:
- image: nginx
  name: po
  resources: 
    requests:
      memory: "1000"
      cpu: "250m"
    limits:
      memory: "128Mi"
      cpu: "500m"
"""

# Load YAML into a Python dictionary
data = yaml.safe_load(yaml_content)

# Extract the 'containers' part
containers = data.get('containers')

# Output the 'containers' part as JSON
json_output = json.dumps(containers, indent=2)
print("JSON OUTPUT:\n")
print(f"""containers: {json_output}""")


import re

def json_to_cue(json_str):
    result = re.sub(r'\"(\w+)\":', r'\1:', json_str)
    result = re.sub(r'\"([0-9]+)\"', r'\1', result)

    return result

cue_format = json_to_cue(json_output)
print(f"""

CUE:

{cue_format}

""")
