from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate

# ── Palette ──────────────────────────────────────────────────────────────────
IVORY        = colors.HexColor("#FDFAF4")
SOFT_BLACK   = colors.HexColor("#1C1C1C")
DUSTY_ROSE   = colors.HexColor("#C2847A")
SAGE         = colors.HexColor("#8A9E85")
GOLD         = colors.HexColor("#C4A35A")
LAVENDER     = colors.HexColor("#9B8EA8")
MIST         = colors.HexColor("#E8E3DA")
DEEP_PLUM    = colors.HexColor("#3D2B3D")

# ── Vocabulary data ───────────────────────────────────────────────────────────
vocab = [
    # A
    ("Abeyance","A state of temporary suspension or inactivity.","The project was held in abeyance until funding was secured."),
    ("Acrimony","Bitterness or ill feeling in speech or manner.","The divorce was filled with acrimony on both sides."),
    ("Adumbrate","To outline or sketch something; to foreshadow.","The architect adumbrated the new design in a few swift strokes."),
    ("Aeon","An indefinitely long period of time; an age.","The canyon was carved over aeons by the slow persistence of water."),
    ("Aesthete","A person who has or professes a special appreciation of art and beauty.","As a true aesthete, she spent hours in the gallery lost in silent contemplation."),
    ("Afflatus","A divine creative impulse or inspiration.","The poem arrived as a sudden afflatus at three in the morning."),
    ("Agrestic","Relating to the countryside; rural and unpolished.","There was something refreshingly agrestic about life on the small farm."),
    ("Alacrity","Brisk and cheerful readiness.","She accepted the invitation with alacrity, eyes bright with excitement."),
    ("Albescent","Growing or shading into white.","The albescent sky just before dawn held a hushed, sacred quality."),
    ("Alembic","A vessel used in distillation; anything that purifies or refines.","Her mind was an alembic, transforming raw experience into luminous prose."),
    ("Aloof","Not friendly or forthcoming; cool and distant.","He stood aloof at the party, watching the crowd with quiet detachment."),
    ("Amaranthine","Undying; of a deep, purplish-red color.","Her amaranthine gown swept the marble floor like a slow tide."),
    ("Ambrosial","Exceptionally pleasing to taste or smell; divine.","The ambrosial scent of jasmine filled the evening garden."),
    ("Ameliorate","To make something bad better; to improve.","Soft music can ameliorate the tension of a long journey."),
    ("Amorphous","Without a clearly defined shape or form.","Her grief was amorphous—vast, formless, impossible to hold."),
    ("Anamnesis","The recollection of past events; a reminiscence.","The old photograph stirred a deep anamnesis of childhood summers."),
    ("Anchorite","A person who has withdrawn from society to live in seclusion.","He retreated to the mountains like an anchorite, seeking only silence."),
    ("Anodyne","Not likely to cause offence or disagreement; painkilling.","Her words were gentle and anodyne, smoothing over the raw edges of sorrow."),
    ("Antediluvian","Of or belonging to the time before the biblical Flood; very old.","The antediluvian oak tree had witnessed centuries pass beneath its boughs."),
    ("Aperture","An opening, hole, or gap.","Light poured through the narrow aperture in the stone wall."),
    ("Aphelion","The point in a planet's orbit farthest from the sun.","In its aphelion, the comet seemed to pause, held briefly by the dark."),
    ("Apocryphal","Of doubtful authenticity; unlikely to be true.","The story of the ghost on the staircase was almost certainly apocryphal."),
    ("Apothegm","A pithy, instructive saying.","'Less is more' is the architect's favourite apothegm."),
    ("Arcadian","Relating to an ideal rustic paradise; simple and happy.","The valley had an arcadian beauty untouched by the modern world."),
    ("Ardor","Great enthusiasm or passion.","She pursued her craft with an ardor that left no room for doubt."),
    ("Argent","Silvery; the heraldic term for silver.","The argent surface of the lake reflected a cold winter moon."),
    ("Arroyo","A steep-sided gully cut by running water in an arid region.","They followed the dry arroyo into the canyon's cool shadow."),
    ("Ashen","Pale grey in color; resembling ash.","His ashen face told her everything before he had spoken a word."),
    ("Asperity","Harshness of tone or manner; roughness of surface.","She spoke without asperity, but the message was unmistakably firm."),
    ("Astral","Relating to the stars; of or resembling a star.","The astral light of the Milky Way arched overhead like a cathedral vault."),
    # B
    ("Baleful","Threatening harm; menacing.","The baleful glare of the lighthouse swept the fog-shrouded sea."),
    ("Beatific","Feeling or expressing blissful happiness.","A beatific smile crossed her face as she held the sleeping child."),
    ("Bedim","To make less bright; to obscure.","Sorrow had begun to bedim the joy she once wore effortlessly."),
    ("Belletristic","Related to the appreciation of fine literature.","The salon had a belletristic atmosphere—books everywhere, conversation unhurried."),
    ("Benison","A blessing.","The old woman offered her benison quietly, hands folded like prayer."),
    ("Bespoke","Made to individual order; custom-made.","He wore a bespoke suit the color of winter smoke."),
    ("Betide","To happen; to befall.","Whatever betide, she resolved to face it with grace."),
    ("Bibliophile","A person who collects or has a great love of books.","As a bibliophile, she could not pass a bookshop without entering."),
    ("Billowing","Moving or flowing in large waves; swelling outward.","The billowing curtains breathed in and out with the summer breeze."),
    ("Bittersweet","Sweet with a bitter aftertaste; pleasant but tinged with sadness.","Their farewell was bittersweet—full of gratitude and quiet grief."),
    ("Blithe","Happy-go-lucky; showing a casual and cheerful indifference.","She moved through the world with a blithe confidence that charmed everyone."),
    ("Blithesome","Cheerful and light-hearted.","The blithesome laughter of children drifted through the open window."),
    ("Boreal","Relating to the north; of or denoting the climatic zone south of the tundra.","A boreal wind swept down from the mountains, sharp and clean."),
    ("Bravura","Great technical skill and brilliance shown in a performance.","The pianist's closing cadenza was pure bravura—breathtaking and exact."),
    ("Bucolic","Relating to the pleasant aspects of the countryside.","They spent a bucolic summer cycling through lavender fields and gentle hills."),
    ("Burnished","Polished by rubbing; made shiny.","The burnished copper of the autumn leaves glowed in the late light."),
    # C
    ("Capricious","Given to sudden and unaccountable changes of mood or behaviour.","The capricious weather shifted from sun to storm within an hour."),
    ("Cascade","A small, steep waterfall; to flow downward rapidly.","Her laughter cascaded through the room like water over smooth stones."),
    ("Cashmere","A fine, soft wool; something of exceptional softness.","She wrapped herself in cashmere and watched the first snow fall."),
    ("Celestial","Belonging or relating to heaven; sublimely beautiful.","The choir's celestial harmonies rose into the vaulted stone ceiling."),
    ("Cerulean","A deep sky-blue color.","The cerulean sea stretched to the horizon, unbroken and still."),
    ("Chiaroscuro","The interplay of light and shadow in a work of art.","The photographer had a gift for chiaroscuro—every image a study in contrast."),
    ("Chimera","A thing that is hoped or wished for but is unlikely to be achieved.","Peace felt like a chimera—beautiful, distant, and just out of reach."),
    ("Chrysalis","A transitional state; a pupa enclosed in its cocoon.","University was her chrysalis—she emerged from it almost unrecognisable."),
    ("Cimmerian","Relating to deep darkness; impenetrably dark.","The cimmerian hours before dawn are when I write most honestly."),
    ("Clandestine","Kept secret or done secretively.","They exchanged clandestine glances across the candlelit table."),
    ("Clarion","Loud and clear; a shrill narrow-tubed war trumpet.","The clarion call of the bird cut through the morning mist."),
    ("Cobalt","A deep blue pigment or color.","She painted the shutters cobalt, a shock of blue against white stone."),
    ("Cognizant","Having knowledge or being aware of something.","She was fully cognizant of the risks and chose to proceed anyway."),
    ("Confluence","The junction of two rivers; a coming together of things.","The café sat at the confluence of three narrow medieval streets."),
    ("Contemplative","Expressing or involving prolonged thought.","He lived a contemplative life—few words, deep attention, quiet rooms."),
    ("Convivial","Cheerful and friendly; relating to good company.","The convivial atmosphere of the dinner lasted long past midnight."),
    ("Corporeal","Relating to a person's body, especially as opposed to the spirit.","Art, she believed, was the spirit made corporeal."),
    ("Coruscate","To flash or sparkle.","The diamonds coruscated under the chandelier's warm light."),
    ("Crepuscular","Relating to twilight.","The crepuscular hour between day and dark is when the world holds its breath."),
    ("Crystalline","Having the structure of a crystal; very clear.","The crystalline quality of the alpine air made everything sharper, closer."),
    # D
    ("Daedal","Complex, ingenious, or skillfully crafted.","The daedal woodwork of the old library was almost impossible to replicate."),
    ("Damask","A rich, heavily patterned fabric; a soft pinkish or light-red hue.","The damask tablecloth caught the candlelight and glowed softly."),
    ("Dawdle","To move slowly; to waste time.","She liked to dawdle on the walk home, collecting small beautiful things."),
    ("Dawnlit","Lit by the first light of dawn.","They stood on the dawnlit terrace with their hands wrapped around warm cups."),
    ("Daydream","A series of pleasant thoughts that distract one from the present.","She often lost herself in a daydream of a quieter, slower life."),
    ("Dappled","Marked with spots or rounded patches of color.","Dappled light fell through the canopy onto the moss below."),
    ("Dazzle","To blind temporarily with an overwhelming display of light.","The city at night dazzled her—a scattered galaxy brought down to earth."),
    ("Deliquesce","To dissolve or melt away; to become liquid by absorbing moisture.","In the heat, the sugar began to deliquesce into a pale amber syrup."),
    ("Demure","Modest, reserved, and shy.","She gave a demure smile but said nothing."),
    ("Diaphanous","Light, delicate, and translucent.","The diaphanous curtains stirred like ghosts in the open window."),
    ("Diffuse","Spread over a wide area; not concentrated.","The light in the studio was deliberately diffuse—soft and shadowless."),
    ("Dilettante","A person who cultivates an interest in art without pursuing it professionally.","He was a charming dilettante—curious about everything, master of nothing."),
    ("Diurnal","Of or during the day; occurring every day.","She found comfort in diurnal rhythms: coffee, light, pages turned."),
    ("Divagate","To stray from the subject; to wander.","His mind was prone to divagate, slipping from thought to thought like water."),
    ("Dolorous","Feeling or expressing great sorrow.","The dolorous notes of the cello filled the room with a beautiful sadness."),
    ("Dulcet","Sweet and soothing, often applied to sound.","The dulcet tones of the violin carried through the warm evening air."),
    ("Dusky","Darkish in color; shadowy and dim.","The dusky violet of the mountains at dusk was nearly impossible to name."),
    # E
    ("Ebullience","The quality of being cheerful and full of energy.","His ebullience was contagious—within minutes, the whole room was laughing."),
    ("Éclat","Brilliant display or effect; great renown.","She delivered the speech with remarkable éclat."),
    ("Effulgent","Radiant; shining brilliantly.","The effulgent summer sun turned the fields to gold."),
    ("Elegiac","Having a mournful quality; relating to an elegy.","The film had an elegiac beauty—tender, slow, and already grieving."),
    ("Elysian","Relating to Elysium; blissful and idyllic.","The garden, in full bloom, had an elysian tranquility."),
    ("Emollient","Softening and soothing; a substance that softens the skin.","Her voice had an emollient quality that quieted the most anxious rooms."),
    ("Empyrean","Relating to heaven; the highest heaven.","She felt she had glimpsed the empyrean—pure light, pure peace."),
    ("Enchant","To delight; to put under a spell.","The old city enchanted her at every turn—a labyrinth of beauty."),
    ("Encomium","A speech or piece of writing that praises someone highly.","The obituary read like an encomium—warm, precise, and deeply felt."),
    ("Enigmatic","Difficult to interpret or understand; mysterious.","He had an enigmatic quality that made people lean in when he spoke."),
    ("Ephemeral","Lasting for a very short time.","Cherry blossoms are ephemeral—perhaps that is what makes them sacred."),
    ("Equanimity","Mental calmness under stress.","She faced the diagnosis with a quiet equanimity that moved everyone who knew her."),
    ("Evanescent","Soon passing out of sight, memory, or existence.","The evanescent mist dissolved as the sun climbed higher."),
    ("Evocative","Bringing strong images, memories, or feelings to mind.","The music was deeply evocative—she was sixteen again in an instant."),
    ("Exquisite","Extremely beautiful and delicate.","The embroidery was exquisite—each stitch placed with devotion."),
    # F
    ("Fable","A short story with a moral; a legend.","Her grandmother told fables every evening, stories rooted in earth and sky."),
    ("Fading","Losing brightness or vitality.","The fading light of the afternoon gave the room a sepia tenderness."),
    ("Felicity","Intense happiness; an ability to find appropriate expression.","She wrote with a felicity that made difficult things feel effortless."),
    ("Fenestrated","Having windows; perforated.","The fenestrated stone screens filtered the desert sun into patterned lace."),
    ("Fervent","Having or displaying a passionate intensity.","He was a fervent believer in the power of quiet, careful work."),
    ("Filigree","Ornamental work of fine twisted wire; something delicate.","The frost had formed a filigree of ice on the windowpane."),
    ("Flicker","To shine unsteadily; a small, wavering light.","The last candle flickered once and went dark."),
    ("Fluvial","Relating to rivers.","The fluvial landscape of the delta was ever-shifting, alive."),
    ("Forlorn","Pitifully sad and abandoned.","A single forlorn lamp burned in the window of the empty house."),
    ("Fragrant","Having a pleasant or sweet smell.","The fragrant air of the herb garden rose in the evening heat."),
    ("Fugacious","Fleeting; tending to disappear.","Beauty, like all fugacious things, is precious because it does not stay."),
    ("Fugue","A state of altered consciousness; a musical composition.","She entered the studio each morning and disappeared into a creative fugue."),
    ("Fulvous","Tawny, dull yellow-brown.","The fulvous grasses of the plain swayed under a heavy autumn sky."),
    # G
    ("Gauzy","Light and translucent; resembling gauze.","Gauzy clouds drifted across the face of the moon."),
    ("Gossamer","Light, delicate, and insubstantial; a fine filmy substance.","Her veil was gossamer, catching the light like a breath held still."),
    ("Gracile","Slender and graceful.","The gracile branches of the silver birch moved in the faintest wind."),
    ("Grandeur","Impressiveness and splendour.","The grandeur of the mountain vista reduced them both to silence."),
    ("Grotto","A small picturesque cave.","They discovered a hidden grotto carpeted in emerald moss."),
    ("Guileless","Devoid of guile; innocent and without deception.","She had a guileless honesty that people often mistook for naivety."),
    # H
    ("Halcyon","Denoting a period of time that was happy and prosperous.","Those halcyon summers by the sea lived inside her like a second heartbeat."),
    ("Hallow","To honor as sacred.","The old cathedral hallowed the silence within its stone walls."),
    ("Harbinger","A person or thing that announces or signals the approach of another.","The first crocus was always a harbinger of longer days ahead."),
    ("Harmony","The combination of simultaneously sounded notes to produce a pleasing effect.","There was a harmony to the village—an old order of stone, wood, and water."),
    ("Hauntingly","In a way that is difficult to forget; evocatively.","The melody was hauntingly familiar, though she couldn't place it."),
    ("Haze","A slight obscuration of the lower atmosphere; an indistinct impression.","The afternoon dissolved into a golden haze of heat and drowsiness."),
    ("Heliotrope","A plant that turns towards the sun; a pinkish-purple color.","She painted the walls heliotrope, a color between dusk and bloom."),
    ("Hiraeth","A Welsh word meaning a longing for home or a past that may never have been.","Listening to the old songs, she felt hiraeth stir beneath her ribs."),
    ("Honeyed","Having the nature of honey; soothing and sweet.","He spoke in honeyed tones that made even hard news sound gentle."),
    ("Horizon","The line at which the earth's surface and the sky appear to meet.","She kept her eyes on the horizon as if the answer lived there."),
    ("Hyacinthine","Resembling a hyacinth; of a deep, rich purple-blue.","His hyacinthine prose was beloved by readers of a certain refinement."),
    # I
    ("Idyllic","Like an idyll; extremely happy, peaceful, or picturesque.","The valley had an idyllic quality—quiet roads, slow time, gentle hills."),
    ("Illumine","To light up; to enlighten.","Great literature illumines not just the mind but the heart."),
    ("Illusive","Based on illusion; deceptive.","Her calm was illusive—inside, a storm moved quietly through her."),
    ("Imaginal","Relating to imagination; of or at the stage of an imago.","She lived largely in the imaginal realm, where stories were more real than facts."),
    ("Immaculate","Perfectly clean or tidy; free from flaws or mistakes.","The manuscript was immaculate—not a word wasted, not a comma wrong."),
    ("Immutable","Unchanging over time or unable to be changed.","The immutable laws of beauty held across every culture she had studied."),
    ("Impalpable","Unable to be felt by touch; not easily grasped by the mind.","There was an impalpable sadness to the place—felt but never named."),
    ("Incandescent","Emitting light as a result of being heated; full of strong emotion.","Her speech was incandescent—every word charged, every pause deliberate."),
    ("Inchoate","Just begun and not fully formed or developed.","She had the inchoate sense of something vast approaching."),
    ("Ineluctable","Unable to be resisted or avoided; inescapable.","There was an ineluctable quality to the tide—it would come, and come again."),
    ("Ineffable","Too great or extreme to be expressed in words.","The ineffable beauty of the sunrise left her wordless for several minutes."),
    ("Infuse","To fill something with a quality.","She tried to infuse every room she decorated with a sense of calm."),
    ("Ingénue","An innocent or unsophisticated young woman.","She played the ingénue convincingly, though she was anything but."),
    ("Inviolable","Never to be broken or dishonoured.","Between them, silence was an inviolable agreement."),
    ("Iridescent","Showing luminous colors that seem to change when seen from different angles.","The dragonfly's wings were iridescent, shifting between teal and copper."),
    # J
    ("Jade","A hard, typically green stone used in jewellery; a blue-green color.","The jade-coloured sea lapped gently at the white stone quay."),
    ("Jasmine","A climbing plant with fragrant white or yellow flowers.","The jasmine outside her window made every evening smell like a dream."),
    ("Jovial","Cheerful and friendly.","He was jovial by nature—the kind of person rooms seemed glad to receive."),
    ("Jubilant","Feeling or expressing great happiness.","The jubilant crowd spilled into the streets long after midnight."),
    ("Juliet","Associated with romance and balcony scenes; a proper noun used lyrically.","She stood on the narrow balcony, playing Juliet to an empty courtyard."),
    # K
    ("Kairos","The right, critical, or opportune moment.","She sensed the kairos of the moment and said exactly the right thing."),
    ("Keen","Sharp or penetrating in quality; eager.","He had a keen eye for light—he always knew when the photograph was there."),
    ("Keening","Wailing in grief; a high mournful sound.","The wind moved through the pines with a keening she felt in her chest."),
    ("Kindred","Similar in kind; related.","She found in him a kindred spirit—someone who also preferred books to parties."),
    ("Knell","The sound of a bell rung solemnly; a sound or sign indicating the end.","The final chord sounded like a knell, beautiful and irreversible."),
    # L
    ("Labyrinthine","Resembling a labyrinth; intricate and confusing.","The labyrinthine streets of the old city rewarded those who wandered slowly."),
    ("Lachrymose","Tearful or given to weeping; inducing tears.","The film was delicately lachrymose—touching without manipulation."),
    ("Lambent","Glowing or flickering with a soft radiance.","The lambent firelight moved across the walls like something alive."),
    ("Languor","Physical or mental inertia; a relaxed pleasantness.","A summer languor settled over the house in the long afternoon."),
    ("Lapis","Short for lapis lazuli; a rich, deep blue color.","The ceiling was painted lapis, scattered with gold-leaf stars."),
    ("Lassitude","Physical or mental weariness; lack of energy.","After the long journey, a welcome lassitude came over her."),
    ("Latent","Existing but not yet developed or manifest.","There was a latent sadness in him that surfaced only in his paintings."),
    ("Laud","To praise someone or something highly.","The novel was lauded by critics as a work of rare and quiet genius."),
    ("Lilt","A gentle, rhythmic swaying movement; a pleasant cadence in speech.","Her voice had a natural lilt that made everything she said sound musical."),
    ("Limpid","Completely clear and transparent; expressed without complexity.","Her limpid prose made even grief feel lucid."),
    ("Liminal","Occupying a position at, or on both sides of, a threshold.","Dawn is a liminal hour—not quite night, not yet day."),
    ("Lissome","Thin, supple, and graceful.","She moved with a lissome grace that made others want to watch her."),
    ("Litany","A series of prayers; a long, repetitive list.","He recited his litany of regrets quietly, then let them go."),
    ("Loquacious","Tending to talk a great deal; talkative.","She was wonderfully loquacious—to be seated beside her was a gift."),
    ("Lucent","Glowing with light; translucent.","The lucent quality of the winter sky made everything seem closer, starker."),
    ("Lucid","Expressed clearly; easy to understand.","She had a lucid intelligence that cut through complexity without effort."),
    ("Luminous","Full of or shedding light; glowing.","The luminous quality of her watercolors came from years of patient practice."),
    ("Lunular","Relating to a crescent shape; moon-like.","She wore a lunular pendant, silver, curved like the last sliver of moon."),
    ("Lush","Growing luxuriantly; rich and abundant.","The lush garden was a world contained—green, cool, and private."),
    ("Lustrous","Having luster; shining.","Her lustrous dark hair was the first thing anyone noticed about her."),
    # M
    ("Madeleine","Something that triggers involuntary memory; from Proust.","The taste of the old pastry was her madeleine—childhood arrived in an instant."),
    ("Maenad","A wild or frenzied woman; a female follower of Dionysus.","She danced like a maenad—abandoned, ecstatic, beyond care."),
    ("Majestic","Having impressive beauty, scale, or dignity.","The majestic slowness of the glacier reminded her of geological time."),
    ("Malleable","Easily influenced; able to be shaped.","The clay was pleasantly malleable in her hands after being warmed."),
    ("Manifest","Clear or obvious; to make something evident.","Her talent began to manifest early—through precise, fearless observation."),
    ("Marbled","Having the appearance of veined marble.","The marbled endpapers of the old book were as beautiful as any painting."),
    ("Maudlin","Self-pityingly sentimental; tearful.","The letter was honest rather than maudlin—grief without performance."),
    ("Mellifluous","Sweet or musical; pleasant to hear.","His mellifluous voice was ideally suited to reading poetry aloud."),
    ("Mercurial","Subject to sudden changes of mood or mind; lively, clever.","She was mercurial—her moods changed like weather over open water."),
    ("Meridian","The highest point; relating to midday.","They arrived at the meridian of their happiness without knowing it."),
    ("Metaphysical","Relating to abstract concepts beyond physical experience.","Her poems had a metaphysical quality—earthly images that opened onto infinity."),
    ("Mnemonic","Assisting or intended to assist memory.","The rhyme was a simple mnemonic, but it held the whole theory inside it."),
    ("Monastic","Relating to monasteries; a secluded, simple life.","She lived a monastic existence—reading, writing, and walking alone."),
    ("Moonlit","Lit by moonlight.","They walked the moonlit beach in silence, saying what needed to be felt."),
    ("Mutable","Liable to change.","She understood that happiness was mutable—to be held, not grasped."),
    ("Murmuration","The action of murmuring; a flock of starlings in flight.","They stood together watching the murmuration, speechless at the spectacle."),
    ("Muse","A person or spirit inspiring creative work; to think deeply.","She walked the canal path every morning to muse without interruption."),
    # N
    ("Nacreous","Resembling mother-of-pearl; iridescent.","The nacreous clouds at sunset shimmered in colors without names."),
    ("Nascent","Just coming into existence; beginning to develop.","She nurtured the nascent idea with patience, not wanting to force it."),
    ("Nebulous","Not clearly defined; hazy.","Her plans were still nebulous—beautiful shapes without solid edges."),
    ("Noctilucent","Luminous at night; applied to high-altitude clouds.","The noctilucent clouds glowed silver-blue long after the sun had gone."),
    ("Nocturnal","Done, occurring, or active at night.","She was nocturnal by temperament—her best thinking happened after midnight."),
    ("Nostalgic","Feeling a wistful longing for the past.","The old film left her nostalgic for a decade she had never lived through."),
    ("Numinous","Having a strong religious or spiritual quality; mysterious and awe-inspiring.","The forest at dusk had a numinous quality—she walked more quietly there."),
    # O
    ("Oblique","Neither parallel nor at a right angle; not explicit.","Her criticism was oblique but landed precisely."),
    ("Obscure","Not discovered or known; unclear.","She had an obscure but genuine talent for rendering light in oil."),
    ("Odalisque","A female slave in a harem; a subject in orientalist painting.","The painting depicted an odalisque—languid, light-drenched, unapologetically observed."),
    ("Opalescent","Showing varying colors depending on the angle; milky.","The opalescent sky before rain had a quality of held breath."),
    ("Oracle","A priest or priestess delivering divine utterance; an authoritative pronouncement.","She spoke rarely, but when she did, her words were treated like oracles."),
    ("Orphic","Relating to Orpheus; mystical, occult.","His music had an orphic power—it reached places words could not."),
    ("Ossify","To harden or become fixed; to cease developing.","She feared her thinking would ossify if she stopped reading new ideas."),
    # P
    ("Palimpsest","Something altered but still bearing visible traces of an earlier form.","The city was a palimpsest—Roman walls beneath medieval streets beneath modernity."),
    ("Panacea","A solution to all problems.","There is no panacea for loneliness, but beauty comes close."),
    ("Pastoral","Used to describe the pleasant aspects of the countryside.","The piece had a pastoral quality—unhurried, spacious, full of green light."),
    ("Patina","A green or brownish film on bronze; a sheen on an old surface.","The copper door had acquired a beautiful patina over the centuries."),
    ("Pensive","Engaged in deep thought.","She sat in a pensive silence, looking at the water without really seeing it."),
    ("Penumbra","The partially shaded outer region of a shadow; a peripheral area.","She lived in the penumbra between certainty and possibility."),
    ("Petrichor","The pleasant smell that frequently accompanies the first rain after a long warm period.","Petrichor rose from the dry earth and she stepped outside to breathe it in."),
    ("Phantasmal","Of the nature of a phantom; illusory.","The fog gave the coastline a phantasmal, dreamlike quality."),
    ("Phosphorescent","Emitting light without combustion or heat.","The phosphorescent wake of the boat glowed beneath the surface like a dream."),
    ("Plangent","Loud and reverberating, with an expressive quality of sadness.","The plangent toll of the bell carried across the winter water."),
    ("Poignant","Evoking a keen sense of sadness or regret.","The final scene was deeply poignant—quietly devastating in its simplicity."),
    ("Porcelain","A white vitrified translucent ceramic; delicate and smooth.","She had a porcelain stillness that made her difficult to read."),
    ("Pristine","In its original condition; unspoiled; clean and fresh.","The pristine snow lay unbroken, waiting for the first set of footprints."),
    ("Profound","Very great or intense; having deep insight.","The simplest question, asked sincerely, can become the most profound."),
    ("Protean","Tending or able to change frequently or easily; versatile.","Her talent was protean—equally at home in a sonnet or a sprawling novel."),
    # Q
    ("Quiescent","In a state of quiet inactivity; calm.","The city was quiescent at four in the morning—still, cool, entirely hers."),
    ("Quintessence","The most perfect or typical embodiment of a quality.","Venice, in winter, fog-filled and lamp-lit, is the quintessence of atmosphere."),
    ("Quixotic","Exceedingly idealistic; unrealistic and impractical.","Her quixotic dream of restoring the old house seemed mad until it was done."),
    # R
    ("Radiant","Sending out light; glowing; clearly very happy.","She stood in the doorway, radiant with the news she had yet to share."),
    ("Rapture","A feeling of intense pleasure or joy.","She listened to the concerto in something close to rapture."),
    ("Rarefied","Made less dense; belonging to a select group.","The rarefied atmosphere of the archive suited her—silence, old paper, order."),
    ("Refulgent","Shining brightly; radiant.","The refulgent dawn broke over the mountains in layers of rose and gold."),
    ("Reminisce","To indulge in enjoyable recollection of past events.","They spent the evening reminiscing—old photographs spread across the kitchen table."),
    ("Repose","A state of rest, sleep, or tranquillity.","She found repose only in music—everything else required effort."),
    ("Resplendent","Attractive and impressive through being richly colourful or sumptuous.","The cathedral interior was resplendent—gold leaf and candlelight in every direction."),
    ("Reverie","A state of being pleasantly lost in one's thoughts.","She drifted into a reverie over her coffee, watching the rain."),
    ("Rhapsodic","Relating to or having the nature of rhapsody; extravagantly enthusiastic.","His review of the exhibition was almost rhapsodic in its praise."),
    ("Ripple","A small wave on water's surface; a gradually spreading effect.","A single kind word can send ripples through a life in unexpected directions."),
    # S
    ("Sacrosanct","Too important or valuable to be interfered with.","Her writing hour was sacrosanct—the whole household understood this."),
    ("Sanguine","Optimistic, especially in difficult situations.","She remained sanguine about the future, even when the evidence was bleak."),
    ("Saudade","A deep emotional state of melancholic longing for something absent.","She couldn't translate saudade; she could only play it on the guitar."),
    ("Scintilla","A tiny trace; a spark.","Not a scintilla of doubt crossed her face as she made the decision."),
    ("Scintillate","To sparkle; to be brilliant.","The conversation scintillated—idea lighting idea like dominoes of light."),
    ("Selenic","Of or relating to the moon.","The selenic glow through the curtains was enough light to read by."),
    ("Seraph","An angelic being; the highest order of angels.","He had drawn her as a seraph—all light and hovering implication."),
    ("Seraphic","Characteristic of or resembling a seraph; lovely and serene.","The sleeping child had a seraphic expression that dissolved her anxieties."),
    ("Serene","Calm, peaceful, and untroubled.","The lake was serene at daybreak—glassy, silver, and entirely still."),
    ("Sfumato","A technique of soft or hazy blending of colors in painting.","The sfumato of the distant hills gave the landscape a dreamlike gentleness."),
    ("Shimmering","Shining with a soft, slightly wavering light.","The mirage shimmered on the road ahead like a pool of silver water."),
    ("Sibylline","Relating to a sibyl; mysterious and prophetic.","Her sibylline remarks made more sense in retrospect than at the time."),
    ("Silhouette","The dark shape and outline of someone or something visible against a lighter background.","The silhouette of the cypress tree against the dusk sky was elegant and exact."),
    ("Silvery","Like silver in color or texture; having a gentle brightness.","A silvery mist rose from the river in the cold morning air."),
    ("Sinuous","Having many curves and turns; lithe and flexible.","The sinuous river wound through the valley like a sentence still being formed."),
    ("Somnolent","Sleepy; inducing drowsiness.","The somnolent afternoon, heavy with sun, begged to be slept through."),
    ("Sonorous","Imposingly deep and full in sound; using impressively grand words.","The organ's sonorous notes filled the vaulted space completely."),
    ("Sorrow","Deep distress caused by loss, disappointment, or other misfortune.","She held her sorrow like a book she wasn't ready to close."),
    ("Spellbinding","Holding the attention as though by magic.","The dancer was spellbinding—the audience barely breathed."),
    ("Stillness","The absence of movement or sound.","The stillness of the snow-covered forest was profound and complete."),
    ("Sublime","Of such excellence or beauty as to inspire great admiration.","The view from the summit was nothing short of sublime."),
    ("Suffuse","Gradually spread through or over; to flush.","The golden light suffused the room, softening every edge."),
    ("Supernal","Relating to the sky or the heavens; celestial.","The supernal light of the comet was visible for only three winter nights."),
    ("Susurrus","A whispering or murmuring sound.","The susurrus of the pine needles was the only sound in the forest."),
    ("Sylvan","Relating to the woods; pleasantly rural or pastoral.","She had grown up in a sylvan village—all oak and moss and dappled lanes."),
    # T
    ("Tacit","Understood or implied without being stated.","There was a tacit agreement between them: some things needed no words."),
    ("Tenuous","Very weak or slight; slender.","The evidence was tenuous, but the argument was beautiful in its structure."),
    ("Threnody","A lament; a song of mourning.","The final movement was a threnody—grief made musical and bearable."),
    ("Timeless","Not affected by the passage of time or changes in fashion.","Good writing is timeless—it does not date; it only deepens."),
    ("Torpid","Mentally or physically inactive; lethargic.","The torpid heat of the afternoon turned everyone to languor."),
    ("Transcendent","Beyond or above the range of normal human experience; surpassing the ordinary.","She experienced moments of transcendent clarity when she painted alone."),
    ("Tremulous","Trembling or quivering; timid, nervous.","He spoke with a tremulous excitement, afraid that happiness might break."),
    ("Twilight","The soft glowing light from the sky after the sun has set.","They always met at twilight, when the world softened its edges."),
    # U
    ("Umbra","The fully shaded inner region of a shadow; darkness.","She retreated into the umbra of the doorway, watching without being seen."),
    ("Undulate","To move with a smooth, wave-like motion.","The fields of lavender undulated under the warm afternoon wind."),
    ("Unspoken","Not said but understood.","The room was full of unspoken things, heavy and beautiful."),
    ("Unearthly","Unnaturally strange; too perfect for this world.","There was an unearthly quality to the silence after the storm."),
    ("Unwavering","Steady or resolute; not wavering.","Her unwavering belief in the work kept her writing through the doubt."),
    ("Uxorious","Having or showing an excessive fondness for one's wife.","He was unashamedly uxorious—she was, he said, his entire reason for care."),
    # V
    ("Valediction","The action of saying farewell; a farewell speech.","Her valediction was brief—a few honest words and then she was gone."),
    ("Vaporous","Of the nature of vapor; vague and insubstantial.","Her memories of that summer were vaporous—more feeling than fact."),
    ("Vellum","A fine parchment; a creamy writing paper.","The invitation was printed on vellum, cool and slightly translucent to the touch."),
    ("Velvet","A closely woven fabric of silk with a soft, thick pile; exceptionally smooth.","The velvet darkness of the new moon night pressed softly against the windows."),
    ("Veracious","Speaking or representing the truth.","She was rigorously veracious—she would not say a thing she did not believe."),
    ("Verdant","Green with grass or other rich vegetation.","The verdant hills rose steeply from the pale road below."),
    ("Vesper","The evening star; evening; the last of the canonical hours.","The vesper bells rang across the rooftops as the first stars appeared."),
    ("Vestige","A trace of something that is disappearing or no longer exists.","Not a vestige of the old house remained—only the oak in the garden."),
    ("Vignette","A brief evocative description or account; a small illustration.","She wrote in vignettes—small, luminous scenes that implied entire lives."),
    ("Viridian","A blue-green pigment; the color of deep, rich green.","The viridian depth of the rainforest canopy took her breath away."),
    ("Visceral","Relating to deep inward feelings; gut-level.","The performance had a visceral power that left the audience shaken."),
    ("Visionary","Thinking about or planning the future with wisdom; a dreamer.","She was a visionary—thirty years ahead of every conversation she entered."),
    ("Vivid","Producing powerful feelings or strong, clear images in the mind.","Her most vivid memory was also the simplest: a yellow dress, late sun."),
    ("Voracious","Wanting or devouring great quantities; highly enthusiastic.","She was a voracious reader—three books a week and always hungry for more."),
    # W
    ("Wanderlust","A strong desire to travel and explore the world.","Her wanderlust never fully settled—she was always partly elsewhere."),
    ("Wistful","Having or showing a feeling of vague or regretful longing.","She gave the old photograph a wistful look before folding it away."),
    ("Wraithlike","Resembling a ghost; thin and pale.","She moved wraithlike through the fog, barely disturbing the air."),
    # X
    ("Xenophile","A person who is attracted to foreign peoples, cultures, or customs.","As a xenophile, she collected recipes, languages, and train tickets in equal measure."),
    ("Xeric","Containing or characterized by little moisture.","The xeric landscape had a stark beauty—all bone and sky and silence."),
    # Y
    ("Yielding","Inclined to give way to arguments, demands, or pressure; soft or flexible.","The yielding light of late autumn gave everything a tender quality."),
    ("Yen","A longing or yearning.","She felt a deep yen for the sea whenever she was too long inland."),
    # Z
    ("Zeal","Great energy or enthusiasm in pursuit of a cause or objective.","She pursued her craft with a quiet but absolute zeal."),
    ("Zeitgeist","The defining spirit of a particular period of history.","The novel perfectly captured the zeitgeist of its decade."),
    ("Zenith","The time at which something is most powerful or successful.","At its zenith, the garden was almost impossible—colour everywhere, effortless."),
    ("Zephyr","A soft gentle breeze.","A zephyr moved through the long grass, cool and unhurried."),
]

# ── Page setup ─────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

# ── Style definitions ──────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    cover_title = ParagraphStyle(
        "CoverTitle",
        fontName="Times-BoldItalic",
        fontSize=38,
        leading=46,
        textColor=DEEP_PLUM,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    cover_sub = ParagraphStyle(
        "CoverSub",
        fontName="Times-Italic",
        fontSize=14,
        leading=18,
        textColor=GOLD,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    cover_body = ParagraphStyle(
        "CoverBody",
        fontName="Times-Roman",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#5A4A5A"),
        alignment=TA_CENTER,
    )
    section_letter = ParagraphStyle(
        "SectionLetter",
        fontName="Times-BoldItalic",
        fontSize=32,
        leading=36,
        textColor=GOLD,
        alignment=TA_CENTER,
        spaceBefore=14,
        spaceAfter=6,
    )
    word_style = ParagraphStyle(
        "Word",
        fontName="Times-Bold",
        fontSize=12,
        leading=15,
        textColor=DEEP_PLUM,
        spaceAfter=1,
    )
    pos_style = ParagraphStyle(
        "POS",
        fontName="Times-Italic",
        fontSize=9,
        leading=11,
        textColor=DUSTY_ROSE,
        spaceAfter=1,
    )
    meaning_style = ParagraphStyle(
        "Meaning",
        fontName="Times-Roman",
        fontSize=10,
        leading=13,
        textColor=SOFT_BLACK,
        spaceAfter=2,
    )
    example_style = ParagraphStyle(
        "Example",
        fontName="Times-Italic",
        fontSize=9.5,
        leading=12,
        textColor=SAGE,
        leftIndent=10,
        spaceAfter=6,
    )
    footer_style = ParagraphStyle(
        "Footer",
        fontName="Times-Italic",
        fontSize=8,
        leading=10,
        textColor=GOLD,
        alignment=TA_CENTER,
    )
    return {
        "cover_title": cover_title,
        "cover_sub": cover_sub,
        "cover_body": cover_body,
        "section_letter": section_letter,
        "word": word_style,
        "meaning": meaning_style,
        "example": example_style,
        "footer": footer_style,
    }

# ── Page background & footer ────────────────────────────────────────────────────
def page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(IVORY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=True, stroke=False)

    # Decorative border
    bm = 18
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.6)
    canvas.rect(bm, bm, PAGE_W - 2*bm, PAGE_H - 2*bm, fill=False, stroke=True)
    canvas.setStrokeColor(DUSTY_ROSE)
    canvas.setLineWidth(0.25)
    canvas.rect(bm+4, bm+4, PAGE_W - 2*(bm+4), PAGE_H - 2*(bm+4), fill=False, stroke=True)

    # Page number
    if doc.page > 1:
        canvas.setFont("Times-Italic", 8)
        canvas.setFillColor(GOLD)
        canvas.drawCentredString(PAGE_W / 2, 30, f"— {doc.page} —")

    canvas.restoreState()

# ── Cover page ─────────────────────────────────────────────────────────────────
def build_cover(styles):
    story = []
    story.append(Spacer(1, 3.5 * cm))

    # Decorative rule top
    story.append(HRFlowable(width="80%", thickness=1.2, color=GOLD, lineCap="round", spaceAfter=18))
    story.append(Paragraph("500", ParagraphStyle("num", fontName="Times-BoldItalic", fontSize=56,
                                                   leading=60, textColor=GOLD, alignment=TA_CENTER)))
    story.append(Paragraph("Aesthetic English Words", styles["cover_title"]))
    story.append(HRFlowable(width="80%", thickness=0.5, color=DUSTY_ROSE, lineCap="round", spaceBefore=8, spaceAfter=18))

    story.append(Paragraph("Their Meanings &amp; How to Use Them", styles["cover_sub"]))
    story.append(Spacer(1, 0.7 * cm))

    quote = (
        "Words are, of course, the most powerful drug used by mankind.<br/>"
        "<i>— Rudyard Kipling</i>"
    )
    story.append(Paragraph(quote, styles["cover_body"]))
    story.append(Spacer(1, 1.5 * cm))

    desc = (
        "A curated lexicon of five hundred words selected for their sonic beauty, "
        "evocative imagery, and expressive depth — from the softly archaic to the "
        "vividly modern. Each entry includes a definition and a sentence illustrating "
        "its natural use."
    )
    story.append(Paragraph(desc, ParagraphStyle("desc", fontName="Times-Roman", fontSize=10,
                                                  leading=15, textColor=colors.HexColor("#4A3A4A"),
                                                  alignment=TA_CENTER, leftIndent=50, rightIndent=50)))

    story.append(Spacer(1, 1.2 * cm))
    story.append(HRFlowable(width="40%", thickness=0.4, color=LAVENDER, lineCap="round"))
    story.append(PageBreak())
    return story

# ── How to use page ─────────────────────────────────────────────────────────────
def build_intro(styles):
    story = []
    story.append(Spacer(1, 1.5 * cm))
    story.append(Paragraph("A Note on This Collection", ParagraphStyle(
        "intro_h", fontName="Times-BoldItalic", fontSize=20, leading=24,
        textColor=DEEP_PLUM, alignment=TA_CENTER, spaceAfter=16
    )))
    story.append(HRFlowable(width="60%", thickness=0.6, color=GOLD, lineCap="round", spaceAfter=20))

    paras = [
        ("Why these words?",
         "Every word in this collection was chosen for at least one of three qualities: "
         "the way it sounds when spoken aloud, the precision with which it names something "
         "that resists easy description, or the sheer beauty it brings to a sentence. "
         "Together, they form a vocabulary of feeling, perception, and nuanced thought."),
        ("How to read it",
         "Each entry gives you the word in full, its meaning, and a sample sentence showing "
         "it in natural use. The sample sentences are designed not merely to illustrate but "
         "to demonstrate — to show the word in a context that itself has aesthetic weight."),
        ("How to use it",
         "Return to this book the way you return to a favourite place: unhurriedly, "
         "without agenda. Let a word find you rather than the other way around. "
         "When one catches, write it on paper, put it in a sentence of your own, "
         "say it aloud. Language, like any skill, deepens through use."),
    ]

    for heading, body in paras:
        story.append(Paragraph(heading, ParagraphStyle(
            "ih", fontName="Times-Bold", fontSize=11, leading=14,
            textColor=DUSTY_ROSE, spaceAfter=4, spaceBefore=12
        )))
        story.append(Paragraph(body, ParagraphStyle(
            "ib", fontName="Times-Roman", fontSize=10, leading=15,
            textColor=SOFT_BLACK, alignment=TA_JUSTIFY, spaceAfter=6
        )))

    story.append(Spacer(1, 1 * cm))
    story.append(HRFlowable(width="40%", thickness=0.4, color=LAVENDER, lineCap="round"))
    story.append(PageBreak())
    return story

# ── Vocab pages ────────────────────────────────────────────────────────────────
def build_vocab(vocab, styles):
    story = []
    current_letter = ""

    for word, meaning, example in vocab:
        first = word[0].upper()
        if first != current_letter:
            current_letter = first
            if story:
                story.append(Spacer(1, 0.3 * cm))
            story.append(HRFlowable(width="100%", thickness=0.8, color=MIST,
                                     lineCap="round", spaceBefore=8, spaceAfter=4))
            story.append(Paragraph(current_letter, styles["section_letter"]))
            story.append(HRFlowable(width="100%", thickness=0.8, color=MIST,
                                     lineCap="round", spaceAfter=8))

        block = [
            Paragraph(word, styles["word"]),
            Paragraph(meaning, styles["meaning"]),
            Paragraph(f"&ldquo;{example}&rdquo;", styles["example"]),
        ]
        story.append(KeepTogether(block))

    return story

# ── Back matter ────────────────────────────────────────────────────────────────
def build_back(styles):
    story = [PageBreak(), Spacer(1, 4 * cm)]
    story.append(HRFlowable(width="60%", thickness=1, color=GOLD, lineCap="round", spaceAfter=20))
    story.append(Paragraph("Finis", ParagraphStyle(
        "fin", fontName="Times-BoldItalic", fontSize=28,
        leading=32, textColor=DEEP_PLUM, alignment=TA_CENTER, spaceAfter=16
    )))
    story.append(Paragraph(
        "The right word is not decoration. It is revelation.",
        ParagraphStyle("fq", fontName="Times-Italic", fontSize=12,
                       leading=16, textColor=GOLD, alignment=TA_CENTER)
    ))
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="60%", thickness=0.4, color=LAVENDER, lineCap="round"))
    return story

# ── Assemble & build ────────────────────────────────────────────────────────────
def main():
    out = "/mnt/user-data/outputs/500_Aesthetic_Words.pdf"
    doc = BaseDocTemplate(
        out,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN + 0.5*cm,
        bottomMargin=MARGIN + 0.5*cm,
    )

    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        PAGE_W - 2*doc.leftMargin, PAGE_H - doc.topMargin - doc.bottomMargin,
        id="normal"
    )
    template = PageTemplate(id="main", frames=[frame], onPage=page_bg)
    doc.addPageTemplates([template])

    styles = build_styles()
    story = []
    story += build_cover(styles)
    story += build_intro(styles)
    story += build_vocab(vocab, styles)
    story += build_back(styles)

    doc.build(story)
    print(f"PDF written → {out}")

main()