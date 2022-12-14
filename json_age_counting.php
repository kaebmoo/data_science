<?php 

  $ch = curl_init('https://coderbyte.com/api/challenges/json/age-counting');
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HEADER, 0);
  $data = curl_exec($ch);
  curl_close($ch);

  // print_r(json_decode($data, true));
  $count = 0;
  $key_age = explode(":", $data);
  $key_age = $key_age[1];
   
  $key_age = ltrim($key_age, "\"");
  $key_age = rtrim($key_age, "\"");
  # print_r($key_age);

  $data_ = explode(",", $key_age);
  
  for ($i = 0; $i < sizeof($data_); $i++) {
    $value = explode("=", $data_[$i]);
    # print_r(array_values($value));
    # print_r($value);
    if (trim($value[0]) == 'age') {
      
      if ($value[1] >= 50) {
        $count++;
      }
    }
  }
  print_r($count);
  

?>