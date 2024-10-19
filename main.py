import yaml

with open('values.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

content = """import (
    "github.com/k8s-1/app/best"
)

#objects: best.#Def & {
    #vals: {
        """

content += f"someval: \"{prime_service['rest']['url']}\""

try:
    content += """
        123
"""

except Exception:
    print("Could not parse field into content")

content += """
    }
}
yaml.MarshalStream([ for _, o in #objects {o} ])
"""

print(content)
