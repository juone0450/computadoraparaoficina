import sys

glow_css = """
/* ENHANCED BLACK AND ORANGE AESTHETICS */
.nav-item.active {
    box-shadow: 0 0 15px rgba(255, 107, 0, 0.4);
    border: 1px solid var(--primary-color);
}
.platform-btn.active {
    box-shadow: 0 0 20px rgba(255, 107, 0, 0.5) !important;
}
.btn-primary {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-hover));
    color: #ffffff !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    border: none;
}
.btn-primary:hover {
    box-shadow: 0 0 25px rgba(255, 107, 0, 0.6) !important;
    transform: translateY(-3px);
}
.card {
    border: 1px solid rgba(255, 107, 0, 0.15);
}
.card:hover {
    border-color: rgba(255, 107, 0, 0.4);
    box-shadow: 0 8px 30px rgba(255, 107, 0, 0.15);
}
.glitch-text {
    text-shadow: 0 0 8px rgba(255, 107, 0, 0.5);
}
"""

files = [
    r'f:\user usuario\Nueva carpeta (2)\style.css',
    r'f:\user usuario\computadoraparaoficina-main\computadoraparaoficina-main\style.css',
    r'f:\user usuario\computadoraparaoficina-main\computadoraparaoficina-main\Computadoras-para-oficina\style.css'
]

for f in files:
    try:
        with open(f, 'a', encoding='utf-8') as file:
            file.write(glow_css)
        print(f'Enhanced {f}')
    except Exception as e:
        print(f'Error {f}: {e}')
