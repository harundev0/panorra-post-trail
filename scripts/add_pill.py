import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

pill_html = """
                <!-- Navigation Pill -->
                <div class="flex items-center justify-between w-[72px] h-[38px] px-4 mt-2 rounded-full bg-black/40 backdrop-blur-md border border-white/10 text-white drop-shadow-sm cursor-pointer hover:bg-black/60 transition-colors">
                    <i class="ph-bold ph-caret-left text-[15px]"></i>
                    <i class="ph-bold ph-caret-right text-[15px]"></i>
                </div>"""

# Replace in interactive prototype
# Find the end of the sidebar
interactive_target = r'                    <span class="text-\[11px\] font-bold drop-shadow-sm">0</span>\n                </button>\n            </div>'
new_interactive = r'                    <span class="text-[11px] font-bold drop-shadow-sm">0</span>\n                </button>' + pill_html + '\n            </div>'
text = re.sub(interactive_target, new_interactive, text)

# Replace in static preview 5
static_pill_html = """
                        <!-- Navigation Pill -->
                        <div class="flex items-center justify-between w-[64px] h-[32px] px-3.5 mt-1.5 rounded-full bg-black/40 backdrop-blur-md border border-white/10 text-white drop-shadow-sm">
                            <i class="ph-bold ph-caret-left text-[14px]"></i>
                            <i class="ph-bold ph-caret-right text-[14px]"></i>
                        </div>"""

static_target = r'<div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-share-fat text-\[20px\]"></i></div><span class="text-\[10px\] font-bold">0</span></div>\n                    </div>'
new_static = r'<div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-share-fat text-[20px]"></i></div><span class="text-[10px] font-bold">0</span></div>' + static_pill_html + '\n                    </div>'
text = re.sub(static_target, new_static, text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
