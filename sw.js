const CACHE_NAME = 'josetraderx-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/about.html',
  '/contact.html',
  '/one-page.html',
  '/portfolio.html',
  '/services.html',
  '/trading-strategies.html',
  '/vendor/bootstrap/css/bootstrap.min.css',
  '/assets/css/fontawesome.css',
  '/assets/css/owl.css',
  '/assets/css/templatemo-finance-business.css',
  '/assets/css/custom-styles.css',
  '/vendor/jquery/jquery.min.js',
  '/vendor/bootstrap/js/bootstrap.bundle.min.js',
  '/assets/js/custom.js',
  '/assets/js/owl.js',
  '/assets/js/slick.js',
  '/assets/js/accordions.js',
  '/assets/js/jquery.singlePageNav.min.js',
  '/assets/images/page-heading-bg.webp',
  '/assets/images/slide_01.webp',
  '/assets/images/slide_02.webp',
  '/assets/images/slide_03.webp',
  '/assets/images/service_01.webp',
  '/assets/images/service_02.webp',
  '/assets/images/service_03.webp',
  '/assets/images/about-image.webp',
  '/assets/images/more-info.webp',
  '/assets/images/client-01.png',
  '/assets/images/client-02.png',
  '/assets/images/client-03.png',
  '/assets/images/client-04.png',
  '/assets/fonts/fontawesome-webfont.woff2?v=4.7.0',
  '/assets/fonts/Flaticon.woff'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});

self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
