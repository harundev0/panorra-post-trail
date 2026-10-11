import re

with open('tourmkr_ui.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add the custom-ping / animate-ring CSS into tourmkr_ui.html
css_to_add = """
        @keyframes custom-spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .animate-spin-slow {
            animation: custom-spin 2s linear infinite;
        }

        /* Custom pulsing animation for the 360 hotspot */
        @keyframes custom-ping {
            0% { transform: scale(0.8); opacity: 0.8; }
            100% { transform: scale(1.5); opacity: 0; }
        }
        .animate-ring {
            animation: custom-ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
        }
"""
text = re.sub(r'@keyframes custom-spin \{[\s\S]*?\.animate-spin-slow \{[\s\S]*?\}', css_to_add.strip(), text)

with open('tourmkr_ui.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
