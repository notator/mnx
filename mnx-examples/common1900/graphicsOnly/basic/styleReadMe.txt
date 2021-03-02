
Having taken a close look at the Draft Spec's style proposals in
    §6.14 Style properties and 
    §6.15 Stylesheet definitions
I think MNX should support CSS in a way that is as standard as possible.
This includes applications being allowed to ignore style settings that are
inappropriate or which they don't support.
For example, applications should be allowed to use their own "house-style" for
fonts and font sizes even if a "font-family" setting says that some other font was
being used when the .mnx file was written.

Conclusions:
1. MNX should have an optional <style> element at the top level (not <stylesheet> as
proposed in the draft spec). The <style> element should contain CSS definitions using
the same syntax as in HTML's <style> element, not the syntax proposed in §6.15 of
the Draft Spec. (We shouldn't try to re-invent the wheel.)
2. The Draft Spec's "smufl-font" should actually be called "music-font". There should
also be a corresponding CSS "text-font" that optionally defines the standard
alphanumeric text font used in a file.
3. All MNX's text elements (see below) except the glyphs used on staves, should have
optional "align" and "orient" attributes. That's instruction, title, author etc.
4. The instruction components: entity, string, image should have an "align" attribute.
5. The instruction components: entity, and image should have a "verticalAlign" attribute.
6. MNX does not need to define "@font-face" to include special fonts. That can be done
later if necessary, in the SVG to which the MNX file is converted, if an unknown font
is declared in a "font-family" statement. 
7. The Draft Spec's "wedge" should be replaced by two elements: "crescWedge" and
"dimWedge". "wedge" has a "type" attribute (that can have values "diminuendo" or
"crescendo") that would conflict with a class attribute (which can change the line's
stroke-width).

So class attributes are redundant because an element's default class (size etc.) is
defined by applications for particular elements using their _name_ (e.g. "title").

- The basic glyphs "clef", "note", "rest" etc. all use the music-font.
  Music fonts should not be expected to support font-styles (e.g. "font-style:italic")
  or font-weights (e.g. "font-weight:bold") but they should support "font-size"
  (for cues, cautionaries etc.) and "color".
  
- An "instruction" uses the text-font by default. An application sets "instruction"
  to its default setting for performance instructions in parts.
  An instruction contains one or more components of type "string" "entity" and
  "image". These are concatenated into a single line instruction.
  
- Other text primitives are "title" and "author" (etc.?)

- The following "extendableText"s (Draft Spec terminology is "spanning directions"):
     "octaveShift", "cresc", "dim", "pedal"
  should be complemented by "accel" and "rit".
  "crescWedge" and "dimWedge" were originally "wedge" spanning directions, but they
  have no text so are not extendableTexts. They are their own classes.
  As always, each of these elements has a distinct default style (different for
  global and part contexts) supplied by the consuming application.
  "octave-shift" and "pedal" are only available in part/measure/directions or
  part/measure/sequence.
  "accel", "rit", "cresc", "dim", "crescWedge" and "dimWedge" are available in
  global/measure/directions, part/measure/directions and part/measure/sequence. 

- Entities: Each consuming application can decide for itself which font to use for
  each individual entity. So here again, the font does not _need_ to be stipulated
  explicitly. Applications should be responsible for aligning entities vertically
  and horizontally depending on the surrounding text. By default, entity baselines
  would be aligned to the surrounding text's baseline.
  
- SVGs: It should be possible to include arbitrary external SVGs.
  In instructions, these could be used as glyphs, and would not be stylable by CSS.
  The size of an <image> element should be determined by its width and height parameters
  (anonymous units as in page size).
  For simplicity of use, I think the MNX <image> element should have attributes that
  control both horizontal (left, right, center), vertical (top, middle, baseline,
  bottom) and orient (above, below) alignment.
  

For example: a small clef could be coded as follows:
    <clef class="cautionary" sign="G" line="2"/>
    
And a small instruction can be:
    <instruction style="font-size:small" location="0">
        <entity style="color:red;text-align:center" value="&ff;"/>
        <instruction style="font-style:italic" value=" diminuendo"/>
        <instruction style="font-style:normal" value=" al fine"/>
    </instruction>
    or
    <instruction class="small" location="0">
        <img src="ff.jpg" alt="fortissimo" width="500" height="60" align="center">
        <instruction style="font-style:italic" value=" diminuendo"/>
        <instruction style="font-style:normal" value=" al fine"/>
    </instruction>

The Draft Spec allows classes to be defined. Class definitions would simplify the
above instruction considerably (especially if the classes are going to be re-used):
<style>
   title, author
   {
       font-face:Optima;
   ]
   instruction, cresc, dim
   {
       font-face:Times New Roman;
   }
   accel, rit
   {
       font-face:Crimson;
       font-size:large;
       font-weight:bold;
       font-style:italic;
       line-style:thick;
       stroke-linecap:round;
       stroke-dasharray:"4 1";
   }
   cresc, dim
   {
       font-style:italic;
       stroke-linecap:round;
       stroke-dasharray:"3 1";
   }
   .small
   {
       font-size:small;
   }
   .italic
   {
       font-style:italic;
   }
   .normalSize
   {
       font-size:normal;
   }
   .redCentered
   {
       color:red;
       text-align:center;
   }
</style>

<clef class="small" sign="G" line="2"/>

<instruction class="small" location="0">
    <entity class="redCentered" value="&ff;"/>
    <instruction class="italic" value=" diminuendo"/>
    <instruction class="normal" value=" al fine"/>
</instruction> 

Digression:
    Possibly, more than one (anonymous) music font could be defined (musicFont1, musicFont2)
    and used in class definitions so that e.g. different shapes of notehead could be used
    at different printout sizes. (The shape of large noteheads in parts should really be
    different from the shape of the small noteheads in scores.)...
    But that can be left to applications to sort out. Only applications know what the 
    the absolute height of the staves is going to be, so they can choose their fonts accordingly.
