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


var staticCacheName = "djangopwa-v1";

var filesToCache = [
  "/", // Cache the homepage
  "/static/images/favicon.svg",
  "/static/images/favicon.ico",
  "/static/images/favicon-96x96.png",
  "/site.webmanifest",
  "/serviceworker.js",
  // Add other static files you want to cache (CSS, JS, fonts, etc)
];

self.addEventListener("install", function (event) {
  console.log("[ServiceWorker] Install");
  event.waitUntil(
    caches.open(staticCacheName).then(function (cache) {
      console.log("[ServiceWorker] Caching app shell");
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener("activate", function (event) {
  console.log("[ServiceWorker] Activate");
  event.waitUntil(
    caches.keys().then(function (keyList) {
      return Promise.all(
        keyList.map(function (key) {
          if (key !== staticCacheName) {
            console.log("[ServiceWorker] Removing old cache", key);
            return caches.delete(key);
          }
        })
      );
    })
  );
});

self.addEventListener("fetch", function (event) {
  console.log("[ServiceWorker] Fetch", event.request.url);
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return response || fetch(event.request);
    })
  );
});
