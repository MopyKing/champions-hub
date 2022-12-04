
#!/bin/bash

while !  wget db:3306; do 
	sleep 5
done

# This will exec the CMD from the Dockerfile
exec "$@"