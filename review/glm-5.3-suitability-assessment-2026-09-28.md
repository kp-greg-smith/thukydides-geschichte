# GLM 5.3 as translator and coordinator for Thucydides: suitability assessment

Date: 2026-09-28
Scope: Book 1, chapters 1–120, in the English, Ukrainian and Hebrew editions produced by GLM 5.3
(as coordinator, translator and reviewer, with subagents of the same model), plus four follow-up
sessions in which GLM 5.3 was asked to review its own output and the German edition.
Reference for every judgement below: the Greek text in `docs/grc/source.xml` (Jones, Oxford),
checked where useful against the public-domain translations of Hobbes, Crawley and Jowett and
against the Loeb translation by C. F. Smith.
Author: Claude Fable 5.1, acting as external auditor; all findings verified at the Greek text.

## 1. Summary

GLM 5.3 is not suitable as an autonomous translator or coordinator for this project. It produces
readable, mostly accurate translations of narrative prose, and as a cold second reviewer it finds
genuine errors of sentence logic. But it has a gap in Ancient Greek lexical and idiomatic knowledge
that it cannot detect in itself. When it meets a construction it does not know, it does not report
uncertainty. It declares the transmitted text "obscure" or "corrupt", writes an editorial note to
that effect, and, as coordinator, enforces its misreading across all three languages against
correct translations. Shown the correct reading, it has twice called the correct reading the error.
This pattern was observed in the original translation run, in a cold re-review, in a comparison
against the German edition, and in a dedicated audit of notes, i.e. in every session so far.

The result is a translation that is good where the Greek is plain and unreliable exactly where a
reader most needs the translator: at idioms, at genuinely difficult sentences, and in the editorial
notes that are supposed to mark real textual doubt.

## 2. What GLM 5.3 does adequately

For fairness, and because the decision on how to use the model depends on it:

- Narrative sections in all three languages are, in a sample of about 30 sections across chapters
  2–120, faithful, complete and readable. Numbers, names, negations and conditionals are handled
  correctly. No copying from modern translations was detected.
- Glossary discipline is good (e.g. σπονδαί rendered "truce" 35 times, ἀρχή "empire", δουλεία
  "slavery"), spelling and name conventions are consistent apart from a handful of slips.
- As a cold second reviewer of its own output it found real errors that the auditor's sample had
  missed: UK 1.86.2 (sense inverted), EN 1.120.1 (negation scope), EN 1.120.2 ("import" for
  κατακομιδή, which is bringing produce down to the coast, i.e. export), UK 1.54.2 (a German
  pronoun left in the Ukrainian text).
- When confronted with evidence from Hobbes and Loeb, it conceded the idiom errors explicitly and
  described its own pattern accurately.

None of this changes the conclusion, because the failure class described below cannot be fixed by
running the same model more often.

## 3. The core defect: unknown idioms become "textual cruxes"

### 3.1 Cases

| Passage | Greek | Standard sense | What GLM 5.3 did |
|---|---|---|---|
| 1.116.1 | Περικλέους δεκάτου αὐτοῦ στρατηγοῦντος | "Pericles in command with nine colleagues" (Hobbes: "Pericles and nine others"; Crawley: "with nine colleagues") | Printed "Pericles himself — the tenth" and added, in all three languages, a note saying the phrase's sense is unclear. Listed the passage in the protocols as a textual crux ("δεκάτου-Crux"). |
| 1.46.2 | Ξενοκλείδης … πέμπτος αὐτός | "Xenoclides with four colleagues" (Crawley: "with four colleagues") | Printed "himself the fifth" and listed the passage as "obscure, left literal, interpretation open" in all three protocols. |
| 1.50.1 | τὰ σκάφη μὲν οὐχ εἷλκον ἀναδούμενοι τῶν νεῶν ἃς καταδύσειαν | "they did not take the hulls of the ships they had disabled in tow" | Translated ἀναδούμενοι as "giving up" and σκάφη as "ship's boats", then added a note: "the Greek text of the first clause is transmitted in harsh form". The text is not corrupt. (Corrected after the first audit.) |
| 1.84.3 | ἀμαθέστερον τῶν νόμων τῆς ὑπεροψίας παιδευόμενοι … | Hard but sound sentence: "educated too little learned to despise the laws" | EN: garbled English plus a note "parts of this sentence are transmitted in disorder". Jones prints no crux here. HE: sense inverted twice ("educated in contempt of the laws"; "boldness counts as disgrace"). UK: inverted ("educated … to despise the laws"). Both reviews passed all three. |
| 1.93.4 | τῆς θαλάσσης … ἀνθεκτέα ἐστί | "one must hold on to the sea", i.e. commit to sea power (ἀντέχομαι + genitive) | EN: "resistance must be offered at sea". In the cold re-review GLM 5.3 then criticised the Ukrainian version, which was closer to the correct sense, and praised the English one. |
| 1.114.2 | καὶ τὸ πλέον οὐκέτι προελθόντες ἀπεχώρησαν | "and without advancing any farther they went home" (τὸ πλέον adverbial) | The translators had it right. The coordinator "restored" τὸ πλέον as "for the most part" in all three languages, transferring the meaning of τὸ πλέον τοῦ χρόνου from 1.118.2, and recorded it as a blocker fix. |
| 1.120.2 | ὅσοι Ἀθηναίοις ἤδη ἐνηλλάγησαν | "those who have already had dealings with the Athenians" (LSJ; Hobbes, Crawley) | The Hebrew translator had "came into contact". The coordinator overruled it as a blocker and imposed "have been wronged by" in all three languages. |
| 1.120.3 | εὖ δὲ παρασχὸν ἐκ πολέμου πάλιν ξυμβῆναι | "when a favourable opportunity offers, to come to terms again" (Crawley, Jowett, Loeb) | All three GLM editions read "when they have given a good account of themselves". In the notes audit GLM 5.3 defended this reading from Hobbes alone and recommended changing the German edition, which is correct, to match. |
| 1.93.2 | μείζων ὁ περίβολος πανταχῇ ἐξήχθη τῆς πόλεως | "the circuit of the city was carried further out in every direction" (Crawley: "the bounds of the city were extended at every point") | Recommended correcting the German "wider than the old one" to "wider than the city itself", reading τῆς πόλεως as a genitive of comparison. |
| 1.75.1 | τοῖς Ἕλλησι μὴ οὕτως ἄγαν ἐπιφθόνως διακεῖσθαι | "not to be so excessively resented by the Greeks" | Claimed the German "the Greeks resent us" had the wrong subject. |

### 3.2 Why this is a property of the model, not of the prompt

The same passages were put to GLM 5.3 four times under different conditions:

1. Original translation and review pipeline (translator, reviewer and coordinator all GLM 5.3).
2. A fresh session, no access to protocols or prior decisions, generic review instructions, with
   control chapters mixed in. It found 2 of 7 known errors and explicitly confirmed the other five
   as correct, including the false notes at 1.116.1 ("recognised crux") and 1.84.3 ("generally
   acknowledged to be transmitted in disorder").
3. Comparison of its three editions against the German edition, which renders the idioms correctly.
   Five of its seven objections to the German were wrong (1.46.2, 1.116.1, 1.120.3, 1.93.2, 1.75.1).
   It had the correct reading in front of it and labelled it "silent resolution of a crux".
4. A dedicated audit of all 16 editorial notes, with the auditor's findings loaded into the session.
   It correctly retracted 1.116.1 and 1.46.2 after checking Hobbes and Loeb, and in the same report
   produced two new wrong recommendations (1.120.3, 1.93.2) and re-endorsed the 1.84.3 note.

A prompt that names the known idioms fixes those idioms. It does not fix the next one, because the
mechanism is missing knowledge combined with confident misattribution of that gap to the source
text. The model's confidence is not correlated with its correctness on this class of passage, so it
cannot be asked to escalate "when unsure": it was not unsure at 1.116.1.

## 4. Coordination failures

The coordinator role amplified the defect:

- **No adjudication.** Across three languages and 120 chapters the protocols record roughly 500
  reviewer findings and zero rejections. A coordinator that accepts every finding is not checking
  them against the Greek; the two coordinator "rulings" that were checked (1.114.2, 1.120.2) were
  both wrong and both replaced correct translations in three languages.
- **Correlated blind spots.** Translator, reviewer and coordinator were the same model. The
  "independent" review shared every lexical gap of the translation and additionally received the
  coordinator's rulings as premises in its prompt. HE 1.84.3 passed two reviews with two sense
  inversions.
- **Publishing over known blockers.** UK chapters 31–40 were committed with three reviewer blockers
  unapplied (1.33.3 direction of fear reversed, 1.36.2, 1.37.5); EN 41–50 was published unreviewed
  and contained the fabricated note at 1.50.1.
- **Process deviations** from the written task in the first run: one bulk commit instead of one per
  language and portion; review protocols kept only in the git-ignored `work/` directory; README and
  index updated prematurely and then reverted; the required per-language protocols created only
  after the audit.
- **Missing self-checks.** A German pronoun ("ihnen") survived into the published Ukrainian text.

## 5. Output hygiene

Every report GLM 5.3 wrote during this project contained corrupted tokens: CJK characters
("坚持", "警告", "这是一份", "地道"), block characters, fused words ("hengengeblieben",
"попередняaceut", "inhaltlicheutsch"), and stray fragments ("FloatTensor", "hará"). The published
HTML was kept clean only because a separate scan was run before each build. The model's own scan
covered the HTML files but not its reports.

## 6. Error density in the published text

Sample: 24 sections read closely against the Greek in all three languages (72 renderings), plus
10 full chapters in the cold re-review. Sense-distorting errors found in the published editions:

- EN: 1.120.1 (negation scope), 1.120.2 ("import"), 1.120.3, 1.116.1 note, 1.84.3 note, 1.93.4.
- UK: 1.84.3, 1.86.2, 1.54.2 ("ihnen"), 1.120.3, 1.116.1 note; earlier 1.33.3, 1.36.2 (fixed).
- HE: 1.84.3 (two inversions), 1.120.3, 1.116.1 note; earlier 1.84.3 passed twice.

That is roughly one sense-distorting error per 10 renderings in speeches and about one per 70 in
narrative. Extrapolated to the 110 chapters that were not closely read, the published Book 1 most
likely contains on the order of 80–120 further errors of the kinds listed above. The speeches
(chapters 32–43, 68–86, 120–124, 140–144), which the task singled out for special care, are where
the density is highest.

## 7. Why the usual mitigations do not work

- **More GLM passes.** A second cold pass found logic errors but confirmed the idiom errors. Ten
  passes would confirm them ten times. The gap is knowledge, not attention.
- **Give it the correct reading as an aid.** Tried implicitly via the German edition: it rejected
  the correct reading and defended its own.
- **Tell it where it is weak.** Tried in the notes audit: it fixed the two named idioms and made two
  new errors of the same class in the same document.
- **Ask it to escalate when unsure.** It is not unsure. It is confidently wrong and attributes the
  problem to the manuscript tradition.

## 8. Conclusion and recommendation

GLM 5.3 can be used in this project only in a subordinate role:

- as a first-draft translator of narrative prose, and
- as a cold second reviewer for sentence logic (negations, conditionals, speaker and addressee),

on condition that every editorial note, every coordinator ruling that touches more than one
language, every rejected reviewer finding, and a random sample of every batch are adjudicated by a
different model that has demonstrated correct handling of Greek idiom (in this project, the model
that produced the German revision, which rendered 1.46.2, 1.116.1, 1.93.4, 1.84.3 and 1.120.3
correctly). Without that external adjudication the pipeline produces plausible-looking text whose
notes mark the wrong passages as doubtful and whose worst errors sit in the speeches.

It should not be used as the coordinator, because the coordinator is the one role in which the
defect propagates: a wrong ruling by GLM 5.3 becomes three wrong editions and a protocol entry
that records the wrong reading as a verified decision.

## Appendix: open corrections in Book 1 (as of HEAD 104b191)

None of the following have been applied yet.

- EN 1.116.1, UK 1.116.1, HE 1.116.1: remove the note; render "Pericles with nine colleagues".
- EN/UK/HE 1.46.2: render "with four colleagues"; strike from the open-issues lists.
- EN 1.84.3: remove the note; UK 1.84.3 and HE 1.84.3 (two clauses): correct the inversions.
- EN 1.120.1: negation covers both clauses. EN 1.120.2: export, not import.
- EN/UK/HE 1.120.3: "when a favourable opportunity offers".
- UK 1.86.2: genuine four-way crux; needs external adjudication.
- UK 1.54.2: "ihnen" → "них".
- EN 1.93.4: "hold on to the sea / commit to sea power".
- Minor: UK 1.53.1 and HE 1.53.1 (herald's staff), HE 1.46.4, UK 1.84.1, HE 1.84.4, UK/HE 1.116.1
  (προσκοπή = reconnaissance), HE 1.75.4, EN 1.75.4 ("constantly"), UK Коринф/Корінф spelling.
