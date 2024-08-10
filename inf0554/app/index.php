<!DOCTYPE html>
<html>

<head>
  <title>Projeto Final</title>
  <style>
    html,
    body {
      height: 100%;
      margin: 0;
    }

    body {
      background: black;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-family: Arial, Helvetica, sans-serif
    }

    h1 {
      font-family: Impact, Charcoal, sans-serif
    }

    canvas {
      border: 1px solid white;
    }

    .container {
      position: relative;
      margin: 0 auto;
    }

    .content {
      position: relative;
      left: 0;
      top: 0;
    }

    .attribute-name {
      display: inline-block;
      font-weight: bold;
      width: 10em;
    }
  </style>
</head>
<?php
  $ch = curl_init();
  $params= array('api-version'=>'2021-02-01', 'format'=>'text');
  $vm_name_url = "http://169.254.169.254/metadata/instance/compute/name" . '?' . http_build_query($params);
  $zone_url = "http://169.254.169.254/metadata/instance/compute/zone" . '?' . http_build_query($params);
  $resourceid_url = "http://169.254.169.254/metadata/instance/compute/resourceId" . '?' . http_build_query($params);// set url
curl_setopt($ch, CURLOPT_URL, $vm_name_url);

// set header
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Metadata:true'));

//return the transfer as a string
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

// $output contains the output string
$vm_name = curl_exec($ch);

curl_setopt($ch, CURLOPT_URL, $zone_url);
$zone = curl_exec($ch);

curl_setopt($ch, CURLOPT_URL, $resourceid_url);
$resource_id = curl_exec($ch);

// close curl resource to free up system resources
curl_close($ch);

  ?>

<body>
  <div class="container">
    <div class="content">
      <h1>Projeto Final INF0554</h1>
      <p><span class="attribute-name">VM Name:</span><code><?php echo $vm_name; ?></code></p>
      <p><span class="attribute-name">Instance ID:</span><code><?php echo $resource_id; ?></code></p>
      <p><span class="attribute-name">Availability Zones:</span><code><?php echo $zone; ?></code></p>
    </div>
  </div>
</body>
</html>
