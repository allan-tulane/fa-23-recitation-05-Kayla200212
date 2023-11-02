# CMPS 2200 Recitation 6
## Answers

**Name:**_kayla willis & cameron mclaren________________________


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**
 
File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |1340                     |826                |0.6164179104477612
alice29.txt    |1039367                     |676374                |0.6507557003445366
asyoulik.txt    |876253                     |606448                |0.6920923523229022
grammar.lsp    |26047                     |17356                |0.6663339348101509
fields.c    |78050                     |56206                |0.7201281229980782

There is a clear trend in the huffman implementation having a lower cost than the fixed length cost, however there is also a trend showing that the ratio between the two is growing. This would imply that the huffman coding has a higher cost with each test going down the list, but it is still decidedly lower than each fixed length cost.


- **e.**
If given a document where every character had the same frequency, all leaves would have the same depth so the cost would be lg of the number of leafs (characters AKA sigma)