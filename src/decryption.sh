path=$(pwd)
password=LunaLovesHackingHellYeah
echo -e $(openssl enc -d -aes-256-cbc -salt -in $path/data.txt.enc  -pass pass:$password)
