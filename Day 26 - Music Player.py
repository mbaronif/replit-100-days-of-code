import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
      stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu: "))
      if stop_playback == 2:
          pause()
          return # let's go back from this play() subroutine
      else:
          continue

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print()
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print()
  print("Press anything else to see the menu again.")
  print()
  # take user's input
  userOption = int(input("Please, choose an option: "))
  # check whether you should call the play() subroutine depending on user's input
  if userOption == 1:
      print("Let's the party start!")
      play()
  elif userOption == 2:
      exit()
  else:
      continue
