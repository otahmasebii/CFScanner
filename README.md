# This is a Forl from MortezaBashsiz cfscanner project

# CloudFlare Scanner
This script scans Millions of Cloudflare IP addresses and generates a result file containing the IPs which are work with CDN

This script uses v2ray+vmess+websocket+tls by default and if you want to use it behind your Cloudflare proxy then you have to set up a vmess account, otherwise, it will use the default configuration.

# CFScanner - Python

The script is designed to scan Cloudflare's edge IPs and locate ones that are viable for use with v2ray/xray. It aims to identify edge IPs that are accessible and not blocked.

CFSCanner runs on different operating systems including and not limited to:

- Linux
- MacOS
- Windows
- Android (termux, UserLAnd, etc.)

# Dependencies

- Python (>=3.6)
- Libraries
  - requests
  - pysocks
  - rich


## Creating a custom config file (optional)

- If you want to use the default sudoer config, you can skip this step

* create a config json file (e.g., myconfig.json) with the following content. replace the values with your own!

```json
{
	"protocol": "vless",
	"port": 443,
	"user": {
                "encryption": "none",
                "flow": "",
                "id": "<usr-id>",
                "level": 8,
                "security": "auto"
              },
	"streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "fingerprint": "",
          "publicKey": "",
          "serverName": "<server_name>",
          "shortId": "",
          "show": false,
          "spiderX": ""
        },
        "wsSettings": {
          "headers": {
            "Host": "<server_name>"
          },
          "path": "/"
        }
      },
	"subnetsList": "https://raw.githubusercontent.com/otahmasebii/CFScanner/main/config/cf.local.iplist"
}
```

# Executing program

## **How to run**

In the following, you can find examples of running the script with and without custom config and subnets file. For more details on the arguments, please see [Arguments](#anchor-args)

- To run with sudoer default config and only one thread on the default subnets list:

  ```bash
  cfscanner.py
  ```

  alternatively, you could use the following command:

  ```bash
  python3 -m cfscanner
  ```

- To run with sudoer default config and 8 threads:

  ```bash
  cfscanner -t 8
  ```

- To run on a list of subnets:

  ```bash
  cfscanner -t 8 -c ./myconfig.json -s ./mysubnets.selection
  ```

  Each line of the file can be either a subnet (in CIDR notation) or a single IP (v4 or v6):

  ```
  1.0.0.0/24
  108.162.218.0/24
  108.162.236.0/22
  162.158.8.0/21
  162.158.60.0/24
  162.158.82.12
  2606:4700::/120
  2606:4700:3032::6815:3819
  ...
  ```

- To run with a minimum acceptable download speed of 100 kilobytes per second

  ```bash
  cfscanner -t 8 -c ./myconfig.json -s ./mysubnets.selection -DS 100
  ```

- To run with a minimum acceptable download and upload speed (in KBps)

  ```bash
  cfscanner -t 8 -c ./myconfig.json -s ./mysubnets.selection -DS 100 -US 25
  ```

- To run and try each IP multiple (in this case 3) times. An IP is marked ok if it passes all the tests.

  ```bash
  cfscanner --threads 8 --config ./myconfig.json --subnets ./mysubnets.selection --download-speed 100 --upload-speed 25 --tries 3
  ```

- To run on a random sample of size 20 of the subnets and minimum acceptable download and upload speed of 10 KBps with the default config

  ```bash
  cfscanner -t 8 -DS 10 -US 10 -r 20
  ```

---

## <a name="anchor-args"></a>Arguments

To use this tool, you can specify various options as follows:

#### Help

To see the help message, use the `--help` or `-h` option.

#### General Options

- `--threads`, `-t`: Number of threads to use for parallel scanning. Default value is 1.
- `--tries`, `-n`: Number of times to try each IP. An IP is marked as OK if all tries are successful. Default value is 1.
- `--subnets`, `-s`: The path to the custom subnets file. Each line should be either a single ip (v4 or v6) or a
  subnet in cidr notation (v4 or v6). If not provided, the program will
  read the list of cidrs from [https://github.com/otahmasebii/CFScanner/blob/main/config/cf.local.iplist](https://github.com/otahmasebii/CFScanner/blob/main/config/cf.local.iplist).

#### Random Scan Options

- `--sample`, `-r`: Size of the random sample to take from each subnet. The sample size can either
  be a float between 0 and 1 ($0 < s < 1$) or an integer ($ s \ge 1$). If it is a float, it will be
  interpreted as a percentage of the subnet size. If it is an integer, it
  will be interpreted as the number of ips to take from each subnet. If
  not provided, the program will take all ips from each subnet
- `--shuffle-subnets`: If passed, the subnets will be shuffled before scanning.

#### Xray Config Options

- `--config`, `-c`: The path to the config file. For config file example, see [sudoer default config](https://github.com/otahmasebii/CFScanner/blob/main/config/ClientConfig.json). If not provided, the program will read the [default sudoer config](https://github.com/otahmasebii/CFScanner/blob/main/config/ClientConfig.json) file.
- `--template`: Path to the proxy (v2ray/xray) client file template. By default vmess_ws_tls is used.
- `--binpath`, `-b`: Path to the v2ray/xray binary file. If not provided, will use the latest compatible version of xray.
- `--novpn`: If passed, xray/v2ray service will not be started and the program will not use vpn.
- `--startprocess-timeout`: Maximum time (in seconds) to wait for xray/v2ray process to start. Default value is 5.

#### Fronting Speed Test Options

- `--fronting-timeout`, `-FT`: Maximum time to wait for fronting response. Default value is 1.

#### Download Speed Test Options

- `--download-speed`, `-DS`: Minimum acceptable download speed in kilobytes per second. Default value is 50.
- `--download-latency`, `-DL`: Maximum allowed latency (seconds) for download. Default value is 2.
- `--download-time`, `-DT`: Maximum (effective, excluding http time) time to spend for each download. Default value is 2.

#### Upload Speed Test Options

- `--upload-test`, `-U`: If passed, upload test will be conducted. If not passed, only download and fronting test will be conducted.
- `--upload-speed`, `-US`: Minimum acceptable upload speed in kilobytes per second. Default value is 50.
- `--upload-latency`, `-UL`: Maximum allowed latency (seconds) for upload. Default value is 2.
- `--upload-time`, `-UT`: Maximum (effective, excluding http time) time (in seconds) to spend for each upload. Default value is 2.

## Remarks

- In the current version, an IP is marked "OK", only if it passes all tries of the experiment
- The size of the file for download is determined based on the arguments `download-speed` and `download-time` (similar for upload as well). Therefore, it is recommended to choose these parameters carefully based on your expectations, internet speed and the number of threads being used

# **Results**

The results will be stored in the `results` directory. Each line of the generated **csv** file includes a Cloudflare edge ip together with the following values:

- `avg_download_speed `: Average download speed in mbps
- `avg_upload_speed`: Average upload speed in mbps
- `avg_download_latency`: Average download latency in ms
- `avg_upload_latency`: Average upload latency in ms
- `avg_download_jitter`: Average jitter during downloads in ms
- `avg_upload_jitter`: Average jitter during uploads in ms
- `download_speed_1,...,n_tries`: Values of download speeds in mbps for each download
- `upload_speed_1,...,n_ties`: Values of download speeds in mbps for each upload
- `download_latency_1,...,n_tries`: Values of download latencies in ms
- `download_latency_1,..._n_tries`: Values of upload latencies in ms
---