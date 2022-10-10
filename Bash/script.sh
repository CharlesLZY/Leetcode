LOG_FILE="log"

### [INFO] 2022/09/17 23:13:58 "GET / HTTP/1.1" 200 "address: https://www.google.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
### [WARNING] 2022/09/17 23:13:60 "GET / HTTP/1.1" 404 "address: https://www.google.com.cn" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

### Filter keyword from log flow
tail -f "$LOG_FILE" | while read -r line ; do
  if [[ $line =~ .*\"GET\ /\ HTTP/1.1\"\ (404)\ \"address:\ (.*)\"\ .*$ ]]
  then
    echo "${BASH_REMATCH[2]}" ### BASH_REMATCH[0]: the whole string BASH_REMATCH[i] the ith group (i>0)
  fi
done

