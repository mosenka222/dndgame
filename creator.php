<?
	$link = mysqli_connect("127.0.0.1", "u1162862_mosenka", "Qclash123!", "u1162862_database");
	mysqli_set_charset($link, "utf8");

	session_start();
	$id = session_id();
    
	$answer = mysqli_query($link, "SELECT player_name, player_marker, player_banned FROM players WHERE player_session = '$id'");
	$row = mysqli_fetch_row($answer);
	
	if ($row[2] == "1") {
        header("Location: https://google.com");
    }
	
	$answer1 = mysqli_query($link, "SELECT * FROM races ORDER BY race_name");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="creator.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	<link rel="icon" href="icon.png" type="image/x-icon">
	<title>D&D - Профиль</title>
	<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
	
</head>
<body>
    <div class="head">
        <div class="temn1">
            <div class="topmenu">
                <a target="blank" href="https://discord.gg/MffG4XveVE"><button class="tbut">Наш Discord</button></a>
                <a href="download.php"><button class="tbut">Скачать D&D</button></a>
                <a href="about.php"><button class="tbut">О нас</button></a>
                <? if ($row) { ?>
                    <a href="profile.php"><div class="profile"></div></a>
                    <b class="nick"><? echo $row[0]; ?></b>
                <? }
                else { ?>
                    <a href="profile.php"><div class="profile"></div></a>
                    <a href="login.php"><button class="tbut login">Войти</button></a>
                <? } ?>
            </div>
            <? if (!($row)) { ?>
                <h1 class="font-effect-fire-animation txt zag1">Вы не вошли в аккаунт!</h1>
            <? }
            else { ?>
                <h2 class="font-effect-fire-animation txt">Создание персонажа</h2>
                <div class="creator_div">
                    <h3 class="font-effect-fire-animation txt header">Раса:</h3>
                    <div class="blocks">
                        <? while ($row1 = mysqli_fetch_row($answer1)) { ?>
                            <button class="block" raceName="<? echo $row1[1] ?>" subraces="<? echo $row1[11] ?>"><? echo $row1[1] ?></button>
                        <? } ?>
                    </div>
                </div>
            <? } ?>
        </div>
    </div>
    <div class="click_menu"></div>
    <div class="menu">
        <a href="history.php"><div class="menu_item"><img class="menu_item_img" src="history.png"><span class="menu_txt">История и события</span></div></a>
            
        <a href="spells.php"><div class="menu_item"><img class="menu_item_img" src="spells.png"><span class="menu_txt">Заклинания</span></div></a>
        <a href="items.php"><div class="menu_item"><img class="menu_item_img" src="magic_items.png"><span class="menu_txt">Артефакты</span></div></a>
        <a href="bestiarium.php"><div class="menu_item"><img class="menu_item_img" src="bestiarium.png"><span class="menu_txt">Бестиарий</span></div></a>
            
        <a href="languages.php"><div class="menu_item"><img class="menu_item_img" src="languages.png"><span class="menu_txt">Языки</span></div></a>
        <a href="posts.php"><div class="menu_item"><img class="menu_item_img" src="posts.png"><span class="menu_txt">Посты</span></div></a>
        <a href="chat.php"><div class="menu_item"><img class="menu_item_img" src="chat.png"><span class="menu_txt">Чат</span></div></a>
    </div>
	<script src="home.js" type="text/javascript"></script>
	<script src="creator.js" type="text/javascript"></script>
</body>
</html>