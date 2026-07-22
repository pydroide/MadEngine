# External modules
import os
import random

# Text alignment logic
align = os.get_terminal_size().columns

# Screen clear function (Pro Version)
def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")
   print("\033[2J\033[H", end="", flush=True)

# Colour variables (Fixed)
bg_red = "\033[41m\033[97m" # Red Background + White Text (Titles/Borders ke liye)
red = "\033[91m"            # Normal Red Text (Warnings/Errors ke liye)
green = "\033[92m"          # Green Text (Inputs/Success ke liye)
reset = "\033[0m"

# Default borders displayed
w_bord = "/// MadEngine ///"
c_bord = "/// TERMINATED ///"
h_bord = "/// HISTORY ///"

# Game ki memory (List)
history_list = []

# Main Game Loop
while True:
   clear_screen()
   
   # Welcome border display
   print(f"{bg_red}{w_bord:^{align}}{reset}")

   # MadEngine interface UI/UX
   khoobi = input(f"\n  //{green}Chalak, mota, darpok\n  gussewala, bhukkad, natkhat{reset}//\n  {reset}Choose one: ")
   print(f"  {green}You typed: {khoobi}{reset}\n")
   
   name = input(f"  //{green}Raju, bandar, bhoot,\n  padosi, neta, chudail {reset}//\n  {reset}Choose one: ")
   print(f"  {green}You typed: {name}{reset}\n")
   
   jagah = input(f"  //{green}Mela, school, chhat,\n  kabaadkhana, samundar, jungle {reset}//\n  {reset}Choose one: ")
   print(f"  {green}You typed: {jagah}{reset}\n")
   
   kaam = input(f"  //{green}Bhagna, rona, khana,\n  naachna, girna, chillana {reset}//\n  {reset}Choose one: ")
   print(f"  {green}You typed: {kaam}{reset}\n")

   # Final story options      
   story = [
    f" Ek din, ek bohot {khoobi}\n  {name} {jagah} mein gaya. Wahan\n  jaate hi wo zor-zor\n  se {kaam} laga.",
    
    f" Kya aapko pata hai? {jagah}\n  ka sabse bada rahasya ek\n  {khoobi} {name} hai, jise raat\n  ko {kaam} bohot pasand hai!",
    
    f" Jab main {jagah} pahuncha, maine\n  dekha ki ek {name} bilkul\n  {khoobi} tarike se {kaam} raha\n  tha. Ye bohot ajeeb tha!"
   ]

   # Select random story and print
   final_story = random.choice(story)
   print(f"  {bg_red} FINAL STORY {reset}")
   print(f"  {green}{final_story}{reset}\n")
   
   # 1. Kahani ko program ki memory (list) mein save karna
   history_list.append(final_story)
   
   # 2. Kahani ko hamesha ke liye '.txt' file mein save (append) karna
   with open("madEngineHistory.txt", "a") as file:
       file.write(f"{final_story}\n")
       file.write("----------------------------\n")
   
   # --- Strict End Menu Loop ---
   while True:
       # Gamer Style UI Menu
       close_game = input(f"  [Enter] Play | {bg_red}[h]{reset} History | {bg_red}[c]{reset} Clear | {bg_red}[q]{reset} Exit : ").strip().lower()
       
       if close_game == "q":
          clear_screen()
          print(f"{bg_red}{c_bord:^{align}}{reset}") 
          exit() 
          
       elif close_game == "":
          break # Andar wale loop ko todega aur naya round shuru karega
          
       # History Menu
       elif close_game == "h":
          clear_screen()
          print(f"{bg_red}{h_bord:^{align}}{reset}\n") 
          
          if len(history_list) == 0:
              print(f"  {bg_red}History khali hai! Koi kahani save nahi hui.{reset}\n")
          else:
              for index, purani_story in enumerate(history_list, 1):
                  print(f"  {bg_red}--- Story {index} ---{reset}")
                  print(f"  {green}{purani_story}{reset}\n")
              
          input(f"  {bg_red}Press enter to go back...{reset}")
          
          # Wapas aane par screen blank na dikhe, isliye Title aur Story dobara print kar rahe hain
          clear_screen()
          print(f"{bg_red}{w_bord:^{align}}{reset}\n")
          print(f"  {bg_red} FINAL STORY {reset}")
          print(f"  {green}{final_story}{reset}\n")
          
       # Clear History Menu
       elif close_game == "c":
          history_list.clear() # Memory se clear
          with open("madEngineHistory.txt", "w") as file:
              pass # Text file se clear
              
          clear_screen()
          print(f"\n  {bg_red}/// HISTORY CLEARED ///{reset}\n")
          print(f"  {green}Saari purani kahaniyan hamesha ke liye delete ho gayi hain!{reset}\n")
          input(f"  {bg_red}Press enter to go back...{reset}")
          
          # Wapas aane par UI refresh
          clear_screen()
          print(f"{bg_red}{w_bord:^{align}}{reset}\n")
          print(f"  {bg_red} FINAL STORY {reset}")
          print(f"  {green}{final_story}{reset}\n")
          
       else:
          # Agar user galat button dabaye
          print(f"  {red}Use [Enter], [h] [c], or [q]{reset}\n")
