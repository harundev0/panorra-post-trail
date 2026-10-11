with open('tourmkr_states_step2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect everything from `<!-- STATE 2: SCROLLED DOWN (MORE WAYPOINTS)       -->` to `</body>`
state2_start = "<!-- ==============================================\n        <!-- STATE 2: SCROLLED DOWN (MORE WAYPOINTS)       -->\n        <!-- ============================================== -->"

parts = html.split(state2_start)
state1_part = parts[0]

# Now let's construct State 2 cleanly:
new_state2 = """<!-- ============================================== -->
        <!-- STATE 2: SCROLLED DOWN (MORE WAYPOINTS)       -->
        <!-- ============================================== -->
        <div class="flex flex-col items-center gap-4">
            <h2 class="text-sm font-semibold text-primary uppercase tracking-widest">State 2: Scrolled (More Waypoints)</h2>
            
            <div class="w-[390px] h-[844px] bg-background relative overflow-hidden flex flex-col rounded-[2.5rem] border-[8px] border-gray-300 dark:border-[#1f2937] shadow-2xl shrink-0 transition-colors duration-300">
                <!-- Status Bar -->
                <div class="h-12 flex justify-between items-center px-6 text-[15px] font-semibold shrink-0 bg-background select-none">
                    <span>9:41</span>
                    <div class="flex gap-2 items-center">
                        <i class="ph-fill ph-cell-signal-full text-[15px]"></i>
                        <i class="ph-fill ph-wifi-high text-[15px]"></i>
                        <i class="ph-fill ph-battery-full text-[20px]"></i>
                    </div>
                </div>

                <!-- Simulating a "Scrolled Down" layout -->
                <div class="flex-1 flex flex-col overflow-y-auto no-scrollbar pb-8 relative bg-background">
                    
                    <!-- Collapsed Top Navigation Area to Simulate Scroll -->
                    <div class="sticky top-0 bg-background/90 backdrop-blur-md z-30 border-b border-border shadow-sm flex items-center justify-between px-4 py-3 select-none">
                        <button class="text-muted-foreground"><i class="ph ph-arrow-left text-xl"></i></button>
                        <div class="text-center">
                            <div class="text-[13px] font-bold text-foreground">Trail & Route Details</div>
                            <div class="text-[10px] text-muted-foreground">Step 2 of 3</div>
                        </div>
                        <button class="px-3 py-1.5 bg-primary text-primary-foreground text-[12px] font-semibold rounded-lg">Next</button>
                    </div>

                    <div class="px-6 pt-6">

                        <!-- 360 Scene Preview (Moved to the Top!) -->
                        <div class="rounded-[1.5rem] bg-card border border-border/50 overflow-hidden shadow-md relative group aspect-[4/5] w-full isolate mb-6">
                            
                            <!-- 360 Image Background -->
                            <img src="https://picsum.photos/seed/spiritmountain360/800/800" alt="" class="absolute inset-0 w-full h-full object-cover bg-slate-800" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'800\\' height=\\'600\\' viewBox=\\'0 0 800 600\\'%3E%3Crect width=\\'800\\' height=\\'600\\' fill=\\'%231e293b\\'/%3E%3C/svg%3E'">
                            
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

                            <!-- Interactive overlay hints (Mobile specific) -->
                            <div class="absolute top-1/2 left-4 -translate-y-1/2 z-20 text-white/50">
                                <i class="ph ph-caret-left text-2xl"></i>
                            </div>
                            <div class="absolute top-1/2 right-4 -translate-y-1/2 z-20 text-white/50">
                                <i class="ph ph-caret-right text-2xl"></i>
                            </div>
    
                            <!-- Bottom: Details & Mini Map -->
                            <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end z-20">
                                <div class="text-white text-shadow-sm flex-1 pr-4">
                                    <div class="text-lg font-bold leading-tight drop-shadow-md">Spirit Mountain</div>
                                    <div class="text-[12px] font-medium text-white/80 mt-1 flex items-center gap-1"><i class="ph-fill ph-map-pin"></i> High Above Spirit Mountain</div>
                                </div>
                                
                                <!-- Mobile Map Inset -->
                                <div class="w-[84px] h-[84px] bg-card rounded-[14px] border border-white/20 dark:border-white/20 shadow-xl overflow-hidden relative shrink-0">
                                    <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=400&auto=format&fit=crop" alt="" class="w-full h-full object-cover grayscale-[0.3]" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'400\\' height=\\'400\\' viewBox=\\'0 0 400 400\\'%3E%3Crect width=\\'400\\' height=\\'400\\' fill=\\'%2394a3b8\\'/%3E%3C/svg%3E'">
                                    
                                    <!-- Map Route Mockup -->
                                    <svg class="absolute inset-0 w-full h-full pointer-events-none drop-shadow-md" viewBox="0 0 100 100">
                                        <path d="M 20 80 Q 40 50 60 20 T 90 40" fill="none" stroke="#5B4BFF" stroke-width="4" stroke-linecap="round" />
                                    </svg>
                                    
                                    <!-- Current Location Dot -->
                                    <div class="absolute top-[40%] left-[60%] -translate-x-1/2 -translate-y-1/2 w-3.5 h-3.5 rounded-full bg-primary border-[2px] border-white shadow-sm"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Key Waypoints & Highlights (Scrolled into view) -->
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
                        </div>

                    </div>
                </div>
            </div>
        </div>

    </div>

</body>
</html>"""

full_clean_html = state1_part + new_state2

with open('tourmkr_states_step2.html', 'w', encoding='utf-8') as f:
    f.write(full_clean_html)

print("done cleaning tourmkr_states_step2.html")
