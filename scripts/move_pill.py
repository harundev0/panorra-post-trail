import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# First, remove the pill from the Right Action Sidebar
# It looks like:
#                 <!-- Navigation Pill -->
#                 <div class="flex items-center justify-between w-[72px] h-[38px] px-4 mt-2 ...

pill_pattern_interactive = r'\s*<!-- Navigation Pill -->\s*<div class="flex items-center justify-between w-\[72px\] h-\[38px\] px-4 mt-2[^>]*>[\s\S]*?</div>'
text = re.sub(pill_pattern_interactive, '', text)

pill_pattern_static = r'\s*<!-- Navigation Pill -->\s*<div class="flex items-center justify-between w-\[64px\] h-\[32px\] px-3\.5 mt-1\.5[^>]*>[\s\S]*?</div>'
text = re.sub(pill_pattern_static, '', text)


# Now, insert it next to the avatar/profile block at the bottom
# For Interactive:
# The avatar block is inside `<div class="absolute bottom-0 inset-x-0 z-20 flex flex-col px-4 pb-4 select-none">`
# and looks like:
#                 <!-- User Profile -->
#                 <div class="flex items-center gap-3 mb-4">
#                     ...
#                 </div>

pill_interactive = """
                    <!-- Navigation Pill -->
                    <div class="flex items-center justify-between w-[72px] h-[38px] px-4 rounded-full bg-black/40 backdrop-blur-md border border-white/10 text-white drop-shadow-sm cursor-pointer hover:bg-black/60 transition-colors shrink-0 outline-none">
                        <i class="ph-bold ph-caret-left text-[15px]"></i>
                        <i class="ph-bold ph-caret-right text-[15px]"></i>
                    </div>"""

# I need to wrap the User Profile and the Pill in a flex apart container to align them
# `<div class="flex items-center justify-between mb-4"><div class="flex items-center gap-3">...profile...</div> ...Pill... </div>`

def replace_interactive_profile(match):
    profile_html = match.group(0)
    # Remove the mb-4 from the inner wrapper so we put it on the new outer wrapper
    profile_html = profile_html.replace('mb-4', '')
    return f'<div class="flex items-center justify-between mb-4 w-full">{profile_html}{pill_interactive}\n                </div>'

text = re.sub(
    r'<!-- User Profile -->\s*<div class="flex items-center gap-3 mb-4">[\s\S]*?</div>\s*</div>',
    replace_interactive_profile,
    text
)

# For Static Preview 5:
# It looks like:
#                         <div class="flex items-center gap-2.5 mb-3">
#                             <div class="w-9 h-9 rounded-full ...

pill_static = """
                            <!-- Navigation Pill -->
                            <div class="flex items-center justify-between w-[64px] h-[32px] px-3.5 rounded-full bg-black/40 backdrop-blur-md border border-white/10 text-white drop-shadow-sm shrink-0">
                                <i class="ph-bold ph-caret-left text-[14px]"></i>
                                <i class="ph-bold ph-caret-right text-[14px]"></i>
                            </div>"""

def replace_static_profile(match):
    profile_html = match.group(0)
    profile_html = profile_html.replace(' mb-3', '')
    return f'<div class="flex items-center justify-between w-full mb-3">{profile_html}{pill_static}\n                        </div>'

# This matches the Filo Rial avatar block in static preview 5
pattern_static_prof = r'<div class="flex items-center gap-2.5 mb-3">\s*<div class="w-9 h-9 rounded-full bg-\[#A69389\].*?</div>\s*<div class="flex-1 drop-shadow-md">\s*<h2.*?</h2>\s*<p.*?</p>\s*</div>\s*</div>'
text = re.sub(pattern_static_prof, replace_static_profile, text)


with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
