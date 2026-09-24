# -*- coding: utf-8 -*-
"""Edit specification per format, plus source-specific warnings.

Every post that reuses existing Drive footage gets a written edit brief, because
none of this footage was shot for the format it is now being used in.
"""

# Per format: (target length, the edit, the on-screen treatment, the audio)
EDIT_SPEC = {
 "The Course": (
   "25 to 35 seconds",
   "Treatment b-roll only. Most of this footage is silent, so the cut carries the story, not a voice. "
   "Open on the machine or the hands, never on a wide room shot. Keep the unglamorous frames: numbing cream, "
   "gel, goggles. Do not add a voiceover pretending to be the patient.",
   "SESSION N OF X and the real date, held on screen for the whole clip. That is the entire narrative device.",
   "Music bed only. If the source has usable room sound, keep it low under the bed."),

 "Skin School": (
   "5 slides",
   "Design only. Slide 1 is the claim, slides 2 to 4 carry the explanation, slide 5 is the CTA. "
   "One slide must contain the thing most people get wrong.",
   "Brand type only, readable at thumbnail size. Use the Dr. Uzair stills for any authority frame.",
   "n/a"),

 "The Menu": (
   "5 to 7 slides",
   "Design only. One treatment per slide, compared on the same axes so they can be read against each other. "
   "Never more than one idea per slide.",
   "Treatment names exactly as branded: Venus Glow, Venus Viva, Venus Legacy, Venus Fat Freeze.",
   "n/a"),

 "New at Venus": (
   "20 to 35 seconds, or 5 slides",
   "For a treatment with no footage this is a shoot. Film the machine, the room and the practitioner's hands. "
   "No patient face is needed for a first introduction.",
   "Treatment name and what it treats, on screen in the first 3 seconds.",
   "Clean voiceover or subtitled practitioner audio."),

 "Men of Venus": (
   "20 to 30 seconds",
   "Shot and cut for men. No soft focus, no floral transitions, no pastel grade. Keep it plain and direct.",
   "Male slot availability on the end frame.",
   "Music bed. Voiceover only if male."),

 "The Offer Free Consultation": (
   "Static",
   "Design only. This is a standing service, not a promotion, so it carries no deadline, no percentage and no urgency strip.",
   "What the consultation includes and that it costs nothing.",
   "n/a"),

 "The Result": (
   "Static",
   "Design only. Award or milestone treated as news.",
   "The verified number only. 9,861 Google reviews, never 10,000+ until it genuinely crosses.",
   "n/a"),

 "Case File": (
   "35 to 50 seconds",
   "Lead with the patient speaking. Cut the clinic b-roll to under a third of the runtime. "
   "Open on her face and her voice, not on the machine. Trim any part where a staff member speaks over her.",
   "Title card on frame 1: CASE FILE 0X / NAME / BEAT N. Visit number and real date bottom left, held for the whole clip. "
   "Burned-in English subtitles, because most of this plays on mute.",
   "Patient audio is the track. No music bed over her voice, light bed only under b-roll."),

 "The One Liner": (
   "7 to 10 seconds, hard cap",
   "One continuous shot if possible. No cuts to the machine, no cuts to reception. Cut on the beat.",
   "One line of text, large, centred, held the whole clip. Treatment name in the bottom corner. Nothing else.",
   "Trending audio only. No voiceover at all."),

 "Really Feels Like": (
   "25 to 40 seconds",
   "Sensory close-ups. Hands, cooling head, the patient's face reacting. "
   "Keep the unflattering frames, including the numbing cream and any wincing. Those frames are the point.",
   "Text describes the sensation, not the benefit. Minute markers if the treatment has stages.",
   "Patient or practitioner voice describing feel. If neither exists in the source, record a voiceover to the cut."),

 "The Machine": (
   "20 to 35 seconds",
   "Machine hero shots, screen UI, applicator moving. Open on the machine, not on a face.",
   "Machine name locked on screen for the first 3 seconds and again at the end. Specs as text if the source has none.",
   "Clean voiceover or subtitled expert audio. Music bed under."),

 "Ask the Room": (
   "30 to 45 seconds",
   "Single angle, seated, no cutaways. Trim all preamble so the answer starts inside 2 seconds.",
   "Practitioner NAME and ROLE on screen for the first 4 seconds. Question as a title card before the answer.",
   "Their voice clean. No music under speech."),

 "In Real Life": (
   "20 to 30 seconds",
   "Cut against the caption, not the treatment. The treatment is one shot in a sequence about a day.",
   "Minimal text. Let the caption do the work.",
   "Trending or warm music bed. Voiceover optional."),

 "Side by Side": (
   "15 to 25 seconds, or a static",
   "Same crop, same distance, same light on both frames. If the source lighting differs, say so on screen rather than colour matching it away.",
   "Dates and session count on both sides. Non-negotiable.",
   "Music bed only, or the client's own audio if it exists."),

 "Is This You": (
   "5 slides",
   "Design only. Slide 1 is the hook, slides 2 to 4 carry the checklist, slide 5 is the CTA. "
   "One slide must say who the treatment is NOT for.",
   "Brand type only. Readable at thumbnail size.",
   "n/a"),

 "The Room": (
   "40 to 60 seconds",
   "One continuous handheld walk if possible. Filmed at a busy hour, never an empty morning.",
   "Branch name and address on the last 3 seconds. Google review count if it is strong.",
   "Ambient room sound kept in, music bed under."),

 "Off Duty": (
   "8 to 20 seconds",
   "Do not over-edit. Vertical, phone-shot, unpolished is correct for this slot. Cut only to tighten the joke.",
   "Minimal or no text. If a caption carries the joke, leave the frame clean.",
   "Trending audio."),
}

# Source-specific warnings, keyed by a fragment of the asset path.
SOURCE_NOTES = [
 ("Sir Uzair Info Videos",
  "SOURCE MISMATCH TO HANDLE: this file is a doctor explainer, filmed as a talking head. "
  "It is being used here for a treatment-led slot, so cut Dr. Uzair to audio only over machine b-roll, "
  "or hold him on screen for no more than the first 3 seconds. The post is about the machine, not the doctor."),
 ("_Subtitling",
  "This file already carries burned-in subtitles. Do not add a second subtitle track. "
  "If the existing subtitle style clashes with the new title cards, use the matching file from the non-subtitled folder instead."),
 ("Sale CountDown",
  "DO NOT USE for this calendar. Countdown files are promotional and this calendar carries no discount posts. "
  "Listed only so the editor recognises the folder and skips it."),
 ("Engaging Content",
  "Shot loose and unpolished. Resist the urge to grade or stabilise it. The rough look is why these posts outperform."),
 ("Visit_0",
  "Part of a multi-visit sequence. Check the other visit folders for the same patient before cutting, "
  "so the framing and wardrobe stay consistent across beats."),
 ("interview segment",
  "Only the interview portion of this file is needed. The treatment footage in the same file belongs to a different beat."),
 ("Palvasha_HydraFacial",
  "This file has no extension in Drive. Confirm it plays before scheduling it."),
]

def spec_for(show):
    return EDIT_SPEC.get(show)

def notes_for(asset):
    out = []
    for frag, note in SOURCE_NOTES:
        if frag.lower() in asset.lower():
            out.append(note)
    return out
