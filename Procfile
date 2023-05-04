
redis_cache: redis-server config/redis_cache.conf
redis_socketio: redis-server config/redis_socketio.conf
redis_queue: redis-server config/redis_queue.conf

web: bench serve --port 8000

socketio: /home/erpnext_user/.nvm/versions/node/v16.15.0/bin/node apps/frappe/socketio.js

watch: bench watch

schedule: bench schedule
worker: bench worker 1>> logs/worker.log 2>> logs/worker.error.log

