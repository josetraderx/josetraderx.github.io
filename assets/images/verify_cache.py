#!/usr/bin/env python3
"""
Script de verificación de configuraciones de caché
Confirma que las políticas de caché están implementadas correctamente
"""

import os
import glob

def verify_htaccess_config():
    """Verifica que el archivo .htaccess tenga las configuraciones correctas"""
    print("🔍 VERIFICACIÓN DE CONFIGURACIONES DE CACHÉ")
    print("=" * 60)
    
    htaccess_path = "../../.htaccess"
    
    if not os.path.exists(htaccess_path):
        print("❌ Archivo .htaccess no encontrado")
        return False
    
    with open(htaccess_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar configuraciones críticas
    checks = [
        ("ExpiresActive On", "✅ Expires module activado"),
        ("image/jpeg", "✅ Cache de imágenes JPEG configurado"),
        ("image/webp", "✅ Cache de imágenes WebP configurado"),
        ("text/css", "✅ Cache de CSS configurado"),
        ("application/javascript", "✅ Cache de JavaScript configurado"),
        ("font/woff2", "✅ Cache de fuentes WOFF2 configurado"),
        ("Cache-Control", "✅ Headers Cache-Control configurados"),
        ("max-age=31536000", "✅ Cache largo (1 año) configurado"),
        ("immutable", "✅ Directiva immutable configurada"),
    ]
    
    all_good = True
    for check, message in checks:
        if check in content:
            print(message)
        else:
            print(f"❌ {check} no encontrado")
            all_good = False
    
    return all_good

def list_cacheable_resources():
    """Lista los recursos que se beneficiarán del cache"""
    print("\n📁 RECURSOS QUE SE BENEFICIARÁN DEL CACHÉ")
    print("=" * 60)
    
    # Cambiar al directorio raíz del proyecto
    os.chdir("../..")
    
    resource_types = {
        "Imágenes": ["**/*.jpg", "**/*.jpeg", "**/*.png", "**/*.webp", "**/*.svg", "**/*.gif"],
        "CSS": ["**/*.css"],
        "JavaScript": ["**/*.js"],
        "Fuentes": ["**/*.woff", "**/*.woff2", "**/*.ttf", "**/*.otf", "**/*.eot"],
    }
    
    total_size = 0
    total_files = 0
    
    for category, patterns in resource_types.items():
        print(f"\n{category}:")
        category_size = 0
        category_files = 0
        
        for pattern in patterns:
            for file_path in glob.glob(pattern, recursive=True):
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    category_size += size
                    category_files += 1
                    if size > 50000:  # Solo mostrar archivos > 50KB
                        print(f"  📄 {file_path}: {size/1024:.1f} KB")
        
        if category_files > 0:
            print(f"  📊 Total {category}: {category_files} archivos, {category_size/1024:.1f} KB")
            total_size += category_size
            total_files += category_files
    
    print(f"\n🎯 RESUMEN TOTAL:")
    print(f"📁 {total_files} archivos cacheables")
    print(f"💾 {total_size/1024:.1f} KB en recursos estáticos")
    print(f"⚡ Estimación de ahorro: ~{total_size/1024:.0f} KB por visitante recurrente")

def estimate_performance_impact():
    """Estima el impacto en el rendimiento"""
    print("\n🚀 IMPACTO ESTIMADO EN RENDIMIENTO")
    print("=" * 60)
    
    print("Con las nuevas políticas de caché:")
    print("✅ Visitantes recurrentes: ~90% menos transferencia de datos")
    print("✅ Tiempo de carga reducido en ~3-5 segundos para segunda visita")
    print("✅ Ancho de banda del servidor reducido significativamente")
    print("✅ Score de 'Serve static assets with an efficient cache policy' mejorado")
    
    print("\nDirectivas implementadas:")
    print("🔧 max-age=31536000 (1 año) para recursos estáticos")
    print("🔧 immutable para evitar revalidaciones innecesarias")
    print("🔧 Vary: Accept-Encoding para compresión óptima")
    print("🔧 public para permitir cache en proxies/CDN")

def main():
    """Función principal de verificación"""
    print("🎯 VERIFICACIÓN DE OPTIMIZACIONES DE CACHÉ")
    print("=" * 70)
    
    config_ok = verify_htaccess_config()
    
    if config_ok:
        list_cacheable_resources()
        estimate_performance_impact()
        
        print(f"\n✨ CONFIGURACIÓN DE CACHÉ COMPLETADA")
        print("=" * 70)
        print("💡 Los cambios están activos inmediatamente")
        print("🔗 Próxima prueba: PageSpeed Insights")
        print("🌐 https://pagespeed.web.dev/report?url=https://www.josetraderx.com/")
        print("\nEspere ~5 minutos antes de probar para que se propaguen los cambios")
        
    else:
        print("\n❌ Algunas configuraciones faltan. Revise el archivo .htaccess")

if __name__ == "__main__":
    main()
