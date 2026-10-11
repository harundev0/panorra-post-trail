with open('tourmkr_states_step2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find lines up to line 780 and keep only State 1, State 2, and State 3
pos = text.find('        <!-- ==============================================\n        <!-- STATE 2: SCROLLED DOWN (MORE WAYPOINTS)       -->\n        <!-- ============================================== -->\n        <div class="flex flex-col items-center gap-4">\n            <h2 class="text-sm font-semibold text-primary uppercase tracking-widest">State 2: Scrolled (More Waypoints)</h2>', 500)

if pos != -1:
    clean_text = text[:pos].strip() + "\n\n    </div>\n\n</body>\n</html>"
    with open('tourmkr_states_step2.html', 'w', encoding='utf-8') as f:
        f.write(clean_text)
    print("Cleaned duplicate states successfully!")
else:
    print("Could not find second occurrence")

