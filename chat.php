<?
	$link = mysqli_connect("127.0.0.1", "u1162862_mosenka", "Qclash123!", "u1162862_database");
	mysqli_set_charset($link, "utf8");

	session_start();
	$id = session_id();
	
	$char = $_GET["char"];
    
	$answer = mysqli_query($link, "SELECT player_name, player_banned FROM players WHERE player_session = '$id'");
	$row = mysqli_fetch_row($answer);
	
	if ($row[1] == "1") {
        header("Location: https://google.com");
    }
	
	$answer1 = mysqli_query($link, "SELECT character_id FROM characters WHERE character_owner_id = (SELECT player_id FROM players WHERE player_session = '$id') ORDER BY character_id");
	$row1 = mysqli_fetch_row($answer1);
	
	$answer2 = mysqli_query($link, "SELECT * FROM characters WHERE character_owner_id = (SELECT player_id FROM players WHERE player_session = '$id')");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="chat.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	<link rel="icon" href="icon.png" type="image/x-icon">
	<title>D&D - Чат</title>
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
            <? if ($row) { ?>
                <? if ($char) { ?>
                    <? $row2 = mysqli_fetch_row($answer2);
                    $answer4 = mysqli_query($link, "SELECT character_region FROM characters WHERE character_id = $char");
                    $row4 = mysqli_fetch_row($answer4); ?>
                    <h1 class="zag1 font-effect-fire-animation">Чат местности: <? echo $row4[0]; ?></h1>
                    <div class="chat_div">
                        <? $region = $row2[5]; ?>
                        <div class="messages">
                        </div>
                        <div class="message">
                            <form>
                                <input class="inp mes" type="text" placeholder="Введите сообщение">
                                <input class="inp sub_mes" type="submit" value="Отправить">
                            </form>
                        </div>
                    </div>
                <? } 
                else { ?>
                    <h1 class="zag1 font-effect-fire-animation">Выбери персонажа</h1>
                    <? if ($row1) {
                        while ($row2 = mysqli_fetch_row($answer2)) { ?>
                            <a href="chat.php?char=<? echo $row2[0] ?>">
                                <div class="char_div">
                                    <p class="char_name">Имя: <? echo $row2[2] . " " . $row2[3] ?></p>
                                    <p class="char_race">Раса: <? echo $row2[4] ?></p>
                                    <p class="char_class">Класс: <? echo $row2[5] ?></p>
                                    <p class="char_level">Уровень: <? echo $row2[6] ?></p>
                                    <p class="char_region">Положение: <? echo $row2[10] ?></p>
                                </div>
                            </a>
                        <? }
                    }
                    else { ?>
                        <h3 class="font-effect-fire-animation txt">У вас пока нет персонажей :(</h3>
                    <? } ?>
                <? } ?>
            <? }
            else { ?>
                <h3 class="font-effect-fire-animation txt">Вы не вошли :(</h3>
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
    <script>
        function get_lol(name){
            const parts = window.location.href.split('?');
            if (parts.length > 1) {
                name = encodeURIComponent(name);
                const params = parts[1].split('&');
                const found = params.filter(el => (el.split('=')[0] === name) && el);
                if (found.length) return decodeURIComponent(found[0].split('=')[1]);
            }
        }
        setInterval(function(){
            $.ajax({
                type: "POST",
                url: 'ajax/chat.php',
                async: true,
                data: {
                    char: get_lol("char"),
                },
                success: function(response){
                    $(".messages").html(response)
                    $('.messages').animate({
                      scrollTop: document.getElementsByClassName("mess").length * 20
                    });
                }
            })
        }, 1000);
    </script>
	<script src="home.js" type="text/javascript"></script>
</body>
</html>