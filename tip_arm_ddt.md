
### ARM DDT license checkup
- curl http://license_server:port_number/status.html >log
- Open log file and find User Name

## license error
- At Ubuntu20
- Message `Error communicating with License server: XXX.YYY.ZZZ : proxy denied connection`
- Solution: unset http_proxy; unset https_proxy
