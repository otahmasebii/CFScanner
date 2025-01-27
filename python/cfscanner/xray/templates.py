vmess_ws_tls = '''{
  "inbounds": [
    {
      "port": PORTPORT,
      "listen": "127.0.0.1",
      "tag": "socks-inbound",
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": false,
        "ip": "127.0.0.1"
      },
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "IP.IP.IP.IP",
            "port": CFPORTCFPORT,
            "users": [
              {
                "id": "IDID"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "wsSettings": {
          "headers": {
            "Host": "HOSTHOST"
          },
          "path": "ENDPOINTENDPOINT"
        },
        "tlsSettings": {
          "serverName": "RANDOMHOST",
          "allowInsecure": false
        }
      }
    }
  ],
  "other": {}
}'''

vless_tls = '''{
  "inbounds": [
    {
      "port": PORTPORT,
      "listen": "127.0.0.1",
      "tag": "socks-inbound",
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": false,
        "ip": "127.0.0.1"
      },
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "IP.IP.IP.IP",
            "port": CFPORTCFPORT,
            "users": [
              {
              "encryption": "none",
                "flow": "",
                "id": "IDID",
                "level": 8,
                "security": "auto"
              }
            ]
          }
        ]
      },
      "streamSettings": {{STREAMINGSETTINGS}}
    }
  ],
  "other": {}
}'''
