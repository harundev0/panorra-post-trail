import re

with open('tourmkr_states_step2.html', 'r', encoding='utf-8') as f:
    step2 = f.read()

with open('tourmkr_states_map_focus.html', 'r', encoding='utf-8') as f:
    map_focus = f.read()

# Extract State 2 from map_focus (The Full Map View)
# In map_focus:
# starts with `<!-- ============================================== -->\n        <!-- STATE 2: FULL MAP VIEW`
# and ends with `<!-- End of State 2 -->` or before `</div>\n    </div>\n</body>`
mf_marker = '<!-- ============================================== -->\n        <!-- STATE 2: FULL MAP VIEW'
mf_part = map_focus[map_focus.find(mf_marker):]
# strip down to the closing of that state's div container
# It ends with:
#                     </div>
#                 </div>
#             </div>
#         </div>

# Let's find the closing of the state 2 flex col in map_focus
end_idx = mf_part.find('    </div>\n\n</body>')
if end_idx != -1:
    state3_html = mf_part[:end_idx].strip()
else:
    # find last </div></div>
    state3_html = mf_part[:mf_part.rfind('</div>\n        </div>') + len('</div>\n        </div>')]

# Rename state heading to State 3: Full Map View (Interactive Map Focus)
state3_html = state3_html.replace('State 2: Map Focus', 'State 3: Map Focus (Full-Screen Route & Waypoints)')

# In step2, let's also ensure the 360 Scene preview card is in State 1 as well, right under Top Actions!
preview_card_html = """                        <!-- 360 Scene / Post Preview (At Top) -->
                        <div class="rounded-[1.5rem] bg-card border border-border/50 overflow-hidden shadow-md relative group aspect-[4/5] w-full isolate mb-8">
                            
                            <!-- 360 Image Background -->
                            <img src="https://picsum.photos/seed/spiritmountain360/800/800" alt="" class="absolute inset-0 w-full h-full object-cover bg-slate-800">
                            
                            <!-- Gradients for text legibility -->
                            <div class="absolute inset-x-0 top-0 h-24 bg-gradient-to-b from-black/60 to-transparent z-10"></div>
                            <div class="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-black/80 via-black/40 to-transparent z-10"></div>
                            
                            <!-- Top Left: Tour Identity -->
                            <div class="absolute top-4 left-4 z-20 flex flex-col gap-2">
                                <div class="bg-background/90 backdrop-blur-md px-3 py-1.5 rounded-full text-[10px] font-bold text-foreground border border-border/50 uppercase tracking-wider flex items-center gap-1.5 shadow-sm w-max">
                                    <i class="ph-fill ph-cube text-primary"></i> 360° Scene
                                </div>
                            </div>
    
                            <!-- Center: Play/Interact Button -->
                            <div class="absolute inset-0 flex items-center justify-center z-20 pointer-events-none">
                                <div class="relative flex items-center justify-center">
                                    <button class="w-16 h-16 rounded-full bg-background/50 backdrop-blur-sm text-white flex items-center justify-center border border-white/20 shadow-lg pointer-events-auto hover:scale-105 active:scale-95 transition-transform">
                                        <i class="ph-fill ph-play text-2xl ml-1"></i>
                                    </button>
                                </div>
                            </div>

                            <!-- Interactive overlay hints -->
                            <div class="absolute top-1/2 left-4 -translate-y-1/2 z-20 text-white/50">
                                <i class="ph ph-caret-left text-2xl"></i>
                            </div>
                            <div class="absolute top-1/2 right-4 -translate-y-1/2 z-20 text-white/50">
                                <i class="ph ph-caret-right text-2xl"></i>
                            </div>
    
                            <!-- Bottom: Details & Mini Map Inset (Clickable to Map Focus) -->
                            <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end z-20">
                                <div class="text-white text-shadow-sm flex-1 pr-4">
                                    <div class="text-lg font-bold leading-tight drop-shadow-md">Spirit Mountain</div>
                                    <div class="text-[12px] font-medium text-white/80 mt-1 flex items-center gap-1"><i class="ph-fill ph-map-pin"></i> High Above Spirit Mountain</div>
                                </div>
                                
                                <!-- Mobile Map Inset -->
                                <div class="w-[84px] h-[84px] bg-card rounded-[14px] border border-white/20 dark:border-white/20 shadow-xl overflow-hidden relative shrink-0 cursor-pointer hover:scale-105 transition-transform">
                                    <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=400&auto=format&fit=crop" alt="" class="w-full h-full object-cover grayscale-[0.3]">
                                    
                                    <!-- Map Route Mockup -->
                                    <svg class="absolute inset-0 w-full h-full pointer-events-none drop-shadow-md" viewBox="0 0 100 100">
                                        <path d="M 20 80 Q 40 50 60 20 T 90 40" fill="none" stroke="#5B4BFF" stroke-width="4" stroke-linecap="round" />
                                    </svg>
                                    
                                    <!-- Current Location Dot -->
                                    <div class="absolute top-[40%] left-[60%] -translate-x-1/2 -translate-y-1/2 w-3.5 h-3.5 rounded-full bg-primary border-[2px] border-white shadow-sm"></div>
                                </div>
                            </div>
                        </div>"""

# Insert preview_card_html into State 1 right after Top Actions
state1_top_actions = """                        <!-- Top Actions -->
                        <div class="flex items-center justify-between mb-8">
                            <button class="h-10 px-4 rounded-xl border border-border bg-card text-foreground text-[14px] font-semibold flex items-center justify-center gap-2 shadow-sm">
                                <i class="ph ph-arrow-left text-lg text-muted-foreground -ml-1"></i> Back
                            </button>
                            <button class="h-10 px-5 rounded-xl bg-primary text-primary-foreground text-[14px] font-semibold flex items-center justify-center gap-2 shadow-md">
                                Next <i class="ph ph-arrow-right text-lg -mr-1"></i>
                            </button>
                        </div>"""

if state1_top_actions in step2:
    step2 = step2.replace(state1_top_actions, state1_top_actions + '\n\n' + preview_card_html)

# Now append State 3 before `    </div>\n\n</body>`
gallery_closing = "    </div>\n\n</body>"
step2 = step2.replace(gallery_closing, "        " + state3_html + "\n\n    </div>\n\n</body>")

# Update gallery container layout for 3 screens
step2 = step2.replace('gap-16 pb-20', 'gap-12 pb-20 max-w-[1400px] mx-auto')

with open('tourmkr_states_step2.html', 'w', encoding='utf-8') as f:
    f.write(step2)

print("Unified step2 successfully!")
