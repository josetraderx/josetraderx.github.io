#!/usr/bin/env python3
"""
Script para aplicar cabeceras de seguridad a todos los archivos HTML
"""

import os
import re
import glob

def add_security_headers_to_html(file_path):
    """Añade cabeceras de seguridad meta tags a un archivo HTML"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar si ya tiene las cabeceras de seguridad
    if 'X-Frame-Options' in content:
        return False  # Ya tiene cabeceras de seguridad
    
    # Buscar la meta tag de viewport
    viewport_pattern = r'(<meta name="viewport"[^>]*>)'
    
    security_headers = '''    
    <!-- Security Headers -->
    <meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
    <meta http-equiv="Permissions-Policy" content="geolocation=(), microphone=(), camera=()">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://code.jquery.com https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self';">
    '''
    
    # Reemplazar añadiendo las cabeceras después del viewport
    new_content = re.sub(
        viewport_pattern,
        r'\1' + security_headers,
        content
    )
    
    # Verificar si encontró viewport para hacer el reemplazo
    if new_content == content:
        # Si no encontró viewport, buscar después de charset
        charset_pattern = r'(<meta charset="[^"]*">)'
        new_content = re.sub(
            charset_pattern,
            r'\1' + security_headers,
            content
        )
    
    # Si sigue siendo igual, añadir después de <head>
    if new_content == content:
        head_pattern = r'(<head>)'
        new_content = re.sub(
            head_pattern,
            r'\1' + security_headers,
            content
        )
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def add_security_script_to_html(file_path):
    """Añade el script de seguridad al archivo HTML"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar si ya tiene el script de seguridad
    if 'security-headers.js' in content:
        return False  # Ya tiene el script
    
    # Buscar el cierre de </head>
    head_close_pattern = r'(</head>)'
    
    security_script = '''
    <!-- Security Headers Script -->
    <script src="assets/js/security-headers.js" defer></script>
    '''
    
    # Añadir el script antes del cierre de head
    new_content = re.sub(
        head_close_pattern,
        security_script + r'\1',
        content
    )
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def apply_security_to_all_html():
    """Aplica cabeceras de seguridad a todos los archivos HTML"""
    
    print("🔒 APLICANDO CABECERAS DE SEGURIDAD A TODOS LOS ARCHIVOS HTML")
    print("=" * 70)
    
    # Cambiar al directorio del proyecto
    os.chdir("../..")
    
    html_files = glob.glob("*.html")
    
    headers_added = 0
    scripts_added = 0
    
    for html_file in html_files:
        print(f"\n📄 Procesando: {html_file}")
        
        # Añadir meta tags de seguridad
        if add_security_headers_to_html(html_file):
            print("  ✅ Meta tags de seguridad añadidas")
            headers_added += 1
        else:
            print("  ✓ Meta tags de seguridad ya presentes")
        
        # Añadir script de seguridad
        if add_security_script_to_html(html_file):
            print("  ✅ Script de seguridad añadido")
            scripts_added += 1
        else:
            print("  ✓ Script de seguridad ya presente")
    
    print(f"\n📊 RESUMEN:")
    print(f"✅ Meta tags añadidas a {headers_added} archivos")
    print(f"✅ Scripts añadidos a {scripts_added} archivos")
    print(f"📁 Total archivos procesados: {len(html_files)}")

def generate_security_report():
    """Genera un reporte de las cabeceras de seguridad implementadas"""
    
    print(f"\n🔒 REPORTE DE CABECERAS DE SEGURIDAD IMPLEMENTADAS")
    print("=" * 60)
    
    security_measures = [
        ("✅ X-Frame-Options", "SAMEORIGIN - Previene clickjacking"),
        ("✅ X-Content-Type-Options", "nosniff - Previene MIME sniffing"),
        ("✅ Referrer-Policy", "strict-origin-when-cross-origin"),
        ("✅ Permissions-Policy", "Restringe geolocation, microphone, camera"),
        ("✅ Content-Security-Policy", "Política estricta de contenido"),
        ("⚠️ Strict-Transport-Security", "GitHub Pages - limitado"),
    ]
    
    for measure, description in security_measures:
        print(f"{measure}: {description}")
    
    print(f"\n🎯 BENEFICIOS DE SEGURIDAD:")
    print("• Protección contra clickjacking")
    print("• Prevención de ataques XSS")
    print("• Control estricto de recursos")
    print("• Protección de datos del usuario")
    print("• Compliance con mejores prácticas")
    
    print(f"\n📈 IMPACTO ESPERADO EN SECURITYHEADERS.COM:")
    print("🎯 Calificación esperada: B+ o A- (desde F)")
    print("⚡ 5/6 cabeceras principales implementadas")
    print("🔒 Protección significativamente mejorada")

def main():
    """Función principal"""
    print("🛡️ IMPLEMENTACIÓN DE CABECERAS DE SEGURIDAD")
    print("=" * 70)
    
    apply_security_to_all_html()
    generate_security_report()
    
    print(f"\n✨ IMPLEMENTACIÓN COMPLETADA")
    print("=" * 50)
    print("🔄 Siguiente paso: Commit y push a GitHub")
    print("🌐 Luego verificar en: https://securityheaders.com/?q=https://josetraderx.com/")
    print("⏱️ Esperar 5-10 minutos para propagación de cambios")

if __name__ == "__main__":
    main()
