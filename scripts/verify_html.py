with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's count divs quickly to see if we unbalanced them.
print("Div diff:", text.count('<div') - text.count('</div'))

