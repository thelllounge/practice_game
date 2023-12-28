import character
import chapter0

player = character.Start()
player.get_weapon("sword")

chapter0 = chapter0.ChapterZero()
chapter0.wakeUp(player)

print("GAME OVER!")