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


def add(string: str) -> str:
    s = ""
    try:
        s += string

    except Exception:
        return

    return s


content += add(f"""
        another: \"{prime_service['rest']['url']}"
""")

content += add(f"""
        fail_100: \"{prime_service['TEST']['url']}"
""")


content += """
    }
}
yaml.MarshalStream([ for _, o in #objects {o} ])
"""

print(content)
