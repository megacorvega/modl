while read line; do
  if [ "$last" != "$line" ]; then
    echo $line
    last=$line
  fi  
done