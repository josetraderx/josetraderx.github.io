#!/usr/bin/env python3
"""
Script para optimizar las imágenes críticas del slider
Convierte JPG a WebP con alta compresión manteniendo buena calidad
"""

from PIL import Image
import os

def optimize_image(input_path, output_path, quality=80, max_width=1200):
    """
    Optimiza una imagen convirtiéndola a WebP
    
    Args:
        input_path: Ruta de la imagen original
        output_path: Ruta de la imagen optimizada
        quality: Calidad de compresión (1-100)
        max_width: Ancho máximo de la imagen
    """
    try:
        # Abrir la imagen original
        with Image.open(input_path) as img:
            print(f"Procesando {input_path}")
            print(f"Tamaño original: {img.size}")
            
            # Redimensionar si es necesario
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Redimensionado a: {img.size}")
            
            # Convertir a RGB si es necesario (para WebP)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Guardar como WebP optimizado
            img.save(output_path, "WebP", quality=quality, optimize=True)
            
            # Mostrar estadísticas
            original_size = os.path.getsize(input_path)
            optimized_size = os.path.getsize(output_path)
            reduction = ((original_size - optimized_size) / original_size) * 100
            
            print(f"Guardado como: {output_path}")
            print(f"Tamaño original: {original_size / 1024:.1f} KB")
            print(f"Tamaño optimizado: {optimized_size / 1024:.1f} KB")
            print(f"Reducción: {reduction:.1f}%")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error procesando {input_path}: {e}")

def main():
    """Función principal"""
    print("🔥 OPTIMIZACIÓN DE IMÁGENES CRÍTICAS")
    print("=" * 50)
    
    # Lista de imágenes a optimizar
    images_to_optimize = [
        ("slide_01.jpg", "slide_01.webp", 85),  # LCP - calidad alta
        ("slide_02.jpg", "slide_02.webp", 80),  # Calidad buena
        ("slide_03.jpg", "slide_03.webp", 80),  # Calidad buena
    ]
    
    total_original = 0
    total_optimized = 0
    
    for input_file, output_file, quality in images_to_optimize:
        if os.path.exists(input_file):
            original_size = os.path.getsize(input_file)
            total_original += original_size
            
            optimize_image(input_file, output_file, quality=quality, max_width=1200)
            
            if os.path.exists(output_file):
                optimized_size = os.path.getsize(output_file)
                total_optimized += optimized_size
        else:
            print(f"⚠️ No se encontró: {input_file}")
    
    # Mostrar resumen total
    if total_original > 0:
        total_reduction = ((total_original - total_optimized) / total_original) * 100
        print("\n🎯 RESUMEN TOTAL:")
        print(f"Tamaño original total: {total_original / 1024:.1f} KB")
        print(f"Tamaño optimizado total: {total_optimized / 1024:.1f} KB")
        print(f"Reducción total: {total_reduction:.1f}%")
        print(f"Ahorro: {(total_original - total_optimized) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
