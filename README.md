# generate configuration for proxy tools(just nginx for now)
```js
    server {        
        listen 443 ssl;
        server_name example.com;

        ssl_certificate cert/fullchain.pem;
        ssl_certificate_key cert/example.com.key;


        @{% 'user/.conf' %}
        @{% 'product/.conf' %}
        @{% 'sms/.conf' %}
        @{% 'mail/.conf' %}
        location / {
            proxy_pass http://frontend:3000;
        }
    }
```

## Installation

```bash
pip install otoconf
```

## Usage

```bash
python -m otoconf
```
or
```bash
python -m otoconf -t nginx --conf /path/to/nginx.conf --output /path/to/oto.conf
```

for more information, please run `python -m otoconf --help`

