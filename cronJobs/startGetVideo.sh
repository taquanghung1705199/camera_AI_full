o ""
echo $(date '+%Y-%m-%d %H:%M:%S')
/usr/bin/docker service ls --filter label=camera_ai=get_video -q | xargs -I % /usr/bin/sh -c 'docker service scale %=1'
echo "-------------------------------------------------------------"
