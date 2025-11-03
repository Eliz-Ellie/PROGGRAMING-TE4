<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <title>Ämnen & Betyg</title>
</head>
<body>
<?php
date_default_timezone_set('Europe/Stockholm');
$name = $_POST['name'] ?? '';
$date = date('Y-m-d');
?>
<form method="POST">
  <input type="text" name="name" placeholder="Ditt namn">
  <button>Skicka</button>
</form>
<?php if ($name): ?>
  <p>Hej <?= htmlspecialchars($name) ?>! Idag är det <?= $date ?>.</p>
<?php endif; ?>

</body>