import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to wrap the Modal Bottom Sheet into a container that acts as an overlay
# Current code has `<div x-show="modalOpen" ... class="absolute inset-0 z-50 bg-background flex flex-col pt-12 shadow-[0_-20px_40px_rgba(0,0,0,0.1)] rounded-t-[2rem]">`

# I will replace the Modal Bottom Sheet HTML with an overlay variant

old_modal = """
            <!-- Modal Bottom Sheet -->
            <div 
                x-show="modalOpen"
                style="display: none;"
                x-transition:enter="transition-transform ease-out duration-300"
                x-transition:enter-start="translate-y-full"
                x-transition:enter-end="translate-y-0"
                x-transition:leave="transition-transform ease-in duration-200"
                x-transition:leave-start="translate-y-0"
                x-transition:leave-end="translate-y-full"
                class="absolute inset-0 z-50 bg-background flex flex-col pt-12 shadow-[0_-20px_40px_rgba(0,0,0,0.1)] rounded-t-[2rem]"
            >
                <div class="absolute top-4 left-1/2 -translate-x-1/2 w-12 h-1.5 bg-border rounded-full z-50"></div>
"""

new_modal = """
            <!-- Modal Overlay & Bottom Sheet -->
            <div 
                x-show="modalOpen"
                style="display: none;"
                class="absolute inset-0 z-50 flex flex-col justify-end"
            >
                <!-- Overlay Backdrop -->
                <div 
                    x-show="modalOpen"
                    x-transition:enter="transition-opacity ease-out duration-300"
                    x-transition:enter-start="opacity-0"
                    x-transition:enter-end="opacity-100"
                    x-transition:leave="transition-opacity ease-in duration-200"
                    x-transition:leave-start="opacity-100"
                    x-transition:leave-end="opacity-0"
                    @click="closeModal()"
                    class="absolute inset-0 bg-black/60 dark:bg-black/80 backdrop-blur-sm"
                ></div>

                <!-- Bottom Sheet Content -->
                <div 
                    x-show="modalOpen"
                    x-transition:enter="transition-transform ease-out duration-300"
                    x-transition:enter-start="translate-y-full"
                    x-transition:enter-end="translate-y-0"
                    x-transition:leave="transition-transform ease-in duration-200"
                    x-transition:leave-start="translate-y-0"
                    x-transition:leave-end="translate-y-full"
                    class="relative w-full h-[90%] bg-background flex flex-col pt-4 shadow-[0_-20px_40px_rgba(0,0,0,0.2)] rounded-t-[2rem] overflow-hidden"
                >
                    <!-- Drag Handle -->
                    <div class="w-full flex justify-center pb-4 shrink-0 bg-background z-50">
                        <div class="w-12 h-1.5 bg-border rounded-full"></div>
                    </div>
"""

# Replace in string
html = html.replace(old_modal, new_modal)

# I should also fix the static previews to look like bottom sheets with an overlay.
# The static previews currently just show the modal taking the whole screen without the header.
# Let's adjust preview 2,3,4 to have an overlay and the modal at the bottom 90% of the screen.

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("done")
