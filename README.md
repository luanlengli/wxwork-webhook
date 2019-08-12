# wxwork-webhook
alertmanager webhook for wechat


# build image
```bash
docker build -t <image_name>:<tag> .
```


# quick start
```bash
docker run -d \
           --restart=on-failure:5 \
           -p 5233:5233 \
           image_name:tag \
           --wxwork-webhook https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxx \
           --listen 0.0.0.0 \
           --port 5233
```
