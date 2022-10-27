<?
	$link = mysqli_connect("127.0.0.1", "u1162862_mosenka", "Qclash123!", "u1162862_database");
	mysqli_set_charset($link, "utf8");

	session_start();
	$id = session_id();

	$answer = mysqli_query($link, "SELECT player_name, player_banned FROM players WHERE player_session = '$id'");
	$row = mysqli_fetch_row($answer);
    
    if ($row[1] == "1") {
        header("Location: https://google.com");
    }
    
    $answer1 = mysqli_query($link, "SELECT info FROM about");
	$row1 = mysqli_fetch_row($answer1);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="about.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	<link rel="icon" href="icon.png" type="image/x-icon">
	<title>D&D - О нас</title>
	<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
	
</head>
<body>
    <div class="head">
        <div class="temn1">
            <div class="topmenu">
                <a target="blank" href="https://discord.gg/MffG4XveVE"><button class="tbut">Наш Discord</button></a>
                <a href="download.php"><button class="tbut">Скачать D&D</button></a>
                <a href="about.php"><button class="tbut">О нас</button></a>
                <div class="workers">
                    <span class="txt7">Команда</span>
                    <a class="a" href="https://e.mail.ru/compose?To=adsizov09@mail.ru"><button class="m_but">ДМ</button></a>
                    <a class="a" href="https://e.mail.ru/compose?To=miroslavgaraev@gmail.com"><button class="m_but">Помощник в CC</button></a>
                    <a class="a" href="https://e.mail.ru/compose?To=bidigyan@gmail.com"><button class="m_but">Композитор</button></a>
                    <a class="a" href="https://e.mail.ru/compose?To=vlad.cher279@gmail.com"><button class="m_but">База данных</button></a>
                    <a class="a" href="https://e.mail.ru/compose?To=lad.cher279@gmail.com"><button class="m_but">Художник</button></a>
                </div>
                <? if ($row) { ?>
                    <a href="profile.php"><div class="profile"></div></a>
                    <b class="nick"><? echo $row[0]; ?></b>
                <? }
                else { ?>
                    <a href="profile.php"><div class="profile"></div></a>
                    <a href="login.php"><button class="tbut login">Войти</button></a>
                <? } ?>
            </div>
            <h1 class="font-effect-fire-animation txt zag1">Dungeons & Dragons</h1>
            <h2 class="font-effect-fire-animation txt">О нас</h2>
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
    <div class="white_list">
        <h2 class="font-effect-fire-animation txt">Инфо</h2>
        <div class="opis"><? echo $row1[0]; ?></div>
        <div class="slider">
            <div class="slide slide1"></div>
            <div class="slide slide2"></div>
            <div class="slide slide3"></div>
        </div>
        <div class="dots">
            <div class="dot dot1"></div>
            <div class="dot dot2"></div>
            <div class="dot dot3"></div>
        </div>
    </div>
    <div class="report">
        <div class="temn1" style="height: 90vh; padding-top: 10vh;">
            <h2 class="font-effect-fire-animation txt">Написать в поддержку</h2>
            <form>
                <input class="inp nick" type="text" placeholder="Твой ник">
                <input class="inp email" type="email" placeholder="Ваша почта">
                <textarea class="inp ta" placeholder="Текст"></textarea>
                <input class="inp texpod" type="submit" value="Отправить">
            </form>
        </div>
    </div>
    <div class="podval">
        <div class="pod_div">
            <p class="pod_h font-effect-fire-animation">Программисты</p>
            <a class="pod_a" href="https://e.mail.ru/compose?To=adsizov09@mail.ru">ДМ</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=miroslavgaraev@gmail.com">Помощник в CC</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=bidigyan@gmail.com">2-й помощник</a>
        </div>
        <div class="pod_div">
            <p class="pod_h font-effect-fire-animation">Музыкальное сопровождение</p>
            <a class="pod_a" href="https://e.mail.ru/compose?To=bidigyan@gmail.com">Композитор</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=adsizov09@mail.ru">ДМ</a><br>
        </div>
        <div class="pod_div">
            <p class="pod_h font-effect-fire-animation">Картинки</p>
            <a class="pod_a" href="https://e.mail.ru/compose?To=vlad.cher279@gmail.com">Художник</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=adsizov09@mail.ru">ДМ</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=vlad.cher279@gmail.com">База данных</a>
        </div>
        <div class="pod_div">
            <p class="pod_h font-effect-fire-animation">НИПы</p>
            <a class="pod_a" href="https://e.mail.ru/compose?To=adsizov09@mail.ru">ДМ</a><br>
            <a class="pod_a" href="https://e.mail.ru/compose?To=miroslavgaraev@gmail.com">Помощник в CC</a>
            <a class="pod_a" href="https://e.mail.ru/compose?To=bidigyan@gmail.com">Проектировщик</a>
        </div>
    </div>
	<script src="home.js" type="text/javascript"></script>
</body>
</html>