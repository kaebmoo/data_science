<?php 

function MathChallenge($str) {

  // code goes here
  $res = -1;
  $length = floor(strlen($str) / 2) + 1;
  for ($i = 1; $i <= $length; $i++) {
    if (!fmod(strlen($str), strlen(substr($str,0,$i))) and str_repeat(substr($str,0,$i), floor(strlen($str) / strlen(substr($str,0,$i))) ) == $str) {
      $res = substr($str,0,$i);
    }
  }
  $str = $res;
  return $str;

}
   
// keep this function call here  
$data = "abcababcababcab";
$data = "GeeksforGeeksGeeksforGeeksGeeksforGeeks";
echo MathChallenge($data);  

?>