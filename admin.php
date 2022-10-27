<?
	$link = mysqli_connect("127.0.0.1", "u1162862_mosenka", "Qclash123!", "u1162862_database");
	mysqli_set_charset($link, "utf8");

	session_start();
	$id = session_id();
	
	$playerId = $_GET["id"];

	$answer = mysqli_query($link, "SELECT player_name, player_marker, player_banned FROM players WHERE player_session = '$id'");
	$row = mysqli_fetch_row($answer);
	
	if ($row[2] == "1") {
        header("Location: https://google.com");
    }
	
	$answer1 = mysqli_query($link, "SELECT * FROM players");
	
	if ($playerId) {
    	$answer4 = mysqli_query($link, "SELECT * FROM players WHERE player_id = $playerId");
    	$row4 = mysqli_fetch_row($answer4);
	}
	
	$answer99 = mysqli_query($link, "SELECT * FROM about");
	$row99 = mysqli_fetch_row($answer99);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="admin.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	<link rel="icon" href="icon.png" type="image/x-icon">
	<title>D&D - Панель администратора</title>
<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
	
</head>
<body>
    <? if ($playerId) { ?>
        <div class="pop-up">
            <a href="admin.php"><img class="close" src="exit.png"></a>
            <div class="player_div">
                <p class="txt"><? echo $row4[1]; ?></p><img class="edit_player_name" src="edit.png">
                <div class="new_player_name"><form><input class='inp new_player_name_inp' type='text' placeholder='Введите новое имя'><br><input playerId="<? echo $row4[0]; ?>" class='inp new_player_name_but' type='submit' value='Изменить'></form></div>
                <p class="txt"><? echo $row4[3]; ?></p><img class="edit_player_mail" src="edit.png">
                <div class="new_player_mail"><form><input class='inp1 new_player_mail_inp' type='text' placeholder='Введите новую почту'><br><input playerId="<? echo $row4[0]; ?>" class='inp1 new_player_mail_but' type='submit' value='Изменить'></form></div>
            </div>
        </div>
    <? } ?>
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
                <? if ($row[1] == "админ") { ?>
                    <h1 class="font-effect-fire-animation txt zag1">Dungeons & Dragons</h1>
                    <h2 class="font-effect-fire-animation txt">Страница администратора</h2>
                <? }
                else { ?>
                    <h1 class="font-effect-fire-animation txt zag1">Вы не админ :(</h1>
                <? } ?>
        </div>
    </div>
    <? if ($row[1] == "админ") { ?>
        <div class="white_list">
            <h2 class="font-effect-fire-animation txt zag1" style="margin-top: 50px;">Игроки</h2>
            <? while ($row1 = mysqli_fetch_row($answer1)) { ?>
                <div class="player_div">
                    <p class="txt"><? echo $row1[1]; ?></p>
                    <p class="txt"><? echo $row1[3]; ?></p>
                    <? $own_id = $row1[0];
                    $answer2 = mysqli_query($link, "SELECT character_name, character_surname FROM characters WHERE character_owner_id = $own_id"); ?>
                    <p class="txt">
                        Персонажи: 
                        <? while ($row2 = mysqli_fetch_row($answer2)) {
                            echo $row2[0] . " " . $row2[1] . "; ";
                        } ?>
                    </p>
                    <img class="ban" src="<? if ($row1[6] == 1) {echo "un";} ?>ban.png" playerId="<? echo $row1[0]; ?>" banned="<? echo $row1[6]; ?>">
                    <? if ($row1[6] == 0) { ?>
                        <span class="bt">забанить</span>
                    <? }
                    else { ?>
                        <span class="bt">разбанить</span>
                    <? } ?>
                    <a href="admin.php?id=<? echo $row1[0]; ?>"><img class="edit_popUp" src="edit.png"></a>
                </div>
            <? } ?>
        </div>
        <div class="report">
            <div class="temn1">
                <h2 class="font-effect-fire-animation txt">Редактировать "О нас"</h2>
                <form>
                    <textarea class="inp2 ta" placeholder="Напишите описание"><? echo $row99[1]; ?></textarea>
                    <input class="inp2 edit_info" type="submit" value="Изменить">
                </form>
            </div>
        </div>
    <? } ?>
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
</body>
</html>