1) External files
`<img src="aaa.png"/>` in the xml files

2) Embedding base64
- `openssl enc -base64 -in aaa.png > aaa.b64`
- `<img src="data:image/png;base64,..."/>` copy/paste aaa.b64 into ...
