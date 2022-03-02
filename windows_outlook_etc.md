## Outlook
- When preview mode doesn't come back to the default
  - Ref: https://helpdesk.eoas.ubc.ca/kb/articles/how-to-set-view-for-all-folders-in-outlook-2013-2016
  - Run `outlook.exe /cleanviews` from the command window

## measuring time over gateway
```
>tracert cnn.com
Tracing route to cnn.com [151.101.193.67]
over a maximum of 30 hops:
  1   232 ms    51 ms    50 ms  ip of gateway
  2    65 ms    52 ms    58 ms  xx.xx.xx.xx
  3     *        *      616 ms  firewall?
  4   381 ms   475 ms     *     xx.xx.xx.xx
  5    80 ms    81 ms   112 ms  151.101.193.67
Trace complete.
```
