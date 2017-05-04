<?php
$conn = mysqli_connect("localhost","root","","uppfind");//连接MySQL
if (!$conn) {
    die("连接数据库失败");
}
mysqli_set_charset($conn, 'utf8');
$file = file_get_contents("C:/Users/Dream Maker/PhpstormProjects/first/new.txt");
$de_json = json_decode($file, true);
$count_json = count($de_json);
for($i=0 ;$i<$count_json;$i++ ) {
    $Name = $de_json[$i]["Name"];
    $University = $de_json[$i]["University"];
    $School = $de_json[$i]["School"];
    $UniversityCode = (int)$de_json[$i]["UniversityCode"];
    $SchoolCode = $UniversityCode*1000 + (int)$de_json[$i]["SchoolCode"];
    $IdentifyCode = $SchoolCode*100000 + (int)$de_json[$i]["IdentifyCode"];
    for($j=1;$j<6;$j++){
        if($de_json[$i]["PhdMajor{$j}Code"]){
            $PhdMajorCode = $de_json[$i]["PhdMajor{$j}Code"];
            $PhdMajorName = $de_json[$i]["PhdMajor{$j}Name"];
            $PhdFieldCode = array();
            $PhdFieldName = array();
            for($r=1;$r<6;$r++){
                $PhdFieldCode[$r] = isset($de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Code"])? $de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Code"] : null;
                $PhdFieldName[$r] = isset($de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Name"])? $de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Name"] : null;
            }
            $sql = "INSERT INTO `phdmajorfieldsheet`(`Name`, `IdentifyCode`, `University`, `UniversityCode`, `School`, `SchoolCode`, `MajorCode`, `MajorName`, `Field1Code`, `Field1Name`, `Field2Code`, `Field2Name`, `Field3Code`, `Field3Name`, `Field4Code`, `Field4Name`, `Field5Code`, `Field5Name`) VALUES ('$Name', '$IdentifyCode', '$University', '$UniversityCode', '$School', '$SchoolCode','$PhdMajorCode','$PhdMajorName','$PhdFieldCode[1]','$PhdFieldName[1]','$PhdFieldCode[2]','$PhdFieldName[2]','$PhdFieldCode[3]','$PhdFieldName[3]','$PhdFieldCode[4]','$PhdFieldName[4]','$PhdFieldCode[5]','$PhdFieldName[5]')";
            if (mysqli_query($conn, $sql)) {
                echo "新记录插入成功";
            } else {
                echo "Error: " . $sql . "<br>" .mysqli_error($conn) ;
            }
        }
        if($de_json[$i]["MasterMajor{$j}Code"]) {
            $MasterMajorCode = $de_json[$i]["MasterMajor{$j}Code"];
            $MasterMajorName = $de_json[$i]["MasterMajor{$j}Name"];
            $MasterFieldCode = array();
            $MasterFieldCode = array();
            if ($de_json[$i]["MasterMajor1Code"] != null && $de_json[$i]["PhdMajor1Code"] == null) {
                for ($r = 1; $r < 6; $r++) {
                    $MasterFieldCode[$r] = isset($de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Code"]) ? $de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Code"] : null;
                    $MasterFieldName[$r] = isset($de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Name"]) ? $de_json[$i]["MajorFeildDetail"]["PhdMajor{$j}Field{$r}Name"] : null;
                }
            } elseif ($de_json[$i]["MasterMajor1Code"] != null && $de_json[$i]["PhdMajor1Code"] != null) {
                for ($r = 1; $r < 6; $r++) {
                    $MasterFieldCode[$r] = isset($de_json[$i]["MajorFeildDetail"]["MasterMajor{$j}Field{$r}Code"]) ? $de_json[$i]["MajorFeildDetail"]["MasterMajor{$j}Field{$r}Code"] : null;
                    $MasterFieldName[$r] = isset($de_json[$i]["MajorFeildDetail"]["MasterMajor{$j}Field{$r}Name"]) ? $de_json[$i]["MajorFeildDetail"]["MasterMajor{$j}Field{$r}Name"] : null;
                }
            }
            $sql = "INSERT INTO `mastermajorfieldsheet`(`Name`, `IdentifyCode`, `University`, `UniversityCode`, `School`, `SchoolCode`, `MajorCode`, `MajorName`, `Field1Code`, `Field1Name`, `Field2Code`, `Field2Name`, `Field3Code`, `Field3Name`, `Field4Code`, `Field4Name`, `Field5Code`, `Field5Name`) VALUES ('$Name', '$IdentifyCode', '$University', '$UniversityCode', '$School', '$SchoolCode','$MasterMajorCode','$MasterMajorName','$MasterFieldCode[1]','$MasterFieldName[1]','$MasterFieldCode[2]','$MasterFieldName[2]','$MasterFieldCode[3]','$MasterFieldName[3]','$MasterFieldCode[4]','$MasterFieldName[4]','$MasterFieldCode[5]','$MasterFieldName[5]')";
            if (mysqli_query($conn, $sql)) {
                echo "新记录插入成功";
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
        }
    }
}
mysqli_close($conn);
?>