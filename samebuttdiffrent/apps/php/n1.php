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

if ($name) {
    // DB path: repo_root/data/php.db
    $dbPath = __DIR__ . '/../../data/php.db';
    $pdo = new PDO("sqlite:" . $dbPath);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sql = "INSERT INTO names(name, count) VALUES(:name, 1) ON CONFLICT(name) DO UPDATE SET count = count + 1";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([':name' => $name]);

    $row = $pdo->prepare("SELECT count FROM names WHERE name = :name");
    $row->execute([':name' => $name]);
    $count = $row->fetchColumn();
}
?>
<form method="POST">
  <input type="text" name="name" placeholder="Ditt namn">
  <button>Skicka</button>
</form>
<?php if (!empty($name)): ?>
  <p>Hej <?= htmlspecialchars($name) ?>! Idag är det <?= $date ?>.</p>
  <p>Antal gånger skickat: <?= intval($count) ?></p>
<?php endif; ?>

</body>
</html>
