# Notation
Groover is intended to enable simple notation of drum set grooves. Each mode has its advantages. There are two ways to input text in Groover: *Disparate Mode* and *Chord Mode*.

## Simple Mode 
In disparate mode, you enter the rhythm for each instrument in your groove *individually*. This means that if your groove uses hi-hat, snare drum, and kick, you'll be asked to enter a line of text for each of these individually (that is, 3 separate lines of text).

This mode may be a good choice, for example, when you are transcribing a groove, and you find it easier to dissect it piece-by-piece (instrument by instrument). On the other hand, it may be a bad choice when you are using at least 1 part of the drum set very sparingly. In this case, you'll be asked to enter the entire rhythm for this part of the drum set, even if it gets used only once every several measures. Finally, the syntax in this mode is incredibly simple to master.

### Syntax
A lowercase *x* represents the presence of a note at the location it's entered, and a *space* character represents the lack of a note at this location (a rest).

### Examples
**TODO: show sheet music examples along with what the input would look like to create it**

## Chord Mode
TODO: come up with better name for this mode
In chord mode, you group pieces of the drumset together when they are to be played together. This means that when the snare, hi-hat, and kick are all meant to be played at the exact same time, then you'd notate this as "skb" (see the section on syntax below). Because there are no spaces between these letters, the system knows that these notes are all meant to be played together.

### Syntax
The syntax for chord mode is more complicated than it is in disparate mode, but this complexity allows for more flexibility. Much of this flexibility is not yet utilized, but will be in the future (think concise ways to notate accents, dynamics, etc.). Each part of the drumset has its own letter, much like it does on the musical staff. It's important to note that these letter are *case sensitive*. This means that **"a"** and **"A"** are *not* the same thing.

Here's a map from character to instrument:
TODO: this is a work in progress
*h* - hi-hat
*c* - crash cymbal 1
*C* - crash cymbal 2
*r* - ride cymbal
*R* - ride bell
*s* - snare
*k* - kick
*1* - high tom
*2* - mid tom
*3* - floor tom

TODO: this is worder horribly
The space character behaves differently in chord mode than in disparate mode. Here, the space character effectively movus through time. To represent the absence of any notes at a point in time, the underscore character *_* is used. The order of characters in each grouping does not matter, e.g., "hk" is the same as "kh".

### Examples
**TODO: show sheet music examples along with what the input would look like to create it**