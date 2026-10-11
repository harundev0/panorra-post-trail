import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to find the static preview sections and adjust them to show the bottom sheet structure.
# For Preview 2 (Loading Context):
# Current: `<div class="absolute inset-0 bg-background flex flex-col pt-[50px] z-10 shadow-[0_-10px_30px_rgba(0,0,0,0.1)]">`
# I will replace it with: Layer 1 (overlay), Layer 2 (bottom sheet h-[90%])

old_static_modal = r'<div class="absolute inset-0 bg-background flex flex-col pt-\[50px\] z-10 shadow-\[0_-10px_30px_rgba\(0,0,0,0\.1\)\]">\s*<div class="w-full flex justify-center pt-2 pb-1 absolute top-\[44px\] z-50 bg-background"><div class="w-10 h-\[5px\] bg-border rounded-full"></div></div>'


new_static_modal = """
                    <!-- Static Overlay Background -->
                    <div class="absolute inset-0 bg-black/60 dark:bg-black/80 backdrop-blur-sm z-10"></div>
                    
                    <!-- Static Bottom Sheet Content -->
                    <div class="absolute bottom-0 left-0 right-0 h-[90%] bg-background flex flex-col pt-4 z-20 shadow-[0_-20px_40px_rgba(0,0,0,0.2)] rounded-t-[2rem] overflow-hidden">
                        <div class="w-full flex justify-center pb-4 shrink-0 bg-background z-50"><div class="w-12 h-1.5 bg-border rounded-full"></div></div>
"""

html = re.sub(old_static_modal, new_static_modal, html)

# The close buttons might be out of place now because `pt-4` in header, let's fix the header padding
html = html.replace('<div class="px-5 pb-4 pt-5 border-b border-border relative shrink-0">', '<div class="px-5 pb-4 border-b border-border relative shrink-0">')
html = html.replace('<div class="px-5 pb-3 pt-4 border-b border-border relative shrink-0">', '<div class="px-5 pb-4 border-b border-border relative shrink-0">')
html = html.replace('<span class="absolute right-4 top-5 text-muted-foreground">', '<span class="absolute right-4 top-0 text-muted-foreground">')
html = html.replace('<span class="absolute right-4 top-4 text-muted-foreground">', '<span class="absolute right-4 top-0 text-muted-foreground">')


with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
