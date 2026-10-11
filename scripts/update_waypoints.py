import re

card_template = """                        <!-- Key Waypoints & Highlights -->
                        <div class="mb-8">
                            <div class="flex items-center justify-between mb-4 px-1">
                                <h2 class="text-[14px] font-bold text-foreground">Key Waypoints & Highlights</h2>
                                <span class="text-[12px] text-muted-foreground font-medium">4 waypoints</span>
                            </div>
                            
                            <div class="flex flex-col gap-3.5">
                                <!-- Card 1 -->
                                <div class="bg-card border border-border/80 rounded-2xl p-4 shadow-sm flex items-start gap-3">
                                    <div class="w-8 h-8 rounded-full bg-emerald-500 text-white flex items-center justify-center text-[13px] font-bold shrink-0 mt-1 shadow-sm">
                                        1
                                    </div>
                                    <div class="flex-1 flex flex-col gap-2.5 min-w-0">
                                        <div class="bg-secondary/70 rounded-xl px-3.5 py-2.5 text-[13px] font-semibold text-foreground truncate border border-border/30">
                                            Trailhead / Start Point
                                        </div>
                                        <div class="flex flex-col gap-1">
                                            <span class="text-[10px] uppercase font-bold tracking-wider text-muted-foreground">HEIGHT (M)</span>
                                            <div class="flex items-center justify-between bg-secondary/70 rounded-xl border border-border/40 overflow-hidden">
                                                <span class="px-3.5 py-2 text-[13px] font-semibold text-foreground">725</span>
                                                <button class="border-l border-border/80 px-4 py-2 text-[13px] font-semibold text-primary hover:text-primary/80 transition-colors">
                                                    Get
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="text-muted-foreground/60 hover:text-foreground shrink-0 mt-2.5 px-0.5">
                                        <i class="ph-bold ph-dots-six-vertical text-lg"></i>
                                    </button>
                                </div>

                                <!-- Card 2 -->
                                <div class="bg-card border border-border/80 rounded-2xl p-4 shadow-sm flex items-start gap-3">
                                    <div class="w-8 h-8 rounded-full bg-blue-500 text-white flex items-center justify-center text-[13px] font-bold shrink-0 mt-1 shadow-sm">
                                        2
                                    </div>
                                    <div class="flex-1 flex flex-col gap-2.5 min-w-0">
                                        <div class="bg-secondary/70 rounded-xl px-3.5 py-2.5 text-[13px] font-semibold text-foreground truncate border border-border/30">
                                            Taman Wisata Alam Gunung Pancar
                                        </div>
                                        <div class="flex flex-col gap-1">
                                            <span class="text-[10px] uppercase font-bold tracking-wider text-muted-foreground">HEIGHT (M)</span>
                                            <div class="flex items-center justify-between bg-secondary/70 rounded-xl border border-border/40 overflow-hidden">
                                                <span class="px-3.5 py-2 text-[13px] font-semibold text-foreground">820</span>
                                                <button class="border-l border-border/80 px-4 py-2 text-[13px] font-semibold text-primary hover:text-primary/80 transition-colors">
                                                    Get
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="text-muted-foreground/60 hover:text-foreground shrink-0 mt-2.5 px-0.5">
                                        <i class="ph-bold ph-dots-six-vertical text-lg"></i>
                                    </button>
                                </div>

                                <!-- Card 3 -->
                                <div class="bg-card border border-border/80 rounded-2xl p-4 shadow-sm flex items-start gap-3">
                                    <div class="w-8 h-8 rounded-full bg-purple-500 text-white flex items-center justify-center text-[13px] font-bold shrink-0 mt-1 shadow-sm">
                                        3
                                    </div>
                                    <div class="flex-1 flex flex-col gap-2.5 min-w-0">
                                        <div class="bg-secondary/70 rounded-xl px-3.5 py-2.5 text-[13px] font-semibold text-foreground truncate border border-border/30">
                                            Pasir Limo Summit (1,075m)
                                        </div>
                                        <div class="flex flex-col gap-1">
                                            <span class="text-[10px] uppercase font-bold tracking-wider text-muted-foreground">HEIGHT (M)</span>
                                            <div class="flex items-center justify-between bg-secondary/70 rounded-xl border border-border/40 overflow-hidden">
                                                <span class="px-3.5 py-2 text-[13px] font-semibold text-foreground">1075</span>
                                                <button class="border-l border-border/80 px-4 py-2 text-[13px] font-semibold text-primary hover:text-primary/80 transition-colors">
                                                    Get
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="text-muted-foreground/60 hover:text-foreground shrink-0 mt-2.5 px-0.5">
                                        <i class="ph-bold ph-dots-six-vertical text-lg"></i>
                                    </button>
                                </div>

                                <!-- Card 4 -->
                                <div class="bg-card border border-border/80 rounded-2xl p-4 shadow-sm flex items-start gap-3">
                                    <div class="w-8 h-8 rounded-full bg-orange-500 text-white flex items-center justify-center text-[13px] font-bold shrink-0 mt-1 shadow-sm">
                                        4
                                    </div>
                                    <div class="flex-1 flex flex-col gap-2.5 min-w-0">
                                        <div class="bg-secondary/70 rounded-xl px-3.5 py-2.5 text-[13px] font-semibold text-foreground truncate border border-border/30">
                                            Pondok Pemburu Campsite
                                        </div>
                                        <div class="flex flex-col gap-1">
                                            <span class="text-[10px] uppercase font-bold tracking-wider text-muted-foreground">HEIGHT (M)</span>
                                            <div class="flex items-center justify-between bg-secondary/70 rounded-xl border border-border/40 overflow-hidden">
                                                <span class="px-3.5 py-2 text-[13px] font-semibold text-foreground">840</span>
                                                <button class="border-l border-border/80 px-4 py-2 text-[13px] font-semibold text-primary hover:text-primary/80 transition-colors">
                                                    Get
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="text-muted-foreground/60 hover:text-foreground shrink-0 mt-2.5 px-0.5">
                                        <i class="ph-bold ph-dots-six-vertical text-lg"></i>
                                    </button>
                                </div>
                            </div>
                        </div>"""

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the entire Key Waypoints block
    pattern = r'<!-- Key Waypoints & Highlights -->[\s\S]*?<!-- Apply Button|<!-- Waypoint 3 \(Expanded|</div>\s*</div>\s*</div>\s*</div>\s*<!-- =============================================='
    
    # Let's inspect where it ends in tourmkr_states_step2.html
    # In State 1, it's followed by:
    #                     </div>
    #                 </div>
    #             </div>
    #         </div>
    
    # In State 2, it's followed by:
    #                                 <button class="w-full h-11 mt-2 rounded-xl border border-dashed
    
    # Let's do a targeted replace for State 1:
    state1_pattern = r'<!-- Key Waypoints & Highlights -->[\s\S]*?(?=</div>\s*</div>\s*</div>\s*</div>\s*<!-- ==============================================)'
    content = re.sub(state1_pattern, card_template + '\n', content)
    
    # In State 2 (Scrolled):
    state2_pattern = r'<!-- Key Waypoints & Highlights \(Scrolled into view\) -->[\s\S]*?(?=<button class="w-full h-11 mt-2 rounded-xl border border-dashed)'
    state2_replacement = card_template.replace('<!-- Key Waypoints & Highlights -->', '<!-- Key Waypoints & Highlights (Scrolled into view) -->')
    content = re.sub(state2_pattern, state2_replacement + '\n                                ', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

replace_in_file('tourmkr_states_step2.html')

# In tourmkr_states_map_focus.html:
with open('tourmkr_states_map_focus.html', 'r', encoding='utf-8') as f:
    mf_content = f.read()

mf_pattern = r'<!-- Key Waypoints & Highlights -->[\s\S]*?(?=</div>\s*</div>\s*</div>\s*</div>\s*<!-- ==============================================)'
mf_content = re.sub(mf_pattern, card_template + '\n', mf_content)

with open('tourmkr_states_map_focus.html', 'w', encoding='utf-8') as f:
    f.write(mf_content)
print("Updated tourmkr_states_map_focus.html")

