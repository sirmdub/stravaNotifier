docker build -t stravanotifier:build .
docker create --name stravanotifierBuild stravanotifier:build
docker cp stravanotifierBuild:/usr/src/app/stravaNotifier.zip /tmp/
docker rm stravanotifierBuild

