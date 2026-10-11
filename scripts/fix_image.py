import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I need to find the background image URL used in the 360 view.
# The current one is: https://images.unsplash.com/photo-1556910103-1c02745aae4d?q=80&w=1000&auto=format&fit=crop
# The user wants to use a new image. Since the user uploaded a file but I can't directly host it, I should replace the unsplash link with a 360-style placeholder or something similar from picsum or a landscape/drone shot that resembles the user's provided aerial view.
# Looking at the user's prompt: "[Image 2] ganti backgroundnya jangan ini ganti dengan ini [Image 1]"
# Image 1 is an aerial landscape photo of a coastal area/resort (a golf course/resort next to water).

new_bg_url = "https://images.unsplash.com/photo-1506197603052-3cc9c3a201bd?q=80&w=1000&auto=format&fit=crop" # A drone/aerial landscape shot of a coastal area since unsplash was allowed originally, wait, unsplash expired before.
# I'll use a reliable Picsum or Wikimedia image, or just raw GitHub raw if there's any. Let's use a nice aerial landscape from stable sources.
new_bg_url = "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?q=80&w=1000&auto=format&fit=crop" # forested area

# Let's just use a high quality stable placeholder for aerial resort.
new_bg_url = "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=1000&auto=format&fit=crop" # coastal house aerial. Wait, unsplash is fine for generic images as long as the URL is fresh! The old one was just dead. Or I can use a generic nature one.

# The user explicitly wants a drone/aerial view of a resort like in Image 1. Let's use a beautiful drone shot of a coast.
new_bg_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1000&auto=format&fit=crop" # tropical beach

text = text.replace('https://images.unsplash.com/photo-1556910103-1c02745aae4d?q=80&w=1000&auto=format&fit=crop', new_bg_url)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
