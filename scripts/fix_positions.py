import re

with open('tourmkr_states_step2.html', 'r', encoding='utf-8') as f:
    step2 = f.read()

# In tourmkr_states_step2.html:
# 1. Look for the "360 Scene" preview component (from `<!-- NEW MOBILE PREVIEW COMPONENT -->` to its end)
preview_component_regex = r'(<!-- NEW MOBILE PREVIEW COMPONENT -->[\s\S]*?<!-- Bottom: Details & Mini Map -->[\s\S]*?</div>\s*</div>\s*</div>)'

match = re.search(preview_component_regex, step2)
if match:
    preview_html = match.group(1)
    # Remove it from its current position
    step2 = step2.replace(preview_html, '')
    
    # Also remove the "Add Custom Waypoint" button
    step2 = re.sub(r'<button class="w-full h-11 mt-2 rounded-xl border border-dashed[\s\S]*?Add Custom Waypoint\s*</button>', '', step2)
    
    # Place the preview_html ABOVE "Key Waypoints & Highlights (Scrolled into view)" in State 2
    # And in State 1 too? Let's check where the user wants it.
    # The user says: "bagian ini add nya hapus dan post nya simpan di atas" (for this part, remove the Add button, and save/put the post above).
    # In State 2 (Scrolled):
    # Above `<!-- Key Waypoints & Highlights (Scrolled into view) -->`, insert preview_html!
    target = '<!-- Key Waypoints & Highlights (Scrolled into view) -->'
    step2 = step2.replace(target, preview_html + '\n\n                        ' + target)

with open('tourmkr_states_step2.html', 'w', encoding='utf-8') as f:
    f.write(step2)

print("step2 updated")

# Same for tourmkr_states_map_focus.html if present
with open('tourmkr_states_map_focus.html', 'r', encoding='utf-8') as f:
    mf = f.read()

match_mf = re.search(preview_component_regex, mf)
if match_mf:
    preview_mf = match_mf.group(1)
    mf = mf.replace(preview_mf, '')
    mf = re.sub(r'<button class="w-full h-11 mt-2 rounded-xl border border-dashed[\s\S]*?Add Custom Waypoint\s*</button>', '', mf)
    # Insert preview_mf above Key Waypoints in map focus if applicable
    # In map focus State 1:
    target_mf = '<!-- Key Waypoints & Highlights -->'
    # only replace the first occurrence in State 1
    parts = mf.split(target_mf)
    if len(parts) > 1:
        mf = parts[0] + preview_mf + '\n\n                        ' + target_mf + parts[1]

with open('tourmkr_states_map_focus.html', 'w', encoding='utf-8') as f:
    f.write(mf)

print("map_focus updated")
