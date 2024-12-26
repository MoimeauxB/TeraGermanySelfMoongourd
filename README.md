# TeraGermanySelfMoongourd
A little program that read HPM for a player and grades him as well as giving him details on unchained skills and skills he neglected or used too much

## how to use

double click the .exe, this will open a window 
if this is your 1st time launching this it will ask you to create a config file, this config file is needed to locate where's the shinra's export location on your computer.

once you've made the config file you'll see a list of dungeon followed by number
enter the corresponding number to see the list of every run you exported in that dungeon.
then type the number corresponding to the run you wanna get more infos on.

You'll see the fight duration, the other players in the party and your cumulative grade with each spells that hit, then the rank and total grade and depending on your class more infos as well as the list of your unchained hits. You will also have a newly created file called Fight_data.html

in this file you'll get more info on what you did, what was expected, etc...

## FAQ
### What os should I have
It has been compiled from a windows 10.

### why can't I see the data for other players?
Because I don't want anyone to use this to be toxic, this is also the reason why I have compiled this into an executable from python rather than just making the one python file visible on github.

### I did less dmg but got a better grade, your program sucks
There's a lot of things going into a fight, your dps is a factor of your healer and tank buffs/debuff, the enrage uptime, the random crit etc. sometime you'll play better but you wont get dps for it, that's sad but that's life.

### I have the same gear and grade on two classes but one of them deals a lot more !
It's called game balence. The best slayer of the world will not deal as much as a good valk on this patch. Althou I think the metric for the grade is not perfect (about 3% off) I think it reflects pretty accuratly the skill level of someone and a 100% on every dps should yeild around the same dps in a balenced world.

### What are the grade meaning anyway?
below 10% you're not playing the game and I can't grade that <br>
10 <  f < 20: you're totally lost and dont know what to do <br>
20 <= e < 35: you understood you have to use spells, but you dont know which ones<br>
35 <= d < 55: you get the gist of the class but you're bad at it <br>
55 <= c < 70: you understand the basis but you're still a little lost<br>
70 <= b < 80: you know what to do but still have brainfarts<br>
80 <= a < 95: you know your way around<br>
95 <= s  < 105: you're playing well <br>
105 < Lolimagie you're among the best players <br>

note that the grade means anything only for fight that last at least 1min30 as it is the timing to reburst for most classes.
if you want to be considered 'good' you need to at least be A rank on every deathless fight.

### I am a healer, why this dosen't work?
Healers should never focus on dealing more dmg with their spells as buffing 4 players should always be worth more than using a spell on a boss. Since the shinra's export does not record the buffs and debuff you gave this program simply do not work for healers

### I am a brawler, why this dosen't work?
While brawlers unlike healers should aim for the best dps possible the very core mechanic of the classe makes their hpm loose a lot of meaning. Their hpm will heavely depend on the boss rng as the reflected dmg from rising fury will count toward the hpm of whatever spell triggered it. while I could have done it for dps brawler as they do not reflect dmg, they are litterally none on the server.

Also it's against my religion to help brawlers.

### I am stuck at a rank and I don't know what I am doing wrong
Sometime when you don't get something on your class watching your hpm and tips wont be enough, in that case feel free to dm me, I usually answer in less than 24hours.
