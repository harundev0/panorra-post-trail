import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I need to match the 360 Toolbar in both the Interactive version and the Static Preview 5.
# The HTML looks like this:
# <!-- 360 Toolbar -->
# <div class="flex items-center h-11 bg-[#111111]/80 backdrop-blur-lg rounded-[14px] px-1 border border-white/10 mx-auto w-full mb-3 shadow-[0_4px_20px_rgba(0,0,0,0.5)]">
# ...
# </div>

toolbar_pattern_interactive = r'<!-- 360 Toolbar -->\s*<div class="flex items-center h-11 bg-\[#111111\]/80 backdrop-blur-lg rounded-\[14px\] px-1 border border-white/10 mx-auto w-full mb-3 shadow-\[0_4px_20px_rgba\(0,0,0,0\.5\)\]">[\s\S]*?</div>\s*<!-- Swipe Up Trigger -->'

toolbar_pattern_static = r'<div class="flex items-center h-10 bg-\[#111111\]/80 backdrop-blur-md rounded-xl px-1 border border-white/10 mb-2">[\s\S]*?</div>\s*(<div class="flex flex-col items-center justify-center gap-0\.5 w-full pt-1 pb-1 text-white/90">)'

# Wait, checking exactly how the static one is marked. Let's use simpler replacement.
text = re.sub(toolbar_pattern_interactive, '<!-- Swipe Up Trigger -->', text)
text = re.sub(toolbar_pattern_static, r'\1', text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
