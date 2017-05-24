<?php
$conn = mysqli_connect("120.25.99.223","myuser","findupp","uppfind");//连接MySQL
if (!$conn) {
    die("连接数据库失败");
}
mysqli_set_charset($conn, 'utf8');

$dir = "D:/data/xinanTU/teacher/";
$teacher = scandir($dir);
$numbers = array();
for($i=2;$i<count($teacher);$i++){
    preg_match("(\d*)",$teacher[$i],$number);
    array_push($numbers,$number[0]);
}

$file = file_get_contents("C:/Users/Dream Maker/PhpstormProjects/first/xinanTU_teacher_new.txt");
$de_json = json_decode($file, true);
$count_json = count($de_json);
for($i=0 ;$i<$count_json;$i++ ) {
    $Name = $de_json[$i]["name"];
    $UniversityCode = "10613";
    $SchoolCode = $de_json[$i]["schoolcode"];;
    $IdentifyCode = $de_json[$i]["identifycode"];
    $Title = isset($de_json[$i]["title"]) ? $de_json[$i]["title"]: null;
    $Degree = isset($de_json[$i]["degree"]) ? $de_json[$i]["degree"]: null;
    $id = strval(intval(substr($IdentifyCode, -4)));
    $Image = "/img/default.jpg";
    if(array_search($id, $numbers)!=false){
        $Image = "/img/10613/teacher/$id.jpg";
    }
    $Email = isset($de_json[$i]["email"]) ? $de_json[$i]["email"] : null;
    $Experience = isset($de_json[$i]["exprience"])? addslashes($de_json[$i]["exprience"]) : null;
    $Introduction = isset($de_json[$i]["introduction"]) ? addslashes($de_json[$i]["introduction"]) : null;
    $PhdMajor = 0;
    $MasterMajor = 0;
    $SearchRate = 0;
    $sql = "INSERT INTO `teachersheet`(`Name`, `IdentifyCode`, `UniversityCode`, `SchoolCode`, `Image`, `Title`, `Degree`, `Email`, `Experience`, `Introduction`, `PhdMajor`, `MasterMajor`, `SearchRate`) VALUES ('$Name', '$IdentifyCode', '$UniversityCode', '$SchoolCode','$Image','$Title', '$Degree', '$Email', '$Experience', '$Introduction','$PhdMajor', '$MasterMajor', '$SearchRate')";
    if (mysqli_query($conn, $sql)) {
        echo "新记录插入成功";
    } else {
        echo "Error: " . $Name . " " .mysqli_error($conn) ;
    }
}

mysqli_close($conn);
?>