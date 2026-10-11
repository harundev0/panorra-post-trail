with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure there is only one "activePhone" logic
# Did I get the x-data scope correct?
# Changed: `<section x-data="prototype()" class="flex flex-col items-center gap-8">`
# And added toggles inside it.
# Check if `<div x-data="{}"... ` is around.
text = text.replace('<div x-data="{}" x-init="$watch(\'activePhone\', () => {})"></div>\n', '')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Double checked HTML syntax!")
