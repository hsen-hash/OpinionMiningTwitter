# OpinionMiningTwitter
Python implementation of opinion mining trough tweets
Twitter Mining Project
======================

This project is a ML/NLP implementation in Python for analyzing tweets and building predictive models. The predictive models are built to help election/ad/marketing campaigns dig into social media conversations (public opinions) in order to get insights for making intelligent decisions.

The project consists of two packages and a resource directory:
<ol>
<li><b>Opinion.py</b> package contains main function that calls other subfunctions in "opinionFunction package"  .</li>
<li><b>opinionFunctions.py</b> package is designed to identify opinion words and contains five functions .</li>

</ol>

<h2> opinionFunctions Package Details:</h2>
<h3>PRE-PROCESSING</h3>
<p>Pre-processing is done to improve accuracy of Data. It also avoids unnecessary data processing in each phase. It includes Remove Unnecessary Words (Like Oh!, OMG!, Smileys, hello guys, thanks, etc.) and Non Alphabetical characters.</p>

<h3>TOKENIZE</h3>
<p>This function will read reviews from Text File. The Text Files consists of paragraphs. So the entire file will break into sentence. This sentence can individually use for mining.</p>

<h3>POS (Part Of Speech) Tagging</h3>
<p>Tagging is the process of assigning a part of speech marker to each word in an input text. Because tags are generally also applied to punctuation, tokenization is usually performed before, or as part of, the tagging process.</p>

<h3>ASPECT EXTRACTION</h3>
<p>Aspects are the important words told in a speech. The aspects for a particular domain are identified through the training process. An aspect may be a single word or a phrase. In order to extract the aspect, searching of noun and noun phrases of the reviews are needed.</p>

<h3>IDENTIFYING OPINION WORDS AND THEIR ORIENTATION</h3>
<p>Opinion words are the words which express opinion towards aspects. In the aspect-based opinion mining, the aspect related opinion words should be identified. The opinion words are mostly adjectives, verbs, adverb adjective, and adverb verb combinations. For each opinion word, we need to identify its semantic orientation, which will be used to predict the semantic orientation of each opinion sentence.

Negations should be handled appropriately to get the contextual information of a sentence. If the opinion word is in negative relation, then its priority score is reversed for negation handling purpose.</p>






