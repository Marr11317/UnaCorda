## UnaCorda and WalkingBossa

![Preview of UnaCorda](UnaCorda.png?raw=true)
![Preview of WalkingBossa](WalkingBossa.png?raw=true)

UnaCorda and WalkingBossa are fonts for music notation of jazz chord symbols. They allow to seamlessly create beautifully layout chord symbols without the help of an external parser.

These fonts are inspired by the work of [Florian Kretlow](https://github.com/fkretlow) and the impressive [Figurato](https://github.com/fkretlow/figurato) font he developed for figured bass, as well as the work of Ronald Caltabiano and his pioneering Sicilian Numerals font. However, the idea came from [Marc Sabatella](https://github.com/MarcSabatella) and his incredible [Campania](https://github.com/MarcSabatella/Campania) font.
This current version of WalkingBossa uses glyphs from [Petaluma](https://github.com/steinbergmedia/petaluma), and UnaCorda uses glyphs from [Bravura](https://github.com/steinbergmedia/bravura). Layout is achieved with some relatively straightforward contextual substitutions and positioning rules to allow you to enter the most common symbols just by typing naturally.

You can download UnaCorda ([TTF](redist/UnaCorda.ttf?raw=true), [OTF](redist/UnaCorda.otf?raw=true)) and WalkingBossa ([TTF](redist/WalkingBossa.ttf?raw=true), [OTF](redist/WalkingBossa.otf?raw=true)) and follow the standard procedures for installing and selecting fonts on your system.

To use these fonts, simply type as you normally would, and the formatting happens automatically.
# To be edited!!!--------------------------
Numeric indications for inversions and seventh/extended chords (e.g., 6, 7, 64, 643, 43, 9, 13) are automatically superscripted and stacked vertically.
When used in a context where this makes sense,

"b" and "#" turn into flat and sharp,
"bb" and "##" turn into double flat and double sharp,
"h" turns into natural,
"o" and "0" turn into diminished and half-diminished symbols,
and "^" turns into a triangle.
"-" and "=" can be used and repeated to create dashes and double dashes of arbitrary length
to connect superscripted and subscripted numbers.
You can also use "\_" to add an additional parallel dash.
Backslash before a character can be used to prevent the usual substitution
(e.g., "\b" to prevent a "b" from turning into a flat).
# To be edited!!!--------------------------


This font should work in any program that handles fonts reasonably.
Some programs - like Microsoft Word - may require you to explicitly enable OpenType features.

[Manual](docs/manual.md) not there yet
[Changelog](docs/changelog.md) not there yet

*UnaCorda is licensed under the SIL Open Font License. That means that it is free to use. However, developing fonts takes considerable time and effort, so if you regularly earn money with this font (by using it for commercial work or by selling a derivative of it on its own or as part of a larger work or collection), please consider supporting me with a donation [via paypal.](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=S2ZCFC2QSQVQ4&source=url)*
