import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for Interactive
interactive_pattern = r'<!-- Right Action Sidebar -->\s*<div class="absolute right-4 bottom-52 flex flex-col items-center gap-5 z-20 select-none drop-shadow-md">[\s\S]*?</div>\s*<!-- Bottom Gradient Overlay -->'

replacement = """<!-- Right Action Sidebar -->
            <div class="absolute right-3.5 bottom-48 flex flex-col items-center gap-4 z-20 select-none drop-shadow-md">
                <button class="flex flex-col items-center gap-1.5 active:scale-90 transition-transform outline-none group text-white">
                    <div class="w-[42px] h-[42px] rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10 group-hover:bg-black/60 transition-colors">
                        <i class="ph ph-heart text-[22px]"></i>
                    </div>
                    <span class="text-[11px] font-bold drop-shadow-sm">0</span>
                </button>
                <button class="flex flex-col items-center gap-1.5 active:scale-90 transition-transform outline-none group text-white">
                    <div class="w-[42px] h-[42px] rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10 group-hover:bg-black/60 transition-colors">
                        <i class="ph ph-chat-circle text-[22px]"></i>
                    </div>
                    <span class="text-[11px] font-bold drop-shadow-sm">0</span>
                </button>
                <button class="flex flex-col items-center gap-1.5 active:scale-90 transition-transform outline-none group text-white">
                    <div class="w-[42px] h-[42px] rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10 group-hover:bg-black/60 transition-colors">
                        <i class="ph ph-bookmark-simple text-[22px]"></i>
                    </div>
                    <span class="text-[11px] font-bold drop-shadow-sm">0</span>
                </button>
                <button class="flex flex-col items-center gap-1.5 active:scale-90 transition-transform outline-none group text-white">
                    <div class="w-[42px] h-[42px] rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10 group-hover:bg-black/60 transition-colors">
                        <i class="ph ph-share-fat text-[22px]"></i>
                    </div>
                    <span class="text-[11px] font-bold drop-shadow-sm">0</span>
                </button>
            </div>

            <!-- Bottom Gradient Overlay -->"""
            
text = re.sub(interactive_pattern, replacement, text)

# Pattern for Static preview 5
static_pattern = r'<!-- Right sidebar -->\s*<div class="absolute right-3 bottom-44 flex flex-col items-center gap-4 z-20 text-white drop-shadow-md">[\s\S]*?</div>\s*<!-- Bottom Area -->'

static_replacement = """<!-- Right sidebar -->
                    <div class="absolute right-3.5 bottom-40 flex flex-col items-center gap-3.5 z-20 text-white drop-shadow-md">
                        <div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-heart text-[20px]"></i></div><span class="text-[10px] font-bold">0</span></div>
                        <div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-chat-circle text-[20px]"></i></div><span class="text-[10px] font-bold">0</span></div>
                        <div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-bookmark-simple text-[20px]"></i></div><span class="text-[10px] font-bold">0</span></div>
                        <div class="flex flex-col items-center gap-1"><div class="w-10 h-10 rounded-full bg-black/40 backdrop-blur-md flex items-center justify-center border border-white/10"><i class="ph ph-share-fat text-[20px]"></i></div><span class="text-[10px] font-bold">0</span></div>
                    </div>

                    <!-- Bottom Area -->"""

text = re.sub(static_pattern, static_replacement, text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
