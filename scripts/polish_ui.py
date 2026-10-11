import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make buttons explicitly h-12 and nicely rounded
content = content.replace('py-3.5 px-4 rounded-lg', 'h-12 px-4 rounded-xl')
content = content.replace('py-3.5 text-center bg-card', 'h-12 flex items-center justify-center bg-card')
content = content.replace('py-3 bg-card text-center rounded-lg', 'h-12 bg-card flex items-center justify-center rounded-xl')
content = content.replace('py-3 text-center bg-primary rounded-lg', 'h-12 bg-primary flex items-center justify-center rounded-xl')

# Soften some font weights from bold to semibold to look more elegant
content = content.replace('font-bold', 'font-semibold')
# Re-bold specific extremely prominent headers
content = content.replace('text-[17px] font-semibold text-foreground tracking-tight', 'text-[18px] font-bold text-foreground')
content = content.replace('h2 class="text-[16px] font-semibold"', 'h2 class="text-[18px] font-bold"')
content = content.replace('You don\'t have any trails or tours yet</h3>', 'You don\'t have any trails or tours yet</h3>').replace('text-[16px] font-semibold mb-3', 'text-[17px] font-bold mb-3')
content = content.replace('text-[15px] font-semibold mb-3', 'text-[17px] font-bold mb-3')

# Clean up empty state spacing and "or"
content = content.replace('py-2', 'py-1.5')

# Make radio buttons look closer to design
content = content.replace('width: 20px;\n            height: 20px;', 'width: 22px;\n            height: 22px;')

# Empty state graphic tweaks (make the document look slightly softer)
content = content.replace('w-24 h-28 bg-card rounded-3xl border-2 border-border', 'w-[90px] h-[106px] bg-card rounded-2xl border-2 border-border/80')
content = content.replace('w-20 h-24 bg-card rounded-[18px] border-2 border-border', 'w-[80px] h-[96px] bg-card rounded-[16px] border-2 border-border/80')

# Padding for list items
content = content.replace('p-2.5 rounded-2xl', 'p-3 rounded-2xl')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(content)
