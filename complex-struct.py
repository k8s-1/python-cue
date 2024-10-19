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
  resources: {}
"""

# Load YAML into a Python dictionary
data = yaml.safe_load(yaml_content)

# Extract the 'containers' part
containers = data.get('containers')

# Output the 'containers' part as JSON
json_output = json.dumps(containers, indent=2)
print(json_output)
