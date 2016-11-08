SpaceAPI for Perth Artifactory
==============================

See http://hackerspaces.nl/spaceapi/ for background

default.json contains the templated items - live status will added before
moving to the site by some other means (python script most likely)

For scratchpad purposes, a hacky combination of PHP and Javascript (combining the worst of both) lets you do
```PHP
<div id="spaceapi"></div>
<script>
<?php # spaceapi stuff
$json = file_get_contents("spaceapi.json");
echo "var spaceapi = $json;\n";
?>
document.getElementById("spaceapi").innerHTML = spaceapi.state.message ;
</script>
```
