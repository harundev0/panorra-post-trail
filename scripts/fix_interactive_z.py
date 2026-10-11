import re
with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# In the interactive prototype, the backdrop doesn't have a z-index set explicitly on itself, it relies on DOM order.
# BUT wait! The wrapper for the interactive overlay is:
# class="absolute inset-0 z-[60] flex flex-col justify-end"
# And then inside it:
# 1. <div class="absolute inset-0 bg-black/60 ..."></div>  (this is the backdrop)
# 2. <div class="relative w-full h-[88%] bg-background ..."></div> (this is the modal content)
# Because both are inside the same wrapper, and #2 comes AFTER #1 in the DOM, #2 should be on top of #1.

# Is it possible that the backdrop in the interactive prototype is hiding the modal content?
# NO - the image you sent me is of the STATIC PREVIEWS! Not the interactive prototype!
# The image shows "Preview 2", "Preview 3", and "Preview 4" (notice they are side by side).
# Yes! The bug was EXCLUSIVELY in the static previews where I accidentally set they overlay to z-[60] and the modal content to z-50.

# Check that the change was successfully applied to all previews.
print(text.count('z-[70] shadow-[0_-20px_50px_rgba(0,0,0,0.3)]'))
