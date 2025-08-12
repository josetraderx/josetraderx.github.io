#!/usr/bin/env python3
"""
Script de verificación de optimizaciones críticas
Confirma que las optimizaciones de imágenes están implementadas correctamente
"""

import os
import glob

def check_webp_files():
    """Verifica que los archivos WebP optimizados existen"""
    print("🔍 VERIFICACIÓN DE ARCHIVOS WebP OPTIMIZADOS")
    print("=" * 50)
    
    webp_files = ["slide_01.webp", "slide_02.webp", "slide_03.webp"]
    
    for webp_file in webp_files:
        if os.path.exists(webp_file):
            size = os.path.getsize(webp_file) / 1024  # KB
            print(f"✅ {webp_file}: {size:.1f} KB")
        else:
            print(f"❌ {webp_file}: NO ENCONTRADO")

def check_css_references():
    """Verifica que el CSS referencia las imágenes WebP"""
    print("\n🎨 VERIFICACIÓN DE REFERENCIAS CSS")
    print("=" * 50)
    
    css_file = "../../css/templatemo-finance-business.css"
    
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        webp_refs = ["slide_01.webp", "slide_02.webp", "slide_03.webp"]
        
        for webp_ref in webp_refs:
            if webp_ref in content:
                print(f"✅ {webp_ref}: Referenciado en CSS")
            else:
                print(f"❌ {webp_ref}: NO encontrado en CSS")
    else:
        print(f"❌ Archivo CSS no encontrado: {css_file}")

def calculate_savings():
    """Calcula el ahorro total conseguido"""
    print("\n💰 RESUMEN DE AHORROS")
    print("=" * 50)
    
    jpg_files = ["slide_01.jpg", "slide_02.jpg", "slide_03.jpg"]
    webp_files = ["slide_01.webp", "slide_02.webp", "slide_03.webp"]
    
    total_original = 0
    total_optimized = 0
    
    for jpg_file, webp_file in zip(jpg_files, webp_files):
        if os.path.exists(jpg_file) and os.path.exists(webp_file):
            original_size = os.path.getsize(jpg_file)
            optimized_size = os.path.getsize(webp_file)
            reduction = ((original_size - optimized_size) / original_size) * 100
            
            total_original += original_size
            total_optimized += optimized_size
            
            print(f"{jpg_file.replace('.jpg', '')}: {original_size/1024:.1f} KB → {optimized_size/1024:.1f} KB (-{reduction:.1f}%)")
    
    if total_original > 0:
        total_reduction = ((total_original - total_optimized) / total_original) * 100
        total_savings = (total_original - total_optimized) / 1024
        
        print(f"\n🎯 TOTAL:")
        print(f"Tamaño original: {total_original/1024:.1f} KB")
        print(f"Tamaño optimizado: {total_optimized/1024:.1f} KB")
        print(f"Ahorro total: {total_savings:.1f} KB ({total_reduction:.1f}%)")
        
        # Estimación de impacto en Core Web Vitals
        if total_savings > 1000:  # Más de 1MB ahorrado
            print(f"\n🚀 IMPACTO ESTIMADO:")
            print(f"- LCP mejorado significativamente")
            print(f"- FCP reducido en ~{total_savings/100:.1f}s en conexiones lentas")
            print(f"- Speed Index mejorado")

def main():
    """Función principal de verificación"""
    print("🎯 VERIFICACIÓN DE OPTIMIZACIONES CRÍTICAS")
    print("=" * 60)
    
    check_webp_files()
    check_css_references()
    calculate_savings()
    
    print("\n✨ VERIFICACIÓN COMPLETADA")
    print("=" * 60)
    print("💡 Próximo paso: Probar en PageSpeed Insights")
    print("🔗 https://pagespeed.web.dev/report?url=https://www.josetraderx.com/")

if __name__ == "__main__":
    main()
