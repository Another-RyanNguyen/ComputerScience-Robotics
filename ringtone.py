#		python code
#		script_name: MUSIC CODE RINGTONE
#
#		author: Ryan Nguyen
#		description: Making a Ringtone using code. 
#

from earsketch import *

init()
setTempo(120)

def beatMaker(music, track, beat, start, end):
    for measure in range(start, end):
        makeBeat(music, track, measure, beat)

start1stVerse = 1
end1stVerse = 3
startTransition = 3
endTransition = 5

for i in range(1, 9):
  #Verse 
  Lead = RD_UK_HOUSE__FMBASS_1
  Beat1 = COMMON_LOVE_DRUMBEAT_1
  Beat2 = EIGHT_BIT_ANALOG_DRUM_LOOP_001
  
  fitMedia(Lead, 1, start1stVerse, end1stVerse)
  fitMedia(Beat1, 2, start1stVerse, end1stVerse)
  fitMedia(Beat2, 3, start1stVerse, end1stVerse)
  beatMaker(CIARA_SET_KICK_1, 4, "----0+-00---00+0", start1stVerse, end1stVerse)
  effectStart = 1
  effectEnd = 2
  for measure1 in range(1, end1stVerse):
    setEffect(4, VOLUME, GAIN, -60, effectStart, 5, effectEnd)
    effectStart += 1
    effectEnd += 1

  #Transition 
  fitMedia(Lead, 1, startTransition, endTransition)
  startTransition += 1
  fitMedia(RD_ELECTRO_SFX_RINGMODRISER_1, 3, startTransition, endTransition)
  beatMaker(CIARA_SET_KICK_1, 2, "-----------00+0+", startTransition, endTransition)
  startTransition -= 1
  
  start1stVerse += 4
  end1stVerse += 4
  startTransition += 4
  endTransition += 4
  




finish()
