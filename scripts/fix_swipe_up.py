import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the "Swipe Up" trigger in Interactive section
interactive_find = r'<!-- Swipe Up Trigger -->\s*<button @click="detailsOpen = true" class="flex flex-col items-center justify-center gap-1 w-full pt-1 pb-1 active:scale-95 transition-transform opacity-90 text-white outline-none">\s*<div class="flex items-center gap-1\.5">\s*<i class="ph-fill ph-google-cardboard text-\[15px\]"></i>\s*<i class="ph-bold ph-caret-up text-\[15px\]"></i>\s*<i class="ph-bold ph-arrow-right text-\[12px\]"></i>\s*</div>\s*<span class="text-\[12px\] font-semibold tracking-wide">Swipe up for details</span>\s*</button>'

new_interactive = """<!-- Swipe Up Trigger -->
                <button @click="detailsOpen = true" class="flex flex-col items-center justify-center gap-1.5 w-full pt-2 pb-1 active:scale-95 transition-transform opacity-[0.85] text-white outline-none">
                    <i class="ph-bold ph-caret-up text-[16px]"></i>
                    <span class="text-[12px] font-semibold tracking-wide" style="font-weight: 600;">Swipe up for details</span>
                </button>"""

text = re.sub(interactive_find, new_interactive, text)

# Replace the "Swipe Up" trigger in Static segment 5
static_find = r'<div class="flex flex-col items-center justify-center gap-0\.5 w-full pt-1 pb-1 text-white/90">\s*<div class="flex items-center gap-1"><i class="ph-fill ph-google-cardboard text-\[13px\]"></i><i class="ph-bold ph-caret-up text-\[13px\]"></i><i class="ph-bold ph-arrow-right text-\[10px\]"></i></div>\s*<span class="text-\[11px\] font-semibold tracking-wide">Swipe up for details</span>\s*</div>'

new_static = """<div class="flex flex-col items-center justify-center gap-1 w-full pt-1 pb-1 text-white/90">
                            <i class="ph-bold ph-caret-up text-[15px]"></i>
                            <span class="text-[11px] font-semibold tracking-wide">Swipe up for details</span>
                        </div>"""

text = re.sub(static_find, new_static, text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
