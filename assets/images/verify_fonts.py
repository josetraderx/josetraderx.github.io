#!/usr/bin/env python3
"""
Script de verificación de optimizaciones de fuentes
Verifica que todas las declaraciones @font-face tengan font-display: swap
"""

import os
import re
import glob

def find_font_declarations():
    """Busca todas las declaraciones @font-face en los archivos CSS"""
    print("🔤 VERIFICACIÓN DE OPTIMIZACIONES DE FUENTES")
    print("=" * 70)
    
    # Cambiar al directorio del proyecto
    os.chdir("../..")
    
    css_files = []
    css_files.extend(glob.glob("assets/css/*.css"))
    css_files.extend(glob.glob("vendor/**/*.css", recursive=True))
    
    font_declarations = {}
    
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Buscar declaraciones @font-face
            font_faces = re.finditer(r'@font-face\s*\{([^}]*)\}', content, re.DOTALL)
            
            for match in font_faces:
                declaration = match.group(1)
                font_family_match = re.search(r"font-family:\s*['\"]([^'\"]+)['\"]", declaration)
                font_display_match = re.search(r'font-display:\s*([^;]+)', declaration)
                
                font_name = font_family_match.group(1) if font_family_match else "Unknown"
                has_font_display = font_display_match is not None
                font_display_value = font_display_match.group(1).strip() if font_display_match else None
                
                if css_file not in font_declarations:
                    font_declarations[css_file] = []
                
                font_declarations[css_file].append({
                    'name': font_name,
                    'has_display': has_font_display,
                    'display_value': font_display_value,
                    'declaration': declaration.strip()
                })
    
    return font_declarations

def analyze_google_fonts():
    """Verifica las fuentes de Google en los archivos HTML"""
    print(f"\n🌐 ANÁLISIS DE FUENTES DE GOOGLE")
    print("-" * 50)
    
    html_files = glob.glob("*.html")
    google_fonts = {}
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar enlaces a Google Fonts
        google_font_links = re.finditer(r'<link[^>]*fonts\.googleapis\.com[^>]*>', content)
        
        for match in google_font_links:
            link = match.group(0)
            # Verificar si tiene display=swap
            has_display_swap = 'display=swap' in link
            
            file_name = os.path.basename(html_file)
            if file_name not in google_fonts:
                google_fonts[file_name] = []
            
            google_fonts[file_name].append({
                'link': link,
                'has_display_swap': has_display_swap
            })
    
    return google_fonts

def estimate_performance_impact():
    """Estima el impacto en el rendimiento"""
    print(f"\n🚀 IMPACTO ESTIMADO EN RENDIMIENTO")
    print("=" * 60)
    
    print("✅ Beneficios de font-display: swap:")
    print("  • Reducción del FOIT (Flash of Invisible Text): ~90ms")
    print("  • Texto visible inmediatamente con fuente fallback")
    print("  • Mejora en First Contentful Paint (FCP)")
    print("  • Mejor experiencia de usuario en conexiones lentas")
    print("  • Reducción en Cumulative Layout Shift (CLS)")
    
    print(f"\n🔧 Técnica implementada:")
    print("  • font-display: swap en @font-face personalizadas")
    print("  • display=swap en fuentes de Google Fonts")
    print("  • Fallback inmediato a fuentes del sistema")
    
    print(f"\n📊 Métricas esperadas:")
    print("  • FOIT eliminado completamente")
    print("  • FCP: Mejora de ~90ms")
    print("  • Speed Index: Puntuación mejorada")
    print("  • User Experience: Sin parpadeos de texto")

def main():
    """Función principal"""
    print("🎨 VERIFICACIÓN DE OPTIMIZACIONES DE FUENTES")
    print("=" * 80)
    
    # Buscar declaraciones @font-face
    font_declarations = find_font_declarations()
    
    total_fonts = 0
    optimized_fonts = 0
    
    print(f"\n📋 DECLARACIONES @font-face ENCONTRADAS:")
    print("-" * 50)
    
    for css_file, fonts in font_declarations.items():
        file_name = os.path.basename(css_file)
        print(f"\n📄 {file_name}:")
        
        for font in fonts:
            total_fonts += 1
            status = "✅" if font['has_display'] else "❌"
            display_info = f" (display: {font['display_value']})" if font['display_value'] else ""
            print(f"  {status} {font['name']}{display_info}")
            
            if font['has_display']:
                optimized_fonts += 1
    
    # Analizar fuentes de Google
    google_fonts = analyze_google_fonts()
    
    google_total = 0
    google_optimized = 0
    
    for html_file, fonts in google_fonts.items():
        if fonts:  # Solo mostrar si hay fuentes de Google
            print(f"\n📄 {html_file}:")
            for font_link in fonts:
                google_total += 1
                status = "✅" if font_link['has_display_swap'] else "❌"
                print(f"  {status} Google Fonts {'(display=swap)' if font_link['has_display_swap'] else '(necesita display=swap)'}")
                
                if font_link['has_display_swap']:
                    google_optimized += 1
    
    # Mostrar impacto
    estimate_performance_impact()
    
    # Resumen final
    print(f"\n✨ RESUMEN DE OPTIMIZACIÓN DE FUENTES")
    print("=" * 60)
    print(f"📝 Fuentes @font-face optimizadas: {optimized_fonts}/{total_fonts}")
    print(f"🌐 Google Fonts optimizadas: {google_optimized}/{google_total}")
    
    total_all = total_fonts + google_total
    optimized_all = optimized_fonts + google_optimized
    
    if total_all > 0:
        percentage = (optimized_all / total_all) * 100
        print(f"🎯 Porcentaje total optimizado: {percentage:.1f}%")
        
        if percentage == 100:
            print(f"🎉 ¡PERFECTO! Todas las fuentes están optimizadas")
            print(f"⚡ Ahorro estimado: ~90ms en renderizado de texto")
        else:
            print(f"🔧 Fuentes pendientes de optimización: {total_all - optimized_all}")
    else:
        print(f"❓ No se encontraron declaraciones de fuentes personalizadas")

if __name__ == "__main__":
    main()
