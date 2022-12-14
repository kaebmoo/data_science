<?php 

function SearchingChallenge($str) {

  // code goes here
  $pattern = "/^[A-Za-z][0-9a-zA-Z]*(?:_+[A-Za-z0-9]+)*$/";
  $length =  strlen($str);
  
  // echo $output;
  if (preg_match($pattern, $str)) {
    $str = "true";
  }
  else {
    $str = "false";
  }
  if($length < 4) {
    $str = "false";
  }
  if($length > 25) {
    $str = "false";
  }
  return $str;
}
   
// keep this function call here  
echo SearchingChallenge(fgets(fopen('php://stdin', 'r')));  

?>