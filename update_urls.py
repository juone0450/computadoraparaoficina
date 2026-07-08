import sys

def replace_urls(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace('https://raw.githubusercontent.com/juanmartinbarrientos/Mis-Redes/main/LandingPage/pc_a_medida.jpg', 'https://juone0450.github.io/computadoraparaoficina/pc_a_medida.jpg')
    content = content.replace('https://juanmartinbarrientos.github.io/LandingPage/', 'https://juone0450.github.io/computadoraparaoficina/')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def replace_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make background image relative
    content = content.replace("url('https://raw.githubusercontent.com/juanmartinbarrientos/Mis-Redes/main/LandingPage/pc_a_medida.jpg')", "url('pc_a_medida.jpg')")
    # Just in case the previous replacement logic replaced the github link incorrectly
    content = content.replace("url('https://juone0450.github.io/computadoraparaoficina/pc_a_medida.jpg')", "url('pc_a_medida.jpg')")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_files = [
    r'f:\user usuario\Nueva carpeta (2)\index.html',
    r'f:\user usuario\computadoraparaoficina-main\computadoraparaoficina-main\index.html'
]
css_files = [
    r'f:\user usuario\Nueva carpeta (2)\style.css',
    r'f:\user usuario\computadoraparaoficina-main\computadoraparaoficina-main\style.css',
    r'f:\user usuario\computadoraparaoficina-main\computadoraparaoficina-main\Computadoras-para-oficina\style.css'
]

for f in html_files:
    try:
        replace_urls(f)
    except:
        pass
        
for f in css_files:
    try:
        replace_css(f)
    except:
        pass

print("Done")
