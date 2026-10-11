with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# For the static previews, I replaced:
# <div class="absolute inset-0 bg-background flex flex-col pt-[50px] z-10 shadow-[0_-10px_30px_rgba(0,0,0,0.1)]">
#     <div class="w-full flex justify-center pt-2 pb-1 absolute top-[44px] z-50 bg-background"><div class="w-10 h-[5px] bg-border rounded-full"></div></div>

# With:
# <!-- Background -->
# <div class="absolute inset-0 bg-black/60 dark:bg-black/80 backdrop-blur-sm z-10"></div>
# <!-- Sheet -->
# <div class="absolute bottom-0 left-0 right-0 h-[90%] bg-background flex flex-col pt-4 z-20 shadow-[0_-20px_40px_rgba(0,0,0,0.2)] rounded-t-[2rem] overflow-hidden">
#     <div class="w-full flex justify-center pb-4 shrink-0 bg-background z-50"><div class="w-12 h-1.5 bg-border rounded-full"></div></div>

# Wait, this replace means I replaced 1 container div (the old absolute wrapper) with an empty backdrop div AND a new sheet container div.
# So I didn't add an extra unbalanced open div to the static previews, because the replacement string has 1 closed div (backdrop) and 1 open div (sheet).
# So the previews are perfectly balanced!

# Furthermore, let's fix the absolute layout inside the Interactive Bottom Sheet context.
# In the original, I used:
# class="absolute inset-0 z-50 bg-background flex flex-col pt-12 shadow-[0_-20px_40px_rgba(0,0,0,0.1)] rounded-t-[2rem]"

# Let's verify everything is okay visually in the code.
