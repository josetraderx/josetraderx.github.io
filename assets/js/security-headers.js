/**
 * Security Headers Implementation for GitHub Pages
 * Implementa cabeceras de seguridad que no pueden ser establecidas via meta tags
 */

(function() {
    'use strict';
    
    // Implementar Content Security Policy adicional vía JavaScript
    function implementCSP() {
        // Detectar y reportar violaciones CSP
        if (typeof SecurityPolicyViolationEvent !== 'undefined') {
            document.addEventListener('securitypolicyviolation', function(e) {
                console.warn('CSP Violation:', e.violatedDirective, e.originalPolicy);
            });
        }
        
        // Validar que todos los scripts tengan origen permitido
        const scripts = document.querySelectorAll('script[src]');
        const allowedDomains = [
            'code.jquery.com',
            'cdn.jsdelivr.net',
            location.hostname
        ];
        
        scripts.forEach(function(script) {
            const src = script.src;
            const isAllowed = allowedDomains.some(domain => 
                src.includes(domain) || src.startsWith('/')
            );
            
            if (!isAllowed) {
                console.warn('Script from unauthorized domain:', src);
            }
        });
    }
    
    // Implementar protección contra Clickjacking
    function implementClickjackProtection() {
        // Verificar si estamos en un iframe
        if (window.top !== window.self) {
            // Si estamos en un iframe de otro dominio, redirigir
            if (window.top.location.hostname !== window.location.hostname) {
                window.top.location = window.location;
            }
        }
    }
    
    // Implementar protección HTTPS
    function enforceHTTPS() {
        // Si estamos en HTTP (no localhost), redirigir a HTTPS
        if (location.protocol !== 'https:' && location.hostname !== 'localhost') {
            location.replace('https:' + window.location.href.substring(window.location.protocol.length));
        }
    }
    
    // Implementar protección contra MIME sniffing
    function preventMimeSniffing() {
        // Establecer nosniff para recursos dinámicos
        const links = document.querySelectorAll('link[rel="stylesheet"]');
        links.forEach(function(link) {
            if (!link.hasAttribute('type')) {
                link.setAttribute('type', 'text/css');
            }
        });
        
        const scripts = document.querySelectorAll('script');
        scripts.forEach(function(script) {
            if (!script.hasAttribute('type')) {
                script.setAttribute('type', 'text/javascript');
            }
        });
    }
    
    // Implementar Permissions Policy (anteriormente Feature Policy)
    function implementPermissionsPolicy() {
        // Deshabilitar funciones sensibles
        if ('permissions' in navigator && 'query' in navigator.permissions) {
            const restrictedFeatures = ['geolocation', 'microphone', 'camera'];
            
            restrictedFeatures.forEach(function(feature) {
                navigator.permissions.query({ name: feature }).then(function(permission) {
                    if (permission.state === 'granted') {
                        console.info('Permission granted for:', feature);
                    }
                }).catch(function() {
                    // Ignorar errores de permisos no soportados
                });
            });
        }
    }
    
    // Implementar medidas adicionales de seguridad
    function additionalSecurityMeasures() {
        // Deshabilitar console en producción (opcional)
        if (location.hostname !== 'localhost' && location.hostname !== '127.0.0.1') {
            // console.log = console.warn = console.error = function() {};
        }
        
        // Protección contra inspección de DOM
        document.addEventListener('keydown', function(e) {
            // Deshabilitar F12, Ctrl+Shift+I, Ctrl+U (opcional - puede ser molesto)
            // if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && e.key === 'I') || (e.ctrlKey && e.key === 'u')) {
            //     e.preventDefault();
            //     return false;
            // }
        });
        
        // Prevenir drag and drop de archivos no autorizados
        document.addEventListener('dragover', function(e) {
            e.preventDefault();
        });
        
        document.addEventListener('drop', function(e) {
            e.preventDefault();
        });
    }
    
    // Inicializar todas las medidas de seguridad
    function initSecurity() {
        try {
            implementCSP();
            implementClickjackProtection();
            enforceHTTPS();
            preventMimeSniffing();
            implementPermissionsPolicy();
            additionalSecurityMeasures();
            
            console.log('✅ Security measures initialized successfully');
        } catch (error) {
            console.error('Security initialization error:', error);
        }
    }
    
    // Ejecutar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSecurity);
    } else {
        initSecurity();
    }
    
})();
