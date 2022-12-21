import Reveal from "reveal.js";
import Markdown from "reveal.js/plugin/markdown/markdown.esm.js";
import RevealHighlight from "reveal.js/plugin/highlight/highlight.esm.js";
import Notes from "reveal.js/plugin/notes/notes.esm.js";
import Math from "reveal.js/plugin/math/math.esm.js";
let deck = new Reveal({
  plugins: [Markdown, RevealHighlight, Notes, Math]
});
deck.initialize({
  controls: true,
  progress: true,
  history: true,
  center: true
});
