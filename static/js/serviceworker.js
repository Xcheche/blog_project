// var staticCacheName = "djangopwa-v1";

// self.addEventListener("install", function (event) {
//   event.waitUntil(
//     caches.open(staticCacheName).then(function (cache) {
//       return cache.addAll([""]);
//     })
//   );
// });

// self.addEventListener("fetch", function (event) {
//   var requestUrl = new URL(event.request.url);
//   if (requestUrl.origin === location.origin) {
//     if (requestUrl.pathname === "/") {
//       event.respondWith(caches.match(""));
//       return;
//     }
//   }
//   event.respondWith(
//     caches.match(event.request).then(function (response) {
//       return response || fetch(event.request);
//     })
//   );
// });


// serviceworker.js

// Cache version - update this to force refresh of cache on new deploy
const staticCacheName = "djangopwa-v2";

// Files to cache - add all static assets your app needs offline
const filesToCache = [
  "/", // Cache homepage
  "/static/images/favicon.svg",
  "/static/images/favicon.ico",
  "/static/images/favicon-96x96.png",
  "/site.webmanifest",
  "/serviceworker.js",
 
  // Add other static assets like CSS, JS, fonts here if needed
];

// Install event - cache app shell files
self.addEventListener("install", (event) => {
  console.log("[ServiceWorker] Install");
  event.waitUntil(
    caches.open(staticCacheName).then((cache) => {
      console.log("[ServiceWorker] Caching app shell");
      return cache.addAll(filesToCache);
    }).then(() => {
      // Activate this service worker immediately without waiting
      return self.skipWaiting();
    })
  );
});

// Activate event - clean old caches and take control of clients ASAP
self.addEventListener("activate", (event) => {
  console.log("[ServiceWorker] Activate");
  event.waitUntil(
    // Delete old caches not matching current cache version
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== staticCacheName) {
            console.log("[ServiceWorker] Removing old cache:", key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => {
      // Take control of all clients immediately
      return self.clients.claim();
    })
  );
});

// Fetch event - respond with cached content if available
// Also fetch from network and update cache in background
self.addEventListener("fetch", (event) => {
  // Ignore non-GET requests (optional)
  if (event.request.method !== "GET") {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          // Update cache with fresh response for next time
          return caches.open(staticCacheName).then((cache) => {
            cache.put(event.request, networkResponse.clone());
            return networkResponse;
          });
        })
        .catch(() => {
          // If network fetch fails (offline), fallback to cached response
          return cachedResponse;
        });
      // Show offline.html for navigation (HTML) pages
      if (event.request.headers.get("accept").includes("text/html")) {
        return caches.match("/static/offline.html");
      }

      // Return cached response immediately, or wait for network fetch
      return cachedResponse || fetchPromise;
    })
  );
});
