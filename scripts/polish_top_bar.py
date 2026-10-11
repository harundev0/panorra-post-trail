import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I also noticed in the new Image 2 that the user provided (the new mockup implementation),
# the details bottom sheet swipe trigger uses a slightly different text alignment, and the top bar uses a darker theme.
# Is the top bar icon a white "FR" text instead of an avatar image now?
# Wait! In Image 2, the bottom left avatar is "FR" (Initials instead of image).
# Let's change the avatar to use initials instead of the ui-avatars.com to be fully independent.

# Replace <img src="https://ui-avatars.com/api/?name=Filo+Rial&background=random&color=000&font-size=0.33&bold=true" class="w-full h-full object-cover">
# With <span class="text-[14px] font-bold text-gray-800">FR</span>

old_avatar = '<img src="https://ui-avatars.com/api/?name=Filo+Rial&background=random&color=000&font-size=0.33&bold=true" class="w-full h-full object-cover">'
old_avatar2 = '<img src="https://ui-avatars.com/api/?name=Filo+Rial&background=random&color=000&font-size=0.33&bold=true" class="w-full h-full">'
new_avatar = '<span class="text-sm font-bold text-gray-700">FR</span>'

text = text.replace(old_avatar, new_avatar)
text = text.replace(old_avatar2, new_avatar)

# Also fix the avatar container. Instead of `bg-gray-100` let's make it a nice beige/brownish color `#B8A096` from the screenshot.
# From `<div class="w-[42px] h-[42px] rounded-full flex items-center justify-center bg-gray-100 ...`
# To   `<div class="w-[42px] h-[42px] rounded-full flex items-center justify-center bg-[#B8A096] ...` (And change text inside to black).

# But I'll just change the background of that profile circle.
text = re.sub(r'bg-white shrink-0 border border-white/20 overflow-hidden', r'bg-[#A69389] shrink-0 border border-white/20 overflow-hidden text-gray-900', text)
text = re.sub(r'bg-gray-100 hover:bg-gray-200 transition shrink-0 border border-gray-200 overflow-hidden', r'bg-[#A69389] hover:bg-[#97847A] transition shrink-0 border border-[#A69389]/50 overflow-hidden', text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
