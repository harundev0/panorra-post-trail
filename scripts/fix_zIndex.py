# The bug is because I set the overlay to z-[60] and the modal sheet to z-50!
# If the overlay is z-[60] and the sheet is z-50, then the overlay will completely cover the bottom sheet! 🤦♂️

import re
with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I want the modal sheets in static previews to be z-[70] so they appear ABOVE the overlay!
# Wait, look at this:
# <div class="absolute bottom-0 left-0 right-0 h-[88%] bg-background flex flex-col pt-3 z-50 shadow-[0_-20px_50px_rgba(0,0,0,0.3)] rounded-t-[2rem]">

# Replace z-50 with z-[70] in the bottom sheets of the static sections:
html = html.replace('pt-3 z-50 shadow', 'pt-3 z-[70] shadow')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done!")
