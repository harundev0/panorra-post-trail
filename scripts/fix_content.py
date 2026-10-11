import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text sizing for the header
content = content.replace('text-[16px] font-bold text-foreground', 'text-[17px] font-semibold text-foreground tracking-tight')

# 2. Update search bar height and styling to look more like the screenshot
# The search bar in the screenshot has a dark background and subtle outline
content = content.replace('bg-secondary border-none rounded-xl py-3', 'bg-card border border-border/80 rounded-[14px] py-2.5 h-11')

# 3. Fix the "Loading your Tourmkr data..." subtitle
# it says: "We're fetching your latest trails and tours. This may take a few seconds." -> "We're fetching your latest trails and tours." <br /> "This may take a few seconds."
content = content.replace('text-[13px] font-medium text-muted-foreground text-center leading-relaxed', 'text-[13px] text-muted-foreground text-center leading-relaxed font-normal')

# 4. In Empty State, "You don't have any trails..." -> "You don't have any trails or tours yet"
content = content.replace('You don\'t have any trails...', 'You don\'t have any trails or tours yet')

# 5. Empty State icon should be list-dashes with an overlay picture. Current has list-dashes like bars.
# The graphic in empty state is a "document" with a tiny warning/mountain. We current have document bars. Let's make it look slightly closer to design by adjusting padding.

# 6. Change active selected border to solid purple, remove background tint (in screenshot, active item bg is very subtle dark blue, not bright purple tint). 
content = content.replace('border-primary bg-primary/5', 'border-primary bg-primary/[0.03]')
content = content.replace('border-primary bg-primary/10', 'border-primary bg-primary/[0.03]')
content = content.replace('bg-accent shadow-sm', 'bg-primary/[0.03] shadow-none')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(content)
