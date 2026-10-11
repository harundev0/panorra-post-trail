with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make all status bars consistent (no z-index so they get covered, or z-10 and overlay z-50)
text = text.replace('bg-background z-10 shrink-0', 'bg-background shrink-0')
text = text.replace('bg-background z-20 shrink-0', 'bg-background shrink-0')
text = text.replace('bg-background z-30 shrink-0', 'bg-background shrink-0')
text = text.replace('bg-background z-40 bg-background', 'bg-background shrink-0')
text = text.replace('bg-background z-40 shrink-0', 'bg-background shrink-0')
text = text.replace('bg-background shrink-0 z-40 bg-background', 'bg-background shrink-0')

# Also fix the specific occurence in interactive prototype
text = text.replace('shrink-0 z-40 bg-background', 'shrink-0 bg-background')

# Now make sure the modal overlay is highly elevated
text = text.replace('z-10 bg-black/60', 'z-[60] bg-black/60')
text = text.replace('z-40 bg-black/60', 'z-[60] bg-black/60')

# Make sure the sheet itself is even higher
text = text.replace('z-20 shadow-[0_-20px_50px_rgba', 'z-[70] shadow-[0_-20px_50px_rgba')
text = text.replace('z-50 flex flex-col justify-end', 'z-[60] flex flex-col justify-end') # interactive wrapper

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
