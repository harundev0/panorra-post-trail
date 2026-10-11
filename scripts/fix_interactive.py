import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I want to add tabs to the top of the Interactive Prototype Section
# to let the user switch between Create Post flow and Post Detail flow.
# I also need to merge the interactive HTML of Post Detail into the Alpine state.

# Currently Alpine uses: `<div x-data="prototype()"`
# Let's change it to: `<div x-data="prototype()"` and add `activePhone: 'create'` to state.

new_prototype_script = """
    function prototype() {
        return {
            activePhone: 'create', // 'create' or 'detail'
            modalOpen: false,
            modalState: 'loading',
            selectedItem: null,
            detailsOpen: false,
            
            trails: [
                { id: 1, name: 'Batur Caldera Rim Trail', dist: '28.4 km', loc: 'Bali, Indonesia', img: 'https://picsum.photos/seed/bali/100/100' },
                { id: 2, name: 'Rinjani Summit Route', dist: '41.2 km', loc: 'Lombok, Indonesia', img: 'https://picsum.photos/seed/lombok/100/100' },
                { id: 3, name: 'Komodo Island Explorer', dist: '18.6 km', loc: 'NTT, Indonesia', img: 'https://picsum.photos/seed/komodo/100/100' },
                { id: 4, name: 'Taman Nasional Baluran', dist: '12.4 km', loc: 'East Java', img: 'https://picsum.photos/seed/java1/100/100' },
                { id: 5, name: 'Ijen Crater Trail', dist: '14.1 km', loc: 'East Java', img: 'https://picsum.photos/seed/java2/100/100' },
                { id: 6, name: 'Mount Prau Hike', dist: '6.2 km', loc: 'Central Java', img: 'https://picsum.photos/seed/java3/100/100' },
            ],

            openModal(scenario) {
                this.modalOpen = true;
                this.selectedItem = null;
                this.modalState = 'loading';
                setTimeout(() => {
                    if (scenario === 'data') {
                        this.modalState = 'list';
                    } else if (scenario === 'empty') {
                        this.modalState = 'empty';
                    }
                }, 1500);
            },

            closeModal() {
                this.modalOpen = false;
            }
        }
    }
"""

text = re.sub(r'function prototype\(\) \{[\s\S]*?\}', new_prototype_script.strip(), text)


# Now wrap the inner contents of `<div x-data="prototype()" class="w-full max-w-[390px] h-[844px] sm:w-[390px] sm:h-[844px] bg-background relative overflow-hidden flex flex-col rounded-[2.5rem] border-[10px] border-black shadow-2xl shrink-0 transition-colors duration-300">`
# with `<template x-if="activePhone === 'create'">`

pattern_open = r'(<div x-data="prototype\(\)" class="w-full max-w-\[390px\] h-\[844px\] sm:w-\[390px\] sm:h-\[844px\] bg-background relative overflow-hidden flex flex-col rounded-\[2.5rem\] border-\[10px\] border-black shadow-2xl shrink-0 transition-colors duration-300">)'
replacement_open = r'\1\n            <!-- Create Post Flow -->\n            <div x-show="activePhone === \'create\'" class="absolute inset-0 flex flex-col">\n'

text = re.sub(pattern_open, replacement_open, text)

# Close the wrapper before the section ends
# Find where the interactive prototype ends. It ends at `</section>`
# Wait, it ends inside the static view.
# So I need to find the `</div>` that closes `<div x-data="prototype()">` and put the closing `</div>` and the new phone template before it.

interactive_end_pattern = r'            </div>\n        </div>\n    </section>\n\n    <!-- =============================================='

# Let's extract the interactive content from detail 
with open('tourmkr_post_detail.html', 'r', encoding='utf-8') as f:
    detail_html = f.read()

detail_interactive_start = r'<!-- 360 Background Image -->'
detail_interactive_end = r'<!-- ==============================================\n    <!-- 2. STATIC PREVIEWS'
# extract between them

part = detail_html[detail_html.find(detail_interactive_start) : detail_html.find("        </div>\n    </section>\n\n    <!-- ==============================================")]

detail_interactive_HTML = """
            </div> <!-- Close Create Flow -->

            <!-- Post Detail (360) Flow -->
            <div x-show="activePhone === 'detail'" style="display: none;" class="absolute inset-0 flex flex-col bg-black">
""" + part

text = text.replace('            </div>\n        </div>\n    </section>\n\n    <!-- ==============================================', detail_interactive_HTML + '\n        </div>\n    </section>\n\n    <!-- ==============================================')


# Now add the toggles on top of the interactive prototype
toggle_html = """
        <div class="flex bg-card border border-border p-1 rounded-xl shadow-sm mb-2">
            <button @click="activePhone = 'create'" :class="activePhone === 'create' ? 'bg-primary text-primary-foreground shadow' : 'text-muted-foreground hover:text-foreground'" class="px-5 py-2 rounded-lg text-sm font-semibold transition-all outline-none">Create Post</button>
            <button @click="activePhone = 'detail'" :class="activePhone === 'detail' ? 'bg-primary text-primary-foreground shadow' : 'text-muted-foreground hover:text-foreground'" class="px-5 py-2 rounded-lg text-sm font-semibold transition-all outline-none">Post Detail (360)</button>
        </div>
"""
# insert before interactive mockup container
text = text.replace('<!-- Interactive Mockup Container -->', '<!-- Interactive Mockup Container -->\n        <div x-data="{}" x-init="$watch(\'activePhone\', () => {})"></div>\n' + toggle_html)
# Wait, I need the toggle to be inside the x-data scope.
# move x-data up!
text = text.replace('x-data="prototype()" class="w-full max-w-[390px]', 'class="w-full max-w-[390px]')
text = text.replace('class="text-center">\n            <h2 class="text-3xl font-bold mb-2">Interactive Prototype</h2>', 'class="text-center">\n            <h2 class="text-3xl font-bold mb-2">Interactive Prototype</h2>')
text = text.replace('<section class="flex flex-col items-center gap-8">', '<section x-data="prototype()" class="flex flex-col items-center gap-8">')


with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
