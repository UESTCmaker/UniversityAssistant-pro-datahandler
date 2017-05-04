<?php
$fp = fopen('D:/data/number.txt','r');
$newfile = fopen('D:/data/new_number.txt','w');
$done = 0;
while(!$done){
    $line = fgets($fp);
$new = preg_replace('/\D/s', '', $line);
fwrite($newfile,$new);
fwrite($newfile,',');
if($line==''){
    $done=1;
}
}
fclose($fp);
fclose($newfile);
?>