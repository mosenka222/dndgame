let stage = 0;
let playerId = 0;
$.ajax({
    type: "POST",
    url: 'ajax/getid.php',
    success: function(response){
        playerId = response;
    }
});
let nc;
setTimeout(function(){
    nc = {
        character_owner_id: playerId,
        character_name: "",
        character_surname: "",
        character_race: "",
        character_class: "",
        character_level: "1",
        character_characteristics: "",
        character_saving_throws: "",
        character_hit_dice: "",
        character_heal_dices: "",
        character_max_hits: "",
        character_time_hits: "",
        character_armor: "",
        character_weapons: "",
        character_tools: "",
        character_skills: "",
        character_proficiency_bonus: "",
        character_speed: "",
        character_money: "",
        character_inventory: "",
        character_background: "",
        character_abilities: "",
        character_armor_class: "",
        character_xp: "",
        character_dead_st: "",
        character_sprite: "",
        character_region: ""
    };
}, 1000);


$(".block").click(function(){
    nc["character_race"] = $(this).attr("raceName");
    stage = "1";
    if ($(this).attr("subraces") == "да") {
        console.log("ploxo")
    }
    else {
        $(".header").html("Класс:")
        $.ajax({
            type: "POST",
            url: 'ajax/getclasses.php',
            success: function(response){
                $(".blocks").html(response);
                
                $(".blockCl").click(function(){
                    nc["character_class"] = $(this).attr("className");
                    $(".header").html("Характеристики:")
                    stage = "2";
                    
                    $(".blocks").html(
                        "Осталось <span class='points'>27</span> очков<br>" +
                        "<div>Сила <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button><button class='butt1'>-</button></div>" +
                        "<div>Ловкость <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button><button class='butt1'>-</button></div>" +
                        "<div>Телосложение <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button><button class='butt1'>-</button></div>" +
                        "<div>Интелект <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button><button class='butt1'>-</button></div>" +
                        "<div>Мудрость <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button'><button class='butt1'>-</button></div>" +
                        "<div>Харизма <span class='c_count'>8</span> <button class='butt' style='clear: both;'>+</button><button class='butt1'>-</button></div>"
                    );
                    
                    pb_chars = [8, 9, 10, 11, 12, 13, 14, 15];
                    pb_cost = [0, 1, 2, 3, 4, 5, 7, 9];
                    points = 27;
                    
                    $(".butt").click(function(){
                        num = parseInt($(this)[0].parentNode.children[0].innerHTML);
                        try {
                            if (points - (pb_cost[pb_chars.indexOf(num + 1)] - pb_cost[pb_chars.indexOf(num)]) >= 0 && num + 1 < 16) {
                                $(this)[0].parentNode.children[0].innerHTML = num + 1;
                                num = parseInt($(this)[0].parentNode.children[0].innerHTML);
                                points -= pb_cost[pb_chars.indexOf(num)] - pb_cost[pb_chars.indexOf(num - 1)];
                                $(".points").html(points);
                            }
                        } catch (e) {}
                    });
                    $(".butt1").click(function(){
                        num = parseInt($(this)[0].parentNode.children[0].innerHTML);
                        if (num - 1 >= 8) {
                            $(this)[0].parentNode.children[0].innerHTML = num - 1;
                            num = parseInt($(this)[0].parentNode.children[0].innerHTML);
                            if (num == 8) {
                                points += 1;
                            }
                            else {
                                points += pb_cost[pb_chars.indexOf(num + 1)] - pb_cost[pb_chars.indexOf(num)];
                            }
                        }
                    });
                });
            }
        });
    }
});
