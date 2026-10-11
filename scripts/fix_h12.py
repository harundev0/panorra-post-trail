import re
with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix spacing on the modal bottom action section
# Increase padding bottom to 8 or 10
text = text.replace('pb-8 pt-10', 'pb-10 pt-4')

text = text.replace('gap-3.5', 'gap-4')
text = text.replace('px-6 py-5', 'px-6 py-4')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)
