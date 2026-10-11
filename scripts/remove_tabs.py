import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the tabs div
pattern = r'<div class="flex[^"]* border-b border-border shrink-0[^>]*>[\s\n]*<(button|div)[^>]*>Trails \(\d+\)</\1>[\s\n]*<(button|div)[^>]*>Tours \(\d+\)</\2>[\s\n]*</div>'

new_content = re.sub(pattern, '', content)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Removed {(len(content) - len(new_content))} characters.")
