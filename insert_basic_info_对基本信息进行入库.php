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
    $Birth = isset($de_json[$i]["Birth"]) ? $de_json[$i]["Birth"] : null;
    $Degree = isset($de_json[$i]["Degree"]) ? $de_json[$i]["Degree"] : null;
    $Email = isset($de_json[$i]["Email"]) ? addslashes($de_json[$i]["Email"]) : null;
    $Gender = isset($de_json[$i]["Gender"]) ? $de_json[$i]["Gender"] : null;
    $Experience = isset($de_json[$i]["Experience"]) ? addslashes($de_json[$i]["Experience"]) : null;
    $Introduction = isset($de_json[$i]["Introduction"]) ? addslashes ($de_json[$i]["Introduction"]) : null;
    $Paper = isset($de_json[$i]["Paper"]) ? addslashes($de_json[$i]["Paper"]) : null;
    $Project = isset($de_json[$i]["Project"]) ? addslashes($de_json[$i]["Project"]) : null;
    $Property = isset($de_json[$i]["Property"]) ? addslashes($de_json[$i]["Property"]) : null;
    $Title = isset($de_json[$i]["Title"]) ? $de_json[$i]["Title"] : null;
    $PhdMajor = isset($de_json[$i]["PhdMajor1Code"]) ? true : false;
    $MasterMajor = isset($de_json[$i]["MasterMajor1Code"]) ? true : false;
    $SearchRate = 0;
    $sql = "INSERT INTO `teachersheet`(`Name`, `IdentifyCode`, `University`, `UniversityCode`, `School`, `SchoolCode`, `Image`, `Gender`, `Birth`, `Title`, `Degree`, `Property`, `Email`, `Experience`, `Introduction`, `Project`, `Paper`, `PhdMajor`, `MasterMajor`, `SearchRate`) VALUES ('$Name', '$IdentifyCode', '$University', '$UniversityCode', '$School', '$SchoolCode', null , '$Gender', '$Birth', '$Title', '$Degree', '$Property', '$Email', '$Experience', '$Introduction', '$Project', '$Paper', '$PhdMajor', '$MasterMajor', '$SearchRate')";
    if (mysqli_query($conn, $sql)) {
        echo "新记录插入成功";
    } else {
        echo "Error: " . $sql . "<br>" .mysqli_error($conn) ;
    }
}
mysqli_close($conn);
?>