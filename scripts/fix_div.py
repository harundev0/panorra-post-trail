with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I replaced one root div (the sheet wrapper) with an overlay wrapper + sheet container, 
# meaning I might need one extra closing div for the new wrapper.

# In my replace I did:
# old:
#             <div 
#                 x-show="modalOpen" ... class="...
#             >
#                 <div class="absolute top-4 left-1/2 -translate-x-1/2 w-12 h-1.5 bg-border rounded-full z-50"></div>

# new:
#             <!-- Modal Overlay & Bottom Sheet -->
#             <div 
#                 x-show="modalOpen"
#                 style="display: none;"
#                 class="absolute inset-0 z-50 flex flex-col justify-end"
#             >
#                 <!-- Backdrop -->
#                 <div ...></div>
#                 <!-- Sheet -->
#                 <div ...>
#                     <!-- Handle -->
#                     <div><div></div></div>

# The closing tags were untouched. This means the new setup has:
# Wrapper div (open)
# Backdrop div (opened and closed)
# Sheet div (open)
# Handle div (opened and closed)
# ... inside content ...
# ... untouched closing tags ... which used to close JUST the old Sheet div container. 
# But now I have the Wrapper div AND the Sheet div open. So I am missing one closing div.

# Let's find where the modal finishes in the interactive section.
target = "<!-- ============================================== -->\n    <!-- 2. STATIC PREVIEWS SECTION -->"
parts = text.split(target)

# I need to add one `</div>` before the closing of the section 1.
# The section 1 ends like this:
#                 </div>
#             </div>
#         </div>
#     </section>
# Let's replace `        </div>\n    </section>` with `            </div>\n        </div>\n    </section>`

text = text.replace('        </div>\n    </section>\n\n    <!-- ============================================== -->\n    <!-- 2. STATIC PREVIEWS SECTION -->', '            </div>\n        </div>\n    </section>\n\n    <!-- ============================================== -->\n    <!-- 2. STATIC PREVIEWS SECTION -->')

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Div diff:", text.count('<div') - text.count('</div'))
