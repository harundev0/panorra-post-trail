import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix rounding artifact on overlays by adding rounded-[inherit] or rounded-3xl
html = html.replace('absolute inset-0 bg-black/60', 'absolute inset-0 bg-black/60 rounded-[inherit]')
html = html.replace('absolute inset-0 z-10 bg-black/60', 'absolute inset-0 z-40 bg-black/60 rounded-[inherit]')

# Fix Status Bar Z-index in static previews so it's UNDER the overlay
html = html.replace('bg-background z-20 shrink-0', 'bg-background z-30 shrink-0')

# Elevate the sheet itself in static previews
# From: class="absolute bottom-0 left-0 right-0 h-[88%] bg-background flex flex-col pt-3 z-20
# To: flex flex-col pt-3 z-50
html = html.replace('pt-3 z-20', 'pt-3 z-50')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
