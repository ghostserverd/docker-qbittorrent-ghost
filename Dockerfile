FROM linuxserver/qbittorrent

# add ghost config file
COPY root/ /

WORKDIR /usr/local/bin

# add default qBittorrent.conf
COPY qBittorrent.conf qBittorrent.conf

# add scripts
COPY password-generator.py password-generator.py
COPY qbit-postprocess.sh qbit-postprocess.sh