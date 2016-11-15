<!DOCTYPE html>
<?php
if(isset($_SESSION["location"])){
    echo $_SESSION["location"];
}
else{
	echo "no data";
}
?>