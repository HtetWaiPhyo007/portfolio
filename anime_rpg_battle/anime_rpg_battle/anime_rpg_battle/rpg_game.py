import random
import os
import time
import pygame

# Initialize sound system
pygame.mixer.init()

# Character stats and voices
characters = {
    "Naruto": {
        "hp": 110, "atk": 30, "def": 12, "skill": "Rasengan Strike",
        "voice_special": "voices/naruto(special attack).mp3",
        "voice_double": "voices/naruto(special double).mp3"
    },
    "Luffy": {
        "hp": 130, "atk": 28, "def": 10, "skill": "Gum-Gum Pistol",
        "voice_special": "voices/luffy(special attack).mp3",
        "voice_double": "voices/luffy(special double).mp3"
    },
    "Mikasa": {
        "hp": 90, "atk": 30, "def": 12, "skill": "Blade Barrage",
        "voice_special": "voices/mikasa(special attack).mp3",
        "voice_double": "voices/mikasa(special double).mp3"
    },
    "Kaneki": {
        "hp": 110, "atk": 28, "def": 9, "skill": "Rinkaku Strike",
        "voice_special": "voices/kaneki_special_attack.mp3",
        "voice_double": "voices/kaneki_special_double.mp3"
    },
    "Makima": {
        "hp": 105, "atk": 26, "def": 11, "skill": "Control Curse",
        "voice_special": "voices/makima(special attack).mp3",
        "voice_double": "voices/makima(special double).mp3"
    },
    "Kurosaki": {
        "hp": 100, "atk": 27, "def": 10, "skill": "Getsuga Slash",
        "voice_special": "voices/kurosaki(special attack).mp3",
        "voice_double": "voices/kurosaki(special double).mp3"
    },
    "Asta": {
        "hp": 120, "atk": 32, "def": 8, "skill": "Black Divider",
        "voice_special": "voices/asta(special attack).mp3",
        "voice_double": "voices/asta(special double).mp3"
    }
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def play_voice(path):
    try:
        # Add project path correctly
        base_path = os.path.dirname(__file__)  # Folder where your code is
        full_path = os.path.join(base_path, path)

        print(f"🔊 Trying to play: {full_path}")  # Debugging info

        if not os.path.exists(full_path):
            print(f"❌ (Voice file not found: {full_path})")
            return

        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"🎵 Error playing sound: {e}")

def naruto_animation():
    frames = [
        "    🌀      ",
        "  🌀💨🌀    ",
        "🌀💨🙎‍♂️💨🌀  ",
        "  🌀💨🌀    ",
        "    🌀      ",
    ]
    for frame in frames:
        clear()
        print("🌀 Naruto's Rasengan Strike! 🌀")
        print(frame)
        time.sleep(0.2)

def luffy_animation():
    frames = [
        "    👊      ",
        "  👊💥👊    ",
        "👊💥💥💥👊  ",
        "  👊💥👊    ",
        "    👊      ",
    ]
    for frame in frames:
        clear()
        print("👊 Luffy's Gomu Gomu Punch! 👊")
        print(frame)
        time.sleep(0.2)


def mikasa_animation():
    frames = [
        "     ⚡        ",
        "   ⚡⚡⚡      ",
        " ⚡⚡💥⚡⚡    ",
        "   ⚡⚡⚡      ",
        "     ⚡        ",
    ]
    for frame in frames:
        clear()
        print("⚡ Mikasa's Lightning Slash! ⚡")
        print(frame)
        time.sleep(0.2)

def makima_animation():
    frames = [
        "    🌀        ",
        "  🌀🌀🌀      ",
        "🌀🔮🌀🔮🌀   ",
        "  🌀🌀🌀      ",
        "    🌀        ",
    ]
    for frame in frames:
        clear()
        print("🔮 Makima's Curse Control! 🔮")
        print(frame)
        time.sleep(0.2)

def kaneki_animation():
    frames = [
        "    🌑        ",
        "  🌑🌑🌑      ",
        "🌑💀🌑💀🌑   ",
        "  🌑🌑🌑      ",
        "    🌑        ",
    ]
    for frame in frames:
        clear()
        print("🌑 Kaneki's Ghoul Burst! 🌑")
        print(frame)
        time.sleep(0.2)

def kurosaki_animation():
    frames = [
        "    ⚫⚪        ",
        "  ⚫⚫⚪⚪      ",
        "⚪💥⚫💥⚪   ",
        "  ⚪⚫⚪⚫      ",
        "    ⚫⚪        ",
    ]
    for frame in frames:
        clear()
        print("☯️ Kurosaki's Shadow & Light! ☯️")
        print(frame)
        time.sleep(0.2)

def asta_animation():
    frames = [
        "    ⚔️      ",
        "  ⚔️🌑⚔️    ",
        "⚔️🌑🖤🌑⚔️ ",
        "  ⚔️🌑⚔️    ",
        "    ⚔️      ",
    ]
    for frame in frames:
        clear()
        print("⚔️ Asta's Black Slash! ⚔️")
        print(frame)
        time.sleep(0.2)

def play_animation(name):
    if name == "Naruto":
        naruto_animation()
    elif name == "Luffy":
        luffy_animation()
    elif name == "Mikasa":
        mikasa_animation()
    elif name == "Makima":
        makima_animation()
    elif name == "Kaneki":
        kaneki_animation()
    elif name == "Kurosaki":
        kurosaki_animation()
    elif name == "Asta":
        asta_animation()

from PIL import Image

def choose_character():
    clear()
    print("👑 Choose your fighter!\n")
    for i, name in enumerate(characters.keys(), 1):
        print(f"{i}. {name} - {characters[name]['skill']} (HP:{characters[name]['hp']}, ATK:{characters[name]['atk']}, DEF:{characters[name]['def']})")
    choice = int(input("\nEnter number of your character: "))
    player_name = list(characters.keys())[choice - 1]
    return player_name, characters[player_name].copy()

def enemy_select(player_name):
    enemy_pool = [name for name in characters.keys() if name != player_name]
    enemy_name = random.choice(enemy_pool)
    return enemy_name, characters[enemy_name].copy()

def attack(attacker, defender, is_skill=False, double=False):
    base = attacker['atk']
    if is_skill:
        print(f"✨ {attacker['skill']} activated!")
    if double:
        base *= 2
    damage = max(0, base - defender['def'] + random.randint(-3, 5))
    defender['hp'] -= damage
    return damage

def show_status(p_name, p_stats, e_name, e_stats):
    print("\n📊 Battle Status:")
    print(f"🧑 {p_name} - HP: {p_stats['hp']}")
    print(f"👹 {e_name} - HP: {e_stats['hp']}")

def main():
    clear()
    print("🎮 Welcome to Anime RPG: Terminal Edition!\n")
    player_name, player = choose_character()
    enemy_name, enemy = enemy_select(player_name)

    print(f"\n🆚 You ({player_name}) vs Enemy ({enemy_name})")
    input("Press Enter to begin battle...")

    turn_count = 0
    enemy_turn_count = 0
    delayed_special = False

    while player['hp'] > 0 and enemy['hp'] > 0:
        clear()
        show_status(player_name, player, enemy_name, enemy)

        print("\n🎲 Rolling dice to decide turn...")
        time.sleep(1)
        turn = random.choice([player_name, enemy_name])
        print(f"🎲 Dice chose: {turn}")

        # PLAYER TURN
        if  turn == player_name:
            turn_count += 1
            print(f"\n💥 {player_name}'s Turn")

            # Auto Special Trigger
            if delayed_special:
               
                play_animation(player_name)
                
                print("💥 Auto Special Triggered (Double Damage!)")
                damage = attack(player, enemy, is_skill=True, double=True)
                print(f"🔥 {player_name} dealt {damage} to {enemy_name} with double special!")
                play_voice(player["voice_double"])

                delayed_special = False
                turn_count = 0

                if enemy['hp'] <= 0:
                    print(f"\n🏆 You defeated {enemy_name}!")
                    print("🎉 YOU WIN!")
                    return

                input("\nPress Enter to roll again...")
                continue

            if turn_count >= 3:
                print("🟡 Special attack is charged!")
                print("1. Normal Attack (next turn = auto special)")
                print("2. Special Attack now")
                move = input("Choose (1 or 2): ")

                if move == "1":
                    damage = attack(player, enemy)
                    print(f"🗡️ {player_name} dealt {damage} to {enemy_name}!")
                    delayed_special = True
                    turn_count = 0
                elif move == "2":
                    play_animation(player_name)
                    
                     

                    
                
                    damage = attack(player, enemy, is_skill=True)
                    print(f"⚡ {player_name} used {player['skill']} and dealt {damage}!")
                    play_voice(player["voice_special"])
                    delayed_special = False
                    turn_count = 0
                else:
                    print("Invalid input. Defaulting to normal attack.")
                    damage = attack(player, enemy)
                    print(f"🗡️ {player_name} dealt {damage} to {enemy_name}!")
                    delayed_special = True
                    turn_count = 0
            else:
                print("🗡️ Normal attack!")
                damage = attack(player, enemy)
                print(f"🎯 {player_name} dealt {damage} to {enemy_name}!")

        # ENEMY TURN
        else:
            enemy_turn_count += 1
            print(f"\n👿 {enemy_name}'s Turn")

            if delayed_special:
                print("❌ You missed your chance to use delayed special.")
                delayed_special = False

            if enemy_turn_count >= 3:
                play_animation(enemy_name)
            
                
                
                damage = attack(enemy, player, is_skill=True)
                print(f"⚡ {enemy_name} used {enemy['skill']} and dealt {damage}!")
                play_voice(enemy["voice_special"])

                enemy_turn_count = 0
            else:
                damage = attack(enemy, player)
                print(f"👊 {enemy_name} dealt {damage} to {player_name}!")

        # WIN/LOSE CHECK
        if player['hp'] <= 0:
            print(f"\n💀 You were defeated by {enemy_name}...")
            print("🎯 YOU LOSE!")
            return
        elif enemy['hp'] <= 0:
            print(f"\n🏆 You defeated {enemy_name}!")
            print("🎉 YOU WIN!")
            return

        input("\nPress Enter to roll again...")

# MAIN LOOP
if __name__ == "__main__":
    while True:
        main()
        choice = input("🔁 Play again? (y/n): ").lower()
        if choice != "y":
            print("👋 Thanks for playing!")
            break
        
