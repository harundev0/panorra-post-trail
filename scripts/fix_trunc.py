with open('tourmkr_states_step2.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('</html>')
if pos != -1:
    clean = text[:pos + len('</html>\n')]
    with open('tourmkr_states_step2.html', 'w', encoding='utf-8') as f:
        f.write(clean)
    print("Truncated after first </html> successfully!")
