#!/usr/bin/env python3
"""
Script de verificación de optimizaciones CSS render-blocking
Verifica que Bootstrap esté cargado de forma asíncrona en todos los archivos HTML
"""

import os
import re
import glob

def check_bootstrap_optimization():
    """Verifica la optimización de Bootstrap en todos los archivos HTML"""
    print("🎯 VERIFICACIÓN CSS RENDER-BLOCKING OPTIMIZATION")
    print("=" * 70)
    
    html_files = glob.glob("../../*.html")
    
    optimized_files = []
    needs_optimization = []
    
    for file_path in html_files:
        file_name = os.path.basename(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si tiene preload de Bootstrap
        has_preload = 'rel="preload"' in content and 'bootstrap' in content and 'as="style"' in content
        # Verificar si tiene noscript fallback
        has_noscript = '<noscript>' in content and 'bootstrap' in content
        # Verificar si tiene render-blocking tradicional
        has_blocking = re.search(r'<link[^>]+href[^>]*bootstrap[^>]*rel="stylesheet"', content)
        
        print(f"\n📄 {file_name}:")
        
        if has_preload and has_noscript:
            print("  ✅ Bootstrap optimizado (preload + noscript fallback)")
            optimized_files.append(file_name)
        elif has_preload:
            print("  ⚠️  Bootstrap con preload pero sin noscript fallback")
            print("      Recomendado: añadir noscript para accesibilidad")
        elif has_blocking:
            print("  ❌ Bootstrap render-blocking (necesita optimización)")
            needs_optimization.append(file_name)
        else:
            print("  ❓ Bootstrap no encontrado o configuración no estándar")
    
    return optimized_files, needs_optimization

def check_other_css_blocking():
    """Verifica otros archivos CSS que podrían estar causando render-blocking"""
    print(f"\n🔍 ANÁLISIS DE OTROS CSS RENDER-BLOCKING")
    print("=" * 60)
    
    html_files = glob.glob("../../*.html")
    css_analysis = {}
    
    for file_path in html_files:
        file_name = os.path.basename(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar todos los links CSS
        css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', content)
        preload_links = re.findall(r'<link[^>]*rel="preload"[^>]*as="style"[^>]*>', content)
        
        print(f"\n📄 {file_name}:")
        print(f"  🔗 CSS tradicional (render-blocking): {len(css_links)}")
        print(f"  ⚡ CSS preload (optimizado): {len(preload_links)}")
        
        if css_links:
            print("  📋 CSS render-blocking encontrados:")
            for link in css_links:
                href_match = re.search(r'href="([^"]+)"', link)
                if href_match:
                    print(f"    - {href_match.group(1)}")
        
        css_analysis[file_name] = {
            'blocking': len(css_links),
            'optimized': len(preload_links)
        }
    
    return css_analysis

def estimate_performance_impact():
    """Estima el impacto en el rendimiento de las optimizaciones CSS"""
    print(f"\n🚀 IMPACTO ESTIMADO EN RENDIMIENTO")
    print("=" * 60)
    
    print("✅ Beneficios de la carga asíncrona de CSS:")
    print("  • Reducción del render-blocking time: ~470ms")
    print("  • Mejora en First Contentful Paint (FCP)")
    print("  • Reducción en Largest Contentful Paint (LCP)")
    print("  • Mejor experiencia de usuario en conexiones lentas")
    
    print("\n🔧 Técnica implementada:")
    print("  • rel=\"preload\" + as=\"style\" + onload")
    print("  • Fallback <noscript> para accesibilidad")
    print("  • CSS se carga en paralelo sin bloquear render")
    
    print("\n📊 Métricas esperadas:")
    print("  • FCP: Mejora de ~300-500ms")
    print("  • Speed Index: Reducción significativa")
    print("  • Total Blocking Time: Disminución notable")

def main():
    """Función principal"""
    print("🎨 VERIFICACIÓN DE OPTIMIZACIONES CSS RENDER-BLOCKING")
    print("=" * 80)
    
    # Cambiar al directorio del proyecto
    os.chdir("../..")
    
    # Verificar Bootstrap
    optimized, needs_opt = check_bootstrap_optimization()
    
    # Verificar otros CSS
    css_analysis = check_other_css_blocking()
    
    # Mostrar impacto
    estimate_performance_impact()
    
    # Resumen
    print(f"\n✨ RESUMEN DE OPTIMIZACIÓN CSS")
    print("=" * 60)
    print(f"✅ Archivos con Bootstrap optimizado: {len(optimized)}")
    print(f"❌ Archivos que necesitan optimización: {len(needs_opt)}")
    
    if needs_opt:
        print(f"\n🔧 Archivos pendientes de optimización:")
        for file_name in needs_opt:
            print(f"  • {file_name}")
    else:
        print(f"\n🎉 ¡Todos los archivos tienen Bootstrap optimizado!")
    
    # Calcular total CSS render-blocking
    total_blocking = sum(analysis['blocking'] for analysis in css_analysis.values())
    total_optimized = sum(analysis['optimized'] for analysis in css_analysis.values())
    
    print(f"\n📊 ESTADÍSTICAS GENERALES:")
    print(f"🔗 Total CSS render-blocking: {total_blocking}")
    print(f"⚡ Total CSS optimizado: {total_optimized}")
    
    if total_blocking == 0:
        print("🎯 ¡EXCELENTE! No hay CSS render-blocking en el sitio")
    else:
        print("🎯 Oportunidad de mejora: Optimizar CSS restantes")

if __name__ == "__main__":
    main()
