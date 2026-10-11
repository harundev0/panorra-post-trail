import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    ui_html = f.read()

with open('tourmkr_post_detail.html', 'r', encoding='utf-8') as f:
    detail_html = f.read()

# Extract the static previews from tourmkr_post_detail.html
# They start with <!-- ====== PREVIEW 1: Base 360 ====== --> and end before <!-- ====== PREVIEW 2: Details Sheet ====== --> ... to the end of the section

start_marker = "<!-- ====== PREVIEW 1: Base 360 ====== -->"
end_marker = "</section>"

detail_previews = detail_html[detail_html.find(start_marker) : detail_html.rfind(end_marker)]

# Let's adjust preview numbers nicely.
# Existing static previews in tourmkr_ui.html are 1 through 4.
detail_previews = detail_previews.replace('1. Post 360 View', '5. Post 360 View')
detail_previews = detail_previews.replace('2. Details (Swipe Up)', '6. Details (Expanded)')
detail_previews = detail_previews.replace('PREVIEW 1:', 'PREVIEW 5:')
detail_previews = detail_previews.replace('PREVIEW 2:', 'PREVIEW 6:')

# Inject into tourmkr_ui.html right before the last closing </div> of the static sections flex container
# Find the end of the flex container for static previews in tourmkr_ui.html.
# The static sections container looks like `<div class="flex flex-wrap justify-center gap-12 w-full items-start">`
# and ends with `</div>\n    </section>\n\n</div>\n\n<script>`

injection_point = "        </div>\n    </section>\n\n</div>"
ui_html = ui_html.replace(injection_point, "            " + detail_previews + "\n" + injection_point)

# I should also update the text "Screen States" description 
ui_html = ui_html.replace('True bottom sheet simulation and layout parity.', 'Includes Create Post flow and Post Detail (360) screens.')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(ui_html)

print("done")

